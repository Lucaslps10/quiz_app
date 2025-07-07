import tkinter as tk

class TelaCategorias:
    def __init__(self, temas, ao_selecionar):
        self.root = tk.Tk()
        self.root.title("Escolha uma categoria")
        self.ao_selecionar = ao_selecionar
        self.root.configure(bg="#e6f2ff")  # Cor de fundo da janela


        label = tk.Label(self.root, text="Selecione uma categoria para iniciar o quiz", font=("Arial", 14), bg="#e6f2ff")
        label.pack(pady=20)

        # Frame para organizar botões
        frame = tk.Frame(self.root, bg="#e6f2ff")
        frame.pack()

        # Botões para temas individuais
        for tema in temas:
            btn = tk.Button(frame, text=tema, width=30, bg="#007acc", command=lambda t=tema: self.selecionar_tema(t))
            btn.pack(pady=5)

        # Botão adicional para "Todas as Categorias"
        btn_todos = tk.Button(self.root, text="📚 Todas as Categorias", width=30, bg="#00b386", command=lambda: self.selecionar_tema("TODOS"))
        btn_todos.pack(pady=10)

    def selecionar_tema(self, tema):
        self.root.destroy()
        self.ao_selecionar(tema)

    def iniciar(self):
        self.root.mainloop()
