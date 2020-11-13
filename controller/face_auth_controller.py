import os
import numpy as np
import cv2

from flask import Flask, request
from flask_cors import CORS

UPLOAD_FOLDER = '../uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

CAMINHO_CASCADE = '../util/haarcascade_frontalface_default.xml'
classificador = cv2.CascadeClassifier(CAMINHO_CASCADE)


@app.route('/cadastro/cadastrar-usuario', methods=['POST'])
def cadastrarUsuario():
    try:
        f = request.files['arquivo']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return "true"
    except ValueError:
        return "false"


if __name__ == "__main__":
    app.run(debug=True)
