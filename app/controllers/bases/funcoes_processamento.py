# -*- coding: utf-8 -*-
import nltk

class FuncoesProcessamento(object):
    def __init__(self):
        pass

    def aplicar_steamer(texto):
        stop_words_nltk = nltk.corpus.stopwords.words('portuguese')
        steammer = nltk.stem.RSLPStemmer()        
        frases_steaming = []
        for(frase, emocao) in texto:
            com_steaming = [str(steammer.stem(p)) for p in frase.split() if p not in stop_words_nltk]
            frases_steaming.append((com_steaming, emocao))
        return frases_steaming

    def busca_palavras(frases):
        todas_palavras = []
        for(palavras, emocao) in frases:
            todas_palavras.extend(palavras)
        return todas_palavras

    def busca_frequencia(palavras):
        palavras = nltk.FreqDist(palavras)
        return palavras

    def busca_palavras_unicas(frequencia):
        freq = frequencia.keys()
        return freq

    #Não estou conseguindo usar aqui
    #Não estou conseguindo usar aqui
    #Não estou conseguindo usar aqui
    def extrator_palavras(documento):
        doc = set(documento)
        caracteristicas = {}
        for palavras in self.palavras_unicas:
            caracteristicas['%s' % palavras] = (palavras in doc)
        return caracteristicas
    
if __name__ == '__main__':    
    print("Base de dados de FUNÇÕES - Apenas para import!")