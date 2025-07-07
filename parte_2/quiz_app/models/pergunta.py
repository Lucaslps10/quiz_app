from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, enunciado, resposta_correta):
        self._enunciado = enunciado
        self._resposta_correta = resposta_correta

    @property
    def enunciado(self):
        return self._enunciado

    @property
    def resposta_correta(self):
        return self._resposta_correta

    @abstractmethod
    def get_opcoes(self):
        pass

    @abstractmethod
    def verificar_resposta(self, resposta_usuario):
        pass
