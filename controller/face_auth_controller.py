import os

from flask import Flask, request
from flask_cors import CORS
from service import face_auth_servico

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/artigo/', methods=['GET'])
def getArtigo():
    return face_auth_servico.getArtigo()


# Este meotod ainda nao foi finalizado
@app.route('/cadastro/cadastrar-usuario', methods=['POST'])
def cadastrarUsuario():
    try:
        arquivo = request.files['arquivo']
        arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], arquivo.filename))
        return "true"
    except ValueError:
        return "false"


@app.route('/autenticacao/autenticar-usuario', methods=['POST'])
def autenticarUsuario():
    try:
        imagem = request.json['imagem']

        return face_auth_servico.autenticar(imagem)

    except ValueError:
        return "false"
