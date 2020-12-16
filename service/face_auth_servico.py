import cv2
import base64

from PIL import Image
from io import BytesIO
from model import dimensao

detectorFace = cv2.CascadeClassifier("util/haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("service/classificadores/classificadorLBPH.yml")

dimensaoFoto = dimensao.Dimensao(220, 220)

listaPessoas = [{1, "Jonathan"}, {2, "Pessoa 1"}, {3, "Pedro V."}]


def autenticar(imagem):
    imagem = Image.open(BytesIO(base64.b64decode(imagem)))
    imagem.save('uploads/image.jpeg', 'JPEG')

    imagemPath = cv2.imread('uploads/image.jpeg')
    imagemCinza = cv2.cvtColor(imagemPath, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza,
                                                    scaleFactor=1.5,
                                                    minSize=(30, 30))

    if len(facesDetectadas) > 0:
        for (x, y, l, a) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (dimensaoFoto.largura, dimensaoFoto.altura))
            id, confianca = reconhecedor.predict(imagemFace)
            nome = ""

            for idPessoa, nomePessoa in listaPessoas:
                if id == idPessoa:
                    nome = nomePessoa
                elif len(nome) < 1:
                    return "noOneFind"
    else:
        return "noFaces"

    return nome + " você foi autenticado com sucesso."


def getArtigo():
    with open('article/artigo.pdf', 'rb') as f:
        blob = base64.b64encode(f.read())

    return blob
