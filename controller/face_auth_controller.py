import os
#import cv2

from flask import Flask, request
from flask_cors import CORS

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#camera = cv2.Video


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cadastro/cadastrar-usuario', methods=['POST'])
def cadastrarUsuario():
    try:
        f = request.files['arquivo']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return "true"
    except ValueError:
        return "false"


#def testDetectFace():
    #help(cv2.face)
    #while True:
     #   conectado, imagem = camera.read()
#
 #       cv2.imshow("Face", imagem)
  #      cv2.waitKey(1)
   # camera.read()
    #cv2.destroyAllWindows()
