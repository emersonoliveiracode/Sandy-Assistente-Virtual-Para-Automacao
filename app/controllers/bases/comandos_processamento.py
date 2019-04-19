import os, time, re


class ComandosProcessamento(object):
    def __init__(self):
        pass

    def sensor(self, nome):
        if nome == "iluminação" or nome == "iluminacao":
            return "iluminacao"
        if nome == "lampada" or nome == "lâmpada":
            return "lampada_quarto"
        return "Desculpe-me. Não entendi a qual sensor você se referiu. Os disponíveis são iluminação e lâmpada."

    def playlist(self, acao):
        if acao == "próxima" or acao == "proxima":
            os.system("clementine -f")
            return "Próxima música"
        if acao == "anterior":
            os.system("clementine -r")
            return "Música anterior"
        if acao == "pausar":
            os.system("clementine -t")
            return "Playlist pausada"
        if acao == "play":
            os.system("clementine -t")
            return "Playlist retomada"
        return "Desculpe, os comandos disponíveis são: PRÓXIMA, ANTERIOR, PAUSAR E PLAY"


    def fechar_janela(self, janela):
        # timeout define o tempo q o xdotool fica procurando pela janela
        pipe = os.popen("timeout 2 xdotool search --sync --onlyvisible " + str(janela))  # Retorna o id, porém com um '/n' no final. Descobrir outra maneira!
        id = pipe.read()
        if id == "":
            return "Janela Não encontrada!"
        else:
            id = re.sub('[^0-9]', '', id)
            os.system("xdotool windowactivate --sync " + id + " key alt+F4")

            # Tratar erro de quando tem mais de uma janela com "o mesmo nome". Ele nã ofecha nenhuma.
        return "Prontinho. Acabei de fechar."


    def executar_programa(self, programa):
        os.system("xdotool exec " + programa + " &")
        return "Executando o programa " + programa + "."


    ##funcionando direito - Melhorar
    def alternar_pasta(self, numero):
        os.system("xdotool keydown Alt_L")
        time.sleep(2.5)
        for i in range(0,int(numero)):
            os.system("xdotool key Tab")
            time.sleep(0.5)
        os.system("xdotool keyup Alt_L")
        return "Alternando Janelas"


    def abrir_pasta(self, pasta):
        t = 0
        if pasta == "pasta":
            t = 1
        if pasta == "area":
            t = 2
        if pasta == "documentos":
            t = 3
        if pasta == "downloads" or pasta == "download":
            t = 4
        if pasta == "imagens":
            t = 5
        if pasta == "musica" or pasta == "musicas" or pasta == "música" or pasta == "músicas":
            t = 6
        if pasta == "videos":
            t = 7
        if pasta == "lixeira":
            t = 8


        os.system("xdotool key super")
        time.sleep(5)
        os.system("xdotool type --delay 215 'Arquivos' ")
        time.sleep(2)
        time.sleep(2)
        os.system("xdotool key Down")
        time.sleep(1)
        os.system("xdotool key KP_Enter")
        for i in range(0, t):
            time.sleep(1)
            os.system("xdotool key Tab")
        os.system("xdotool key KP_Enter")
        return "Feito"


    @classmethod
    def abaixar(self, id, aux):
        cont = 0
        while cont < int(aux):
            os.system("xdotool windowactivate --sync " + id + " key Down")
            time.sleep(0.5)
            cont+=1
        return "Rolagem parada!"


    def navegacao(self, palavras):
        id = 0
        for p in palavras:
            time.sleep(0.5)
            if p == "comando" or p == "Comando":
                continue
            elif p == "direita":
                os.system("xdotool windowactivate --sync " + id + " key Right")
            elif p == "esquerda":
                os.system("xdotool windowactivate --sync " + id + " key Left")
            elif p == "cima":
                os.system("xdotool windowactivate --sync " + id + " key Up")
            elif p == "baixo":
                os.system("xdotool windowactivate --sync " + id + " key Down")
            elif p == "entrar":
                os.system("xdotool windowactivate --sync " + id + " key KP_Enter")
            elif p == "voltar":
                os.system("xdotool windowactivate --sync " + id + " key BackSpace")
            elif p == "abaixar":
                pass
                pipe = os.popen("xdotool search --name " + str(palavras[1]))  # Retorna o id, porém com um '/n' no final. Descobrir outra maneira!
                id = pipe.read()
                id = re.sub('[^0-9]', '', id)
                if id == "":
                    return "Desculpe! Não encontrei..."
                if palavras[3].isdigit() == True:
                    return self.abaixar(id, palavras[3])
                else:
                    return "Número incorreto"
            else:
                pipe = os.popen("xdotool search --name " + str(p))  # Retorna o id, porém com um '/n' no final. Descobrir outra maneira!
                id = pipe.read()
                id = re.sub('[^0-9]', '', id)
        return "Feito"


    def desligar(self, palavra):
        if palavra == "computador":
            os.system("shutdown -h 1")
            print("Desligou")
        return "Desligando Computador... O computador será desligado em 1 minuto"


    def buscar(self, frase):
        palavras = frase.split()

        print(palavras)
        if palavras[1] == "abrir":
            return self.abrir_pasta(palavras[2])

        if palavras[1] == "alternar":
            return self.alternar_pasta(palavras[2])

        if palavras[1] == "desligar":
            return self.desligar(palavras[2])

        if palavras[1] == "executar":
            return self.executar_programa(palavras[2])

        if palavras[1] == "fechar":
            return self.fechar_janela(palavras[2])

        if palavras[1] == "playlist":
            return self.playlist(palavras[2])

        if palavras[1] == "sensor":
            return self.sensor(palavras[2])
        else:
            return self.navegacao(palavras)
