import tkinter as tk
from tkinter import messagebox

class QuizGUI:
    def __init__(self, quiz):
        self.quiz = quiz
        self.root = tk.Tk()
        self.root.title("Quiz App")
        self.lbl_pergunta = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.lbl_pergunta.pack(pady=20)
        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack()
        self.botoes = []
        self.entrada_aberta = None
        self.botao_enviar = None
        self.carregar_pergunta()

    def carregar_pergunta(self):
        for widget in self.frame_botoes.winfo_children():
            widget.destroy()

        pergunta = self.quiz.proxima_pergunta()
        if not pergunta:
            self.fim_do_quiz()
            return

        self.lbl_pergunta.config(text=pergunta.enunciado)
        opcoes = pergunta.get_opcoes()

        if opcoes:
            self.botoes = []
            for opcao in opcoes:
                btn = tk.Button(self.frame_botoes, text=opcao, width=40,
                                command=lambda o=opcao: self.responder(o))
                btn.pack(pady=5)
                self.botoes.append(btn)
        else:
            self.entrada_aberta = tk.Entry(self.frame_botoes, width=40)
            self.entrada_aberta.pack(pady=5)
            self.botao_enviar = tk.Button(self.frame_botoes, text="Enviar", command=self.responder_aberta)
            self.botao_enviar.pack()

    def responder(self, resposta):
        self.quiz.responder(resposta)
        self.carregar_pergunta()

    def responder_aberta(self):
        resposta = self.entrada_aberta.get()
        self.quiz.responder(resposta)
        self.carregar_pergunta()

    def fim_do_quiz(self):
        messagebox.showinfo("Fim do Quiz", f"{self.quiz.usuario.nome}, sua pontuação foi: {self.quiz.usuario.pontuacao}/{len(self.quiz.perguntas)}")
        self.root.destroy()

    def iniciar(self):
        self.root.mainloop()
