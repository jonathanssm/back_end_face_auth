import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getFotoComId():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    faces = []
    ids = []

    for caminhoFoto in caminhos:
        id = int(os.path.split(caminhoFoto)[-1].split('.')[1])
        face = cv2.cvtColor(cv2.imread(caminhoFoto), cv2.COLOR_BGR2GRAY)

        ids.append(id)
        faces.append(face)
    return np.array(ids), faces

ids, faces = getFotoComId()

print("Training...")
eigenface.train(faces, ids)
eigenface.write('classificadores/classificadorEigen.yml')

print("Training...")
fisherface.train(faces, ids)
fisherface.write('classificadores/classificadorFisher.yml')

print("Training...")
lbph.train(faces, ids)
lbph.write('classificadores/classificadorLBPH.yml')

print("End training.")