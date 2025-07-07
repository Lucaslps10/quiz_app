import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

class QuizGUI:
    def __init__(self, quiz, on_finish=None):
        pygame.mixer.init()
        self.quiz = quiz
        self.on_finish = on_finish # Salvar referência do callback
        self.root = tk.Tk()
        self.root.title("Quiz App")

        self.lbl_pergunta = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.lbl_pergunta.pack(pady=20)

        self.label_imagem = tk.Label(self.root)
        self.label_imagem.pack()

        self.botao_repetir_audio = tk.Button(self.root, text="🔁 Repetir Som", command=self.repetir_audio)
        self.audio_atual = None
        self.audio_timer_id = None # Variável para guardar o id do timer de som



        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack()

        self.botoes = []
        self.entrada_aberta = None
        self.botao_enviar = None

        self.tempo_maximo = 15  # segundos por pergunta
        self.tempo_restante = self.tempo_maximo
        self.label_tempo = tk.Label(self.root, text="", font=("Arial", 12), fg="red")
        self.label_tempo.pack()
        self.timer_id = None

        self.root.protocol("WM_DELETE_WINDOW", self.encerrar_manual)

        self.carregar_pergunta()
        self.configurar_hotkeys()
    


    def configurar_hotkeys(self):
        self.root.bind("<a>", lambda e: self.responder_hotkey(0))
        self.root.bind("<b>", lambda e: self.responder_hotkey(1))
        self.root.bind("<c>", lambda e: self.responder_hotkey(2))
        self.root.bind("<d>", lambda e: self.responder_hotkey(3))

    def responder_hotkey(self, indice):
    
        if 0 <= indice < len(self.botoes):
            try:
                texto = self.botoes[indice]["text"]
                # Extrair apenas o texto da opção sem (A), (B), etc.
                resposta = texto.split(") ", 1)[1] if ") " in texto else texto
                self.responder(resposta)
            except (tk.TclError, IndexError):
                pass  # Ignora se o botão foi destruído antes da tecla ser processada




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

        # Dentro do método carregar_pergunta()
        imagem_path = getattr(pergunta, 'get_imagem', lambda: None)()
        if imagem_path:
            imagem = Image.open(imagem_path)
            imagem = imagem.resize((300, 200))  # redimensiona
            foto = ImageTk.PhotoImage(imagem)
            self.label_imagem.config(image=foto)
            self.label_imagem.image = foto  # evita ser coletada pelo garbage collector
        else:
            self.label_imagem.config(image='', text='')

        audio_path = getattr(pergunta, 'get_audio', lambda: None)()
        self.audio_atual = audio_path  # armazena

        if not audio_path:
            self.botao_repetir_audio.pack_forget()


        if audio_path:
            try:
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.play()
                self.botao_repetir_audio.pack(pady=5)
                
                # Parar o som após o tempo da pergunta
                if self.audio_timer_id:
                    self.root.after_cancel(self.audio_timer_id)
                self.audio_timer_id = self.root.after(self.tempo_maximo * 1000, self.parar_audio)
                
            except Exception as e:
                print(f"Erro ao reproduzir áudio: {e}")
                self.botao_repetir_audio.pack_forget()



    def repetir_audio(self):
        if self.audio_atual:
            try:
                pygame.mixer.music.load(self.audio_atual)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"Erro ao repetir áudio: {e}")

    def atualizar_tempo(self):
        if not self.root.winfo_exists():
            return  # A janela foi destruída, evita erro

        self.label_tempo.config(text=f"⏱ Tempo restante: {self.tempo_restante}s")
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.timer_id = self.root.after(1000, self.atualizar_tempo)
        else:
            messagebox.showinfo("Tempo esgotado", "Você não respondeu a tempo!")
            self.responder("")  # Trata como resposta errada


    def parar_audio(self):
        pygame.mixer.music.stop()
        self.audio_timer_id = None



    def responder(self, resposta):
        self.quiz.responder(resposta)
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        if self.audio_timer_id:
            self.root.after_cancel(self.audio_timer_id)
            self.audio_timer_id = None
            self.parar_audio()

        self.carregar_pergunta()


    def responder_aberta(self):
        resposta = self.entrada_aberta.get()
        self.quiz.responder(resposta)
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        if self.audio_timer_id:
            self.root.after_cancel(self.audio_timer_id)
            self.audio_timer_id = None
            self.parar_audio()

        self.carregar_pergunta()


    def encerrar_manual(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.root.destroy()


    def fim_do_quiz(self):
        messagebox.showinfo("Fim do Quiz", f"{self.quiz.usuario.nome}, sua pontuação foi: {self.quiz.usuario.pontuacao}/{len(self.quiz.perguntas)}")
        self.root.destroy()
       
        if self.on_finish:
            self.on_finish()  # Chamar a função passada (ex: salvar no ranking)
    

    def iniciar(self):
        self.root.mainloop()
