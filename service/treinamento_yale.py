import cv2
import os
import numpy as np
import time

from PIL import Image

eigenface = cv2.face.EigenFaceRecognizer_create(15, 8000)
fisherface = cv2.face.FisherFaceRecognizer_create(2, 2000)
lbph = cv2.face.LBPHFaceRecognizer_create(1, 1, 7, 7, 18)


def getImagemComId():
    caminhos = [os.path.join('yalefaces/treinamento', f) for f in os.listdir('yalefaces/treinamento')]
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = Image.open(caminhoImagem).convert('L')
        imagemNP = np.array(imagemFace, 'uint8')
        id = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))
        ids.append(id)
        faces.append(imagemNP)

    return np.array(ids), faces


ids, faces = getImagemComId()

print("Treinando...")

tempo_inicio_eigenface = time.time()
eigenface.train(faces, ids)
eigenface.write('classificadores/classificadorEigenYale.yml')
print("--- %s segundos ---" % (time.time() - tempo_inicio_eigenface))

tempo_inicio_fisherface = time.time()
fisherface.train(faces, ids)
fisherface.write('classificadores/classificadorFisherYale.yml')
print("--- %s segundos ---" % (time.time() - tempo_inicio_fisherface))

tempo_inicio_lbph = time.time()
lbph.train(faces, ids)
lbph.write('classificadores/classificadorLBPHYale.yml')
print("--- %s segundos ---" % (time.time() - tempo_inicio_lbph))

print("Treinamento realizado")
