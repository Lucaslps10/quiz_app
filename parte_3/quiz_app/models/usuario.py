class Usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__pontuacao = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def pontuacao(self):
        return self.__pontuacao

    def adicionar_ponto(self):
        self.__pontuacao += 1
