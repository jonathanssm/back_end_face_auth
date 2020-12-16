import os
import base64

from flask import Flask, request
from flask_cors import CORS
from PIL import Image
from io import BytesIO
from model import dimensao


dimensaoFoto = dimensao.Dimensao(220, 220)

listaPessoas = [{1, "Jonathan"}, {2, "Pessoa 1"}, {3, "Pedro V."}]

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/artigo/', methods=['GET'])
def getArtigo():
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


