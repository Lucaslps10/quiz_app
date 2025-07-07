from models.usuario import Usuario
from models.pergunta_multipla import PerguntaMultiplaEscolha
from models.pergunta_aberta import PerguntaAberta
from core.quiz import Quiz
from ui.gui import QuizGUI

def main():
    usuario = Usuario("Lucas")
    quiz = Quiz(usuario)

    quiz.adicionar_pergunta(
        PerguntaMultiplaEscolha("Qual a capital do Brasil?", ["São Paulo", "Rio", "Brasília", "BH"], "Brasília")
    )
    quiz.adicionar_pergunta(
        PerguntaAberta("Quem escreveu Dom Casmurro?", "Machado de Assis")
    )
    quiz.adicionar_pergunta(
        PerguntaMultiplaEscolha("Linguagem usada no Flutter?", ["Java", "Dart", "Python", "Kotlin"], "Dart")
    )

    gui = QuizGUI(quiz)
    gui.iniciar()

if __name__ == "__main__":
    main()
