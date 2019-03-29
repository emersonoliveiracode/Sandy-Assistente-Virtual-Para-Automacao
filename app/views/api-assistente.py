from flask import Flask, request
#from flask_restful import reqparse, Resource, Api
from flask import jsonify
#from app import api, db
app = Flask(__name__)


@app.route("/")
def index():
    import os, time
    os.system("xdotool key super")
    time.sleep(1.5)
    os.system("xdotool type --delay 215 'Arquivos' ")
    time.sleep(1.5)
    os.system("xdotool key Down")
    os.system("xdotool key KP_Enter")
    for i in range(0, 12):
        time.sleep(0.5)
        os.system("xdotool key Tab")
    os.system("xdotool key KP_Enter")

    #print(escutar())
    #return pre_processamento("Lorem íPsulem,.")
    return "Esperando algum 'gatilho' para ativar o ESCUTAR..."


# Habilitar API de reconhecimento da voz
#refazer com a API -> window.webkitSpeechRecognition
@app.route("/api/v1/escutar")
def escutar():
    import speech_recognition as sr                                 #Import api de reconhecimento
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pronto! Aguardando instruções...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            fraseR = r.recognize_google(audio, language='pt')
            return fraseR
        except():
            return None


# Pre-processamento - Caixa baixa; normalizar caractere; retirar acentos e pontuações
@app.route("/api/v1/pre-processamento")
def pre_processamento(frase):
    import unicodedata, re                                          #Import bibliotecas necessárias
    nova_frase = frase.lower()                                      # Altera todos os caracteres para caixa baixa
    nfkd = unicodedata.normalize('NFKD', nova_frase)                # Unicode normalize transforma um caracter em seu equivalente em latin.
    frase_sem_acento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    return re.sub('[^a-zA-Z0-9 \\\]', '', frase_sem_acento)         # Usa expressão regular para retornar a palavra apenas com números, letras e espaço


# Retorna se é um comando explícito (Estático) ou não
@app.route("/api/v1/detectar-comando")
def detectar_comando(frase):
    palavras = frase.split()
    if palavras[0] == "0" or palavras[0] == "zero":
        return True
    else:
        return False


# Identifica que comando estático (executar_programa; fechar_janela; ou abrir_pasta) deve ser executado
# Caso não seja um comando, ele fará a navegação através do teclado
@app.route("/api/v1/buscar-palavra")
def buscar(palavras):
    if palavras[1] == "executar":
        executar_programa(palavras[2])
    if palavras[1] == "fechar":
        fechar_janela(palavras[2])
    if palavras[1] == "abrir":
        abrir_pasta(palavras[2])
    else:
        navegacao(palavras)






app.run(host='0.0.0.0', debug = True, port=9999)





