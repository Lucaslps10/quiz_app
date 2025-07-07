from .pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, enunciado, opcoes, resposta_correta, dificuldade):
        super().__init__(enunciado, resposta_correta, dificuldade)
        self._opcoes = opcoes

    def get_opcoes(self):
        return self._opcoes

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()

    
    def get_dificuldade(self):
        return self._dificuldade
