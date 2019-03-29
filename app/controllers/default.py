from app import app, db
from flask import Flask, render_template, Response, request, redirect, url_for, flash
import psutil
import requests

# Bases
from app.controllers.bases.bot import Bot
from app.controllers.bases.comandos_processamento import ComandosProcessamento


import os, json

endereco_ip_assistente = "127.0.0.1:7000"
endereco_ip_raspberry = "192.168.0.104:80"

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/assistente-mobile')
def assistente_mobile():
    return render_template('/assistente-mobile.html')


@app.route('/cpu', methods=['GET'])
def cpu():
    cpu = psutil.cpu_percent(percpu=True)
    return str(cpu)


@app.route('/memoria', methods=['GET'])
def memoria():
    memoria = psutil.virtual_memory().percent
    return str(memoria)


@app.route('/temperatura', methods=['GET'])
def temperatura():
    temperatura = psutil.sensors_temperatures()['acpitz'][0].current
    return str(temperatura)


@app.route('/iluminacao', methods=['GET'])
def iluminacao():
    r = requests.get('http://' + endereco_ip_raspberry + '/get-luminosidade')
    print(str(r.text))
    if int(r.text) < 20:
        res = ". Iluminação ambiente satisfatória."
        return "Nível de iluminação igual a " + str(r.text) + res
    if int(r.text) < 60:
        res = "Iluminação ambiente baixa. Talvez você devesse acender uma lâmpada."
        return "Nível de iluminação igual a " + str(r.text) + res
    return "Uaaau... Está bem escuro aqui! Melhor acender uma lâmpada!"

@app.route('/lampada_quarto_status', methods=['GET'])
def lampada_quarto_status():
    r = requests.get('http://' + endereco_ip_raspberry + '/get-lampada-quarto-status')
    print(str(r.text))
    if r.text == "1":
        return "A lâmpada está desligado no momento!"
    else:
        return "A lâmpada está ligada!"

@app.route('/set-ligar-lampada-quarto', methods=['GET'])
def set_ligar_lampada_quarto():
    r = requests.get('http://' + endereco_ip_raspberry + '/set-lampada-quarto/0')
    return "Pronto! Acabei de acender."

@app.route('/set-desligar-lampada-quarto', methods=['GET'])
def set_desligar_lampada_quarto():
    r = requests.get('http://' + endereco_ip_raspberry + '/set-lampada-quarto/1')
    return "Ok! Apagada."

import re, unicodedata
####
# Normalizar, retirar acentos e caixa baixa.
####
def normalizar(frase):
    nova_frase = frase.lower()
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', nova_frase)
    frase_sem_acento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', frase_sem_acento)



####
# Detectar comando
####
@app.route('/comando/<frase>', methods=['GET'])
def detectar_comando(frase):
    cp = ComandosProcessamento()
    frase = normalizar(frase)
    resposta = cp.buscar(frase)
    if resposta == "iluminacao":
        return iluminacao()
    if resposta == "lampada_quarto":
        return lampada_quarto_status()
    return resposta



@app.route('/processar/<frase>', methods=['GET'])
def processar(frase):
    direcao = ["esquerda", "direita", "cima", "baixo"]
    frase = normalizar(frase)
    #p = IntencaoProcessamento()
    #ip.verificar_instrucao("aumentar_volume")
    bot = Bot()
    # Envio sempre o 1, pois primeiro ele detecta a emoção. Se for NEUTRO que eu procuro a intenção
    classe = bot.tratamento_emocao(frase)
    print(classe)
    if classe == "neutro":
        resposta = bot.tratamento_intencao(frase)
        if resposta == "ligar_lampada_quarto":
            return set_ligar_lampada_quarto()
        if resposta == "desligar_lampada_quarto":
            return set_desligar_lampada_quarto()
        return resposta
    else:
        return classe

#os.system("nohup x-terminal-emulator -e cvlc -Z /home/emerson/Música &")



