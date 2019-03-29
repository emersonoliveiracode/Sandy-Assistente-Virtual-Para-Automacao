from flask import Flask, request
#from flask_restful import reqparse, Resource, Api
from flask import jsonify
#from app import api, db
app = Flask(__name__)

app.run(host='0.0.0.0', debug = True, port=9999)

@app.route("/")
def index():
    #print(escutar())
    #return pre_processamento("Lorem íPsulem,.")
    return "Esperando algum 'gatilho' para ativar o ESCUTAR..."

@app.route("/processar-frase")
def processar_comando(frase):
    curl("asd")
