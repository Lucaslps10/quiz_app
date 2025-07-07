from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, enunciado, resposta_correta, dificuldade):
        self._enunciado = enunciado
        self._resposta_correta = resposta_correta
        self._dificuldade = dificuldade.lower()

    @property
    def enunciado(self):
        return self._enunciado

    @property
    def resposta_correta(self):
        return self._resposta_correta
    
    @property
    def dificuldade(self):
        return self._dificuldade

    @abstractmethod
    def get_opcoes(self):
        pass

    @abstractmethod
    def verificar_resposta(self, resposta_usuario):
        pass

    def get_dificuldade(self):
        return self._dificuldade