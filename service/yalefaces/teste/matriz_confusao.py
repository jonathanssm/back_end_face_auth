import cv2
import os
import glob
import seaborn
import time
import matplotlib.pyplot as plt

from PIL import Image
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

detectorFace = cv2.CascadeClassifier("../../../util/haarcascade_frontalface_default.xml")

lbph = cv2.face.LBPHFaceRecognizer_create()
lbph.read("../../classificadores/classificadorLBPHYale.yml")

fisher = cv2.face.FisherFaceRecognizer_create()
fisher.read("../../classificadores/classificadorFisherYale.yml")

eigen = cv2.face.EigenFaceRecognizer_create()
eigen.read("../../classificadores/classificadorEigenYale.yml")

idDetectado = []

tempo_inicio = time.time()


def getImagemTesteComId():
    ids = []
    total_confianca = 0.0
    total_acerto = 0
    for caminhoImagem in glob.glob('*.jpg'):
        imagemFace = cv2.imread(caminhoImagem)
        imagemFace = cv2.cvtColor(imagemFace, cv2.COLOR_BGR2GRAY)

        facesDetectadas = detectorFace.detectMultiScale(imagemFace,
                                                        scaleFactor=1.5,
                                                        minSize=(30, 30))
        for (x, y, l, a) in facesDetectadas:
            idFaceDetectado, confianca = fisher.predict(imagemFace)
            idAtual = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))

            if idFaceDetectado == idAtual:
                total_acerto += 1
                total_confianca += confianca

        idDetectado.append(idFaceDetectado)
        ids.append(idAtual)

    return ids, total_confianca, total_acerto


ids_teste, total_confianca, total_acerto = getImagemTesteComId()

# Avaliacoes
taxa_acerto = accuracy_score(ids_teste, idDetectado)
taxa_erro = 1 - taxa_acerto
media_confianca = (total_confianca / total_acerto)
print("Taxa Acerto " + str(taxa_acerto * 100))
print("Taxa Erro " + str(taxa_erro * 100))
print("Acuracia " + str(accuracy_score(ids_teste, idDetectado) * 100))
print("Media Confianca " + str(media_confianca))
print("--- %s segundos ---" % (time.time() - tempo_inicio))


# print(confusion_matrix(ids_teste, idDetectado))


def plot_confusion_matrix(data, labels, output_filename):
    seaborn.set(color_codes=True)
    plt.figure(1, figsize=(9, 6))

    plt.title("Confusion Matrix")

    seaborn.set(font_scale=1.4)
    ax = seaborn.heatmap(data, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Scale'})

    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)

    ax.set(ylabel="True Label", xlabel="Predicted Label")

    plt.savefig(output_filename, bbox_inches='tight', dpi=300)
    plt.close()


# define data
data = confusion_matrix(ids_teste, idDetectado)

# define labels
try:
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    plot_confusion_matrix(data, labels, "confusion_matrix.png")
except:
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    plot_confusion_matrix(data, labels, "confusion_matrix.png")

# create confusion matrix
plot = cv2.imread("confusion_matrix.png")
cv2.imshow("Plot", cv2.resize(plot, (500, 500)))
cv2.waitKey(0)
