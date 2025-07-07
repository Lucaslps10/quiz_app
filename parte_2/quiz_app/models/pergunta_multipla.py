from .pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, enunciado, opcoes, resposta_correta):
        super().__init__(enunciado, resposta_correta)
        self._opcoes = opcoes

    def get_opcoes(self):
        return self._opcoes

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.lower() == self._resposta_correta.lower()
