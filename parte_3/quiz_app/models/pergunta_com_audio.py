from models.pergunta_multipla import PerguntaMultiplaEscolha

class PerguntaComAudio(PerguntaMultiplaEscolha):
    def __init__(self, enunciado, opcoes, resposta_correta, caminho_audio, dificuldade):
        super().__init__(enunciado, opcoes, resposta_correta, dificuldade)
        self.caminho_audio = caminho_audio

    def get_audio(self):
        return self.caminho_audio
    
    def get_dificuldade(self):
        return self._dificuldade
    
    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()
