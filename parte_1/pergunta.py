from abc import ABC, abstractmethod
# A classe 'abc' força que métodos sejam implementados nas subclasses.
# Impedir que classes base sejam instanciadas diretamente (se tiverem métodos abstratos).
# Qualquer classe que herdar da classe base será obrigada a implementar o método que 
# tenha o decorador @abstractmethod;

class Pergunta(ABC):
    def __init__(self, enunciado, resposta_correta):
        self._enunciado = enunciado
        self._resposta_correta = resposta_correta

    @abstractmethod
    def exibir(self):
        pass

    @abstractmethod
    def verificar_resposta(self, resposta_usuario):
        pass


# Pergunta de múltipla escolha
class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, enunciado, opcoes, resposta_correta):
        super().__init__(enunciado, resposta_correta)
        self._opcoes = opcoes

    def exibir(self):
        print(f"\n{self._enunciado}")
        for i, opcao in enumerate(self._opcoes, start=1):
            print(f"{i}. {opcao}")

    def verificar_resposta(self, resposta_usuario):
        try:
            resposta_index = int(resposta_usuario) - 1
            return self._opcoes[resposta_index].lower() == self._resposta_correta.lower()
        except (IndexError, ValueError):
            return False


# Pergunta dissertativa (aberta)
class PerguntaAberta(Pergunta):
    def exibir(self):
        print(f"\n{self._enunciado}")

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()
        # Remove espaços em branco e compara as respostas em minúsculas.
        # Importante: essa comparação é exata — qualquer variação na escrita da resposta 
        # (como acentos ou sinônimos) causará erro.
