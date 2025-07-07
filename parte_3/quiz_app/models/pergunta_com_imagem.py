from models.pergunta_multipla import PerguntaMultiplaEscolha

class PerguntaComImagem(PerguntaMultiplaEscolha):
    def __init__(self, enunciado, opcoes, resposta_correta, caminho_imagem, dificuldade):
        super().__init__(enunciado, opcoes, resposta_correta, dificuldade)
        self.caminho_imagem = caminho_imagem

    def get_imagem(self):
        return self.caminho_imagem
    
    def get_dificuldade(self):
        return self._dificuldade
    
    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()
