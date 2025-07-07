import tkinter as tk
from core.constantes import DIFICULDADE_FACIL, DIFICULDADE_MEDIO, DIFICULDADE_DIFICIL


class TelaDificuldade:
    def __init__(self, tema, ao_selecionar):
        self.tema = tema
        self.ao_selecionar = ao_selecionar
        self.root = tk.Tk()
        self.root.title("Escolha a Dificuldade")
        self.root.configure(bg="#e6f2ff")  # Cor de fundo da janela

        label = tk.Label(self.root, text=f"Selecionar dificuldade para o tema: {tema}", font=("Arial", 14), bg="#e6f2ff")
        label.pack(pady=20)

        # Frame para os botões de dificuldade
        frame = tk.Frame(self.root, bg="#e6f2ff")
        frame.pack()

        for nivel in [DIFICULDADE_FACIL, DIFICULDADE_MEDIO, DIFICULDADE_DIFICIL]:
            btn = tk.Button(frame, text=nivel, width=30, command=lambda n=nivel: self.selecionar_dificuldade(n), bg="#007acc")
            btn.pack(pady=5)

        # Botão fora do frame
        btn_todos = tk.Button(self.root, text="⭐ Todos os Níveis", width=30, bg="#00b386", command=lambda: self.selecionar_dificuldade("TODOS"))
        btn_todos.pack(pady=10)


    def selecionar_dificuldade(self, dificuldade):
        self.root.destroy()
        self.ao_selecionar(self.tema, dificuldade)

    def iniciar(self):
        self.root.mainloop()
