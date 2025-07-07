from models.usuario import Usuario
from core.quiz import Quiz
from ui.gui import QuizGUI
from ui.tela_dificuldade import TelaDificuldade
from ui.tela_categorias import TelaCategorias
from core.banco_perguntas import carregar_perguntas_por_tema
from core.ranking import exibir_ranking, salvar_pontuacao
from core.banco_perguntas import carregar_todas_perguntas

def iniciar_quiz_com_tema(tema):
    tela_dif = TelaDificuldade(tema, iniciar_quiz_com_tema_e_dificuldade)
    tela_dif.iniciar()


def iniciar_quiz_com_tema_e_dificuldade(tema, dificuldade):
    nome = input("Digite seu nome: ")
    usuario = Usuario(nome)

    # ✔ carregar todas as perguntas, de acordo com o tema
    if tema == "TODOS":
        todas = carregar_todas_perguntas()
    else:
        todas = carregar_perguntas_por_tema(tema)

    # ✔ filtrar dificuldade ou não
    if dificuldade.lower() == "todos":
        perguntas = todas
    else:
        perguntas = [p for p in todas if p.get_dificuldade() == dificuldade.lower()]

    if not perguntas:
        print("⚠ Nenhuma pergunta encontrada para este tema e dificuldade.")
        return

    quiz = Quiz(usuario)
    for p in perguntas:
        quiz.adicionar_pergunta(p)

    def ao_finalizar():
        salvar_pontuacao(usuario.nome, usuario.pontuacao)
        main()

    gui = QuizGUI(quiz, on_finish=ao_finalizar)
    gui.iniciar()


def main():
    temas = ["Geografia", "Literatura", "Tecnologia", "Artes", "Sons"]
    tela = TelaCategorias(temas, iniciar_quiz_com_tema)
    tela.iniciar()

if __name__ == "__main__":
    main()
    exibir_ranking()
