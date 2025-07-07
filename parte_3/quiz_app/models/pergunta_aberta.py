from .pergunta import Pergunta

class PerguntaAberta(Pergunta):
    def __init__(self, enunciado, resposta_correta, dificuldade):
        super().__init__(enunciado, resposta_correta, dificuldade)
    def get_opcoes(self):
        return []  # Sem opções visuais

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()
    
    def get_dificuldade(self):
        return self._dificuldade
