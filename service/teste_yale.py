import cv2
import os
import numpy as np
import time

from PIL import Image

detectorFace = cv2.CascadeClassifier("../util/haarcascade_frontalface_default.xml")
#reconhecedor = cv2.face.EigenFaceRecognizer_create()
#reconhecedor.read("./classificadores/classificadorEigenYale.yml")
#reconhecedor = cv2.face.FisherFaceRecognizer_create()
#reconhecedor.read("./classificadores/classificadorFisherYale.yml")
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("./classificadores/classificadorLBPHYale.yml")

totalAcertos = 0
percentualAcerto = 0.0
totalConfianca = 0.0

tempo_inicio = time.time()
caminhos = [os.path.join('yalefaces/teste', f) for f in os.listdir('yalefaces/teste')]
for caminhoImagem in caminhos:
    imagemFace = Image.open(caminhoImagem).convert('L')
    imagemFaceNP = np.array(imagemFace, 'uint8')
    facesDetectadas = detectorFace.detectMultiScale(imagemFaceNP)
    for (x, y, l, a) in facesDetectadas:
        idprevisto, confianca = reconhecedor.predict(imagemFaceNP)
        idatual = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))
        print(str(idatual) + " foi classificado como " + str(idprevisto) + " - " + str(confianca))
        if idprevisto == idatual:
            totalAcertos += 1
            totalConfianca += confianca
        #cv2.rectangle(imagemFaceNP, (x, y), (x + l, y + a), (0, 0, 255), 2)
        #cv2.imshow("Face", imagemFaceNP)
        #cv2.waitKey(1000)
percentualAcerto = (totalAcertos / len(caminhos)) * 100
totalConfianca = totalConfianca / totalAcertos
print("Percentual de acerto: " + str(percentualAcerto))
print("Total confiança: " + str(totalConfianca))
print("--- %s segundos ---" % (time.time() - tempo_inicio))

