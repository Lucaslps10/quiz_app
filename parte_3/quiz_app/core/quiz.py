class Quiz:
    def __init__(self, usuario):
        self.usuario = usuario
        self.perguntas = []
        self.indice_atual = 0

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def proxima_pergunta(self):
        if self.indice_atual < len(self.perguntas):
            return self.perguntas[self.indice_atual]
        return None

    def responder(self, resposta_usuario):
        pergunta = self.perguntas[self.indice_atual]
        if pergunta.verificar_resposta(resposta_usuario):
            self.usuario.adicionar_ponto()
        self.indice_atual += 1


    def acabou(self):
        return self.indice_atual >= len(self.perguntas)
