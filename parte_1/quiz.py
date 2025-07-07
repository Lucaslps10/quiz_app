from pergunta import PerguntaAberta, PerguntaMultiplaEscolha
from usuario import Usuario

class Quiz:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__perguntas = []

    def adicionar_pergunta(self, pergunta):
        self.__perguntas.append(pergunta)

    def executar(self):
        print(f"\nIniciando o quiz para {self.__usuario.nome}!\n")
        for pergunta in self.__perguntas:
            pergunta.exibir()
            resposta = input("Sua resposta: ")
            if pergunta.verificar_resposta(resposta):
                print("✅ Correto!\n")
                self.__usuario.adicionar_ponto()
            else:
                print(f"❌ Errado! Resposta correta: {pergunta._resposta_correta}\n")
        print(f"\nPontuação final de {self.__usuario.nome}: {self.__usuario.pontuacao}/{len(self.__perguntas)}")

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    usuario = Usuario(nome)
    quiz = Quiz(usuario)

    quiz.adicionar_pergunta(
        PerguntaMultiplaEscolha(
            "Qual a capital do Brasil?",
            ["Rio de Janeiro", "São Paulo", "Brasília", "Belo Horizonte"],
            "Brasília"
        )
    )

    quiz.adicionar_pergunta(
        PerguntaAberta("Quem escreveu Dom Casmurro?", "Machado de Assis")
    )

    quiz.adicionar_pergunta(
        PerguntaMultiplaEscolha(
            "Qual a linguagem usada para desenvolver apps Flutter?",
            ["Kotlin", "Swift", "Dart", "Java"],
            "Dart"
        )
    )

    quiz.executar()
