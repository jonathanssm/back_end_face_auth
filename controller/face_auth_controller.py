import os

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS

UPLOAD_FOLDER = '../uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def test():
   return jsonify('Bem vindo.')

@app.route('/cadastro/cadastrar-usuario', methods=['GET', 'POST'])
def cadastrarUsuario():
   if request.method == 'POST':
      f = request.files['arquivo']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
      return 'Cadastro realizado com sucesso.'

if __name__ == "__main__":
    app.run(debug=True)