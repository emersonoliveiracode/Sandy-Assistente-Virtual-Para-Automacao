# -*- coding: utf-8 -*-
from app.controllers.bases.intencao_processamento import IntencaoProcessamento as ip
from app.controllers.bases.funcoes_processamento import FuncoesProcessamento as fp

from app.controllers.bases.base_emocao import Base as BaseEmocoes
from app.controllers.bases.base_intencao import Base as BaseIntencoes
import nltk

class Bot(object):
    def __init__(self):
        #POG1 - Resolver isso!!!!
        self.palavras_unicas = 0

    @classmethod
    def get_base_emocoes(self):
        return BaseEmocoes.retorna_base_emocoes(object)

    @classmethod
    def get_base_intencoes(self):
        return BaseIntencoes.retorna_base_intencoes(object)

    @classmethod
    def extrator_palavras(self, documento):
        doc = set(documento)
        caracteristicas = {}
        for palavras in self.palavras_unicas:
            caracteristicas['%s' % palavras] = (palavras in doc)
        return caracteristicas

    @classmethod
    def tratamento_emocao(self, frase):
        base = self.get_base_emocoes()
        frases_com_steaming = fp.aplicar_steamer(base)
        palavras = fp.busca_palavras(frases_com_steaming)
        frequencia = fp.busca_frequencia(palavras)
        # POG1 - Resolver isso!!!!
        self.palavras_unicas = fp.busca_palavras_unicas(frequencia)
        base_completa = nltk.classify.apply_features(self.extrator_palavras, frases_com_steaming)
        classificador = nltk.NaiveBayesClassifier.train(base_completa)
        classificador.labels()  # Classes
        teste_steaming = []
        stemmer = nltk.stem.RSLPStemmer()
        for (palavras) in frase.split():
            com_steam = [p for p in palavras.split()]
            teste_steaming.append(str(stemmer.stem(com_steam[0])))

        novo = self.extrator_palavras(teste_steaming)
        classificadorEmocao = nltk.NaiveBayesClassifier.train(base_completa)
        classe = classificadorEmocao.classify(novo)
        print(classe)
        print(classe)
        print(classe)
        print(classe)
        return classe


    # Não preciso MAIS
    def tratamento_intencao(self, frase):
        base = self.get_base_intencoes()
        frases_com_steaming = fp.aplicar_steamer(base)
        palavras = fp.busca_palavras(frases_com_steaming)
        frequencia = fp.busca_frequencia(palavras)
        self.palavras_unicas = fp.busca_palavras_unicas(frequencia)
        base_completa = nltk.classify.apply_features(self.extrator_palavras, frases_com_steaming)
        classificador = nltk.NaiveBayesClassifier.train(base_completa)
        classificador.labels()  # Classes
        teste_steaming = []
        stemmer = nltk.stem.RSLPStemmer()
        for (palavras) in frase.split():
            com_steam = [p for p in palavras.split()]
            teste_steaming.append(str(stemmer.stem(com_steam[0])))

        novo = self.extrator_palavras(teste_steaming)
        classificadorIntencao = nltk.NaiveBayesClassifier.train(base_completa)
        classe = classificadorIntencao.classify(novo)

        # Retorna a probabilidade
        # distribuicao = classificador.prob_classify(novo)
        # for classe in distribuicao.samples():
        #    print("%s: %f" %(classe, distribuicao.prob(classe)))

        return ip.verificar_instrucao(ip, classe, frase)
