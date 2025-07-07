from .pergunta import Pergunta

class PerguntaAberta(Pergunta):
    def get_opcoes(self):
        return []  # Sem opções visuais

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()
