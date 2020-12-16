import os
import base64
import cv2

from flask import Flask, request, make_response
from flask_cors import CORS
from PIL import Image
from io import BytesIO

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/artigo/', methods=['GET'])
def send_pdf():
    with open('./article/artigo.pdf', 'rb') as f:
        blob = base64.b64encode(f.read())

    return blob


@app.route('/cadastro/cadastrar-usuario', methods=['POST'])
def cadastrarUsuario():
    try:
        f = request.files['arquivo']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return "true"
    except ValueError:
        return "false"


