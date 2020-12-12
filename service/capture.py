import cv2
import numpy as np

from model import dimensao

classificador = cv2.CascadeClassifier("../util/haarcascade_frontalface_default.xml")
classificadorOlho = cv2.CascadeClassifier("../util/haarcascade_eye.xml")

camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 25
id = input('Digite o id: ')
dimensaoFoto = dimensao.Dimensao(220, 220)

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor=1.5,
                                                     minSize=(150, 150))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho, scaleFactor=1.8)

        for (ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

            if cv2.waitKey(1) & 0xFF == ord('p'):
                if np.average(imagemCinza) > 110:
                    face = cv2.resize(imagemCinza[y:y + a, x:x + l], (dimensaoFoto.altura, dimensaoFoto.largura))
                    cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", face)
                    print("[foto " + str(amostra) + " capturada com sucesso.]")
                    amostra += 1

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)

    if amostra >= numeroAmostras + 1 or 0xFF == ord('b'):
        break

camera.release()
cv2.destroyAllWindows()
