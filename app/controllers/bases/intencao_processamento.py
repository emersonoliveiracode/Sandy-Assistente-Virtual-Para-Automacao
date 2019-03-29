# -*- coding: utf-8 -*-

import nltk
import os
import webbrowser


import threading
import time

class IntencaoProcessamento(object):
    def __init__(self):
        pass
    #Ver como fazer para sempre abrir em uma nova janela
    @classmethod
    def abrir_facebook(self):
        webbrowser.open_new("http://www.facebook.com")
        return "Facebook Aberto"

    @classmethod
    def aumentar_volume(self):
        os.system("amixer -D pulse sset Master 20%+")
        return "Volume +20%"

    @classmethod
    def diminuir_volume(self):
        os.system("amixer -D pulse sset Master 20%-")
        return "Volume -20%"

    @classmethod
    def abrir_github(self):
        webbrowser.open("https://github.com/")
        return "Github Aberto"

    @classmethod
    def abrir_youtube(self):
        webbrowser.open("https://www.youtube.com/watch?v=RBumgq5yVrA&t=0s&list=PL7JUHWfnc1ROIEdxsnxB4e56kQvAyYx2X&index=17")
        return "Youtube Aberto"

    # usar para os 3
    #https: // www.lexico.pt /
    @classmethod
    def buscar_sinonimo(self, frase):
        lista_palavras = ["qual", "o", "buscar", "busca", "por", "sinonimo", "sinônimo", "pesquisar",
                          "pesquise", "pesquisa", "de", "significado"]
        frase = frase.split(" ")
        new_frase = []

        for pal in frase:
            if pal not in lista_palavras:
                new_frase.append(pal)

        n = " ".join(new_frase)

        webbrowser.open("https://www.google.com.br/search?q=sinonimo+" + n)
        return "sinonimo de :" + n

    @classmethod
    def buscar_antonimo(self):
        palavra = "pertinente"
        webbrowser.open("https://www.google.com.br/search?q=antonimo+" + palavra)
        return "antonimo de :" + palavra

    @classmethod
    def buscar_significado(self, frase):
        lista_palavras = ["qual", "o" "buscar", "busca", "por", "google", "internet", "sobre", "pesquisar",
                                 "pesquise", "pesquisa", "no", "na", "de", "significado"]
        frase = frase.split(" ")
        new_frase = []

        for pal in frase:
            if pal not in lista_palavras:
                new_frase.append(pal)

        n = " ".join(new_frase)
        webbrowser.open("https://www.google.com.br/search?q=" + n)
        return "significado de " + n

        palavra = "pertinente"
        webbrowser.open("https://www.google.com.br/search?q=significado+" + palavra)
        return "significado de :" + palavra

    @classmethod
    def hora_atual(self):
        from datetime import datetime
        now = datetime.now()
        # return str(now.day) + "/" + str(now.month) + "/" + str(now.ynohup x-terminal-emulator -e cvlc -Z /home/haw/Música &ear) + "
        hora_atual = str(now.hour) + " horas, " + str(now.minute) + " minutos e " + str(now.second) + " segundos"
        return str(hora_atual)

    @classmethod
    def tocar_musica(self):
        os.system("x-terminal-emulator -e clementine -p /home/emerson/Música/ &")
        return "Playlist carregada!"


    #Não funciona se não usar o recurso **kwargs
    @classmethod
    def buscar_no_google(self, frase):
        lista_palavras_google = ["buscar", "busca", "por", "google", "internet", "sobre", "pesquisar",
                                 "pesquise", "pesquisa", "no", "na"]
        frase = frase.split(" ")
        new_frase = []

        for pal in frase:
            if pal not in lista_palavras_google:
                new_frase.append(pal)

        n = " ".join(new_frase)

        import re
        import wikipedia
        wikipedia.set_lang('pt')
        sentencas = wikipedia.search(n)
        for primeira in sentencas:
            n = str(wikipedia.summary(primeira, sentences=0))  # Sentences = 1 busca 1 sentença de cada
            break
        n = re.sub("\(", " ", str(n))

        #webbrowser.open("https://www.google.com.br/search?q=" + n)
        return n


    @classmethod
    def contar_piada(self):
        from random import randint
        piadas = ["Qual a diferença entra a mulher e a arma?. Na arma você pode colocar um silenciador.",
                  "A professora chega para o Joãozinho e diz: Joãozinho qual é o tempo da frase: Eu procuro um homem fiel? E então Joãozinho responde. É tempo perdido!",
                  "Porque o elefante nao pega fogo? Porque ele já é cinza",
                  "Porque o elefante nao pega fogo? Porque ele já é cinza",
                  "Se o cachorro tivesse religião, qual seria? Cao-domblé",
                  "O que o cavalo foi fazer no orelhão? Passar um trote",
                  "O que o tomate foi fazer no banco? Foi tirar extrato",
                  "O que dá o cruzamento de pão, queijo e um macaco? X-panzé",
                  "Por que não é bom guardar o quibe no freezer? Porque lá dentro ele esfirra",
                  "Por que as plantinhas não falam? Porque elas são mudas. ",
                  "Por que o galo canta de olhos fechados? Porque ele já sabe a letra da música decor",
                  "Como o Batman faz para que abram a bat-caverna? Ele bat-palma.",
                  "Como se faz omelete de chocolate ? Com ovos de páscoa!",
                  "Para que serve óculos verde ? Para verde perto.",
                  "Para que serve óculos vermelho? Para vermelhor ",
                  "Para que serve óculos marrom? Para ver marromenos",
                  "Por que a mulher do Hulk divorciou-se dele? Porque ela queria um homem mais maduro",
                  "Por que o jacaré tirou o jacarezinho da escola? Porque ele réptil de ano.",
                  "Você conhece a piada do fotógrafo? Não né. Porque Ainda nao foi revelada.",
                  "Como se fala top-less em chinês? Xem-chu-tian.",
                  " Manoel vai às compras.. O português, com a lista de compras na mão, diz ao rapaz que o atende:- Eu queria dois quilos de carne, um quilo de linguiça, duas dúzias de ovos, um quilo de batata...- Espera um pouco! O senhor é português, não é?- Sim... Descobristes pelo meu sutaque?- Não! É que isto aqui é uma farmácia!",
                  "O Garoto e a feijoada A mãe chamou o filho e disse: - Filhinho! Amanhã eu vou fazer uma feijoada completa. Liga pro açougue e vê se tem tudo isso aqui! A mãe deu a lista de ingredientes pro garoto, que telefonou para o açougue. - É o açougueiro? - É sim... - O senhor tem pé de porco? - Tenho. - Tem orelha de porco? - Tenho. - Tem costela de porco? - Tenho. - Tem rabo de porco? - Tenho. - Tem fucinho de porco? - Tenho. - Nossa, como o senhor é feio!"]
        return str(piadas[randint(0,len(piadas))])



    def verificar_instrucao(self, classe, frase):
        if (classe == "abrir_facebook"):
            return self.abrir_facebook()

        elif (classe == "aumentar_volume"):
            return self.aumentar_volume()

        elif (classe == "diminuir_volume"):
            return self.diminuir_volume()

        elif (classe == "abrir_youtube"):
            return self.abrir_youtube()

        elif (classe == "buscar_sinonimo"):
            return self.buscar_sinonimo(frase)

        elif (classe == "buscar_antonimo"):
            return self.buscar_antonimo(frase)

        elif (classe == "buscar_significado"):
            return self.buscar_significado(frase)

        elif (classe == "hora_atual"):
            return self.hora_atual()

        elif (classe == "tocar_musica"):
            return self.tocar_musica()

        elif (classe == "contar_piada"):
            return self.contar_piada()

        elif (classe == "ligar_lampada_quarto"):
            return "ligar_lampada_quarto"

        elif (classe == "desligar_lampada_quarto"):
            return "desligar_lampada_quarto"

        elif (classe == "buscar_no_google"):
            return self.buscar_no_google(frase)

#Funções para implementar!!!!
#Fechar terminal que está com a música executando
#Fechar página/navegador aberto
#Encontrar uma pasta/documento no computador
#Navegar entre pastas
#Enviar kwargs para função buscar_sinonimo e antonimo

if __name__ == '__main__':
    print("Base de dados de EMOÇÕES - Apenas para import!")

#Jeito correto
#xdotool    windowactivate - -sync    39873743    key    F5