import random
from models.pergunta_multipla import PerguntaMultiplaEscolha
from models.pergunta_aberta import PerguntaAberta
from models.pergunta_com_imagem import PerguntaComImagem
from models.pergunta_com_audio import PerguntaComAudio
from core.constantes import DIFICULDADE_FACIL, DIFICULDADE_MEDIO, DIFICULDADE_DIFICIL

# Defina essa constante no início do arquivo (ou mova para core/constantes.py se preferir reutilizar em outros arquivos)
TODOS_TEMAS = ["Geografia", "Tecnologia", "Literatura", "Artes", "Sons"]

def carregar_perguntas_por_tema(tema, dificuldade=None):
    todas = []

    if tema == "Artes":
        todas = [
            # Artes – Fácil
            PerguntaComImagem("Qual o nome desta obra?", 
                ["Mona Lisa", "O Grito", "Noite Estrelada", "Guernica"], 
                "Noite Estrelada", 
                "parte_3/quiz_app/midias/imagens/noite_estrelada.jpg",    
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaComImagem("Qual artista pintou esta obra?", 
                ["Van Gogh", "Picasso", "Da Vinci", "Monet"], 
                "Da Vinci", 
                "parte_3/quiz_app/midias/imagens/mona_Lisa.jpg", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaAberta("Quem pintou o teto da Capela Sistina?", 
                "Michelangelo",  
                dificuldade=DIFICULDADE_FACIL
            ),

            # Artes – Médio
            PerguntaComImagem("Qual o nome desta pintura expressionista?", 
                ["O Grito", "Noite Estrelada", "O Pensador", "A Persistência da Memória"], 
                "O Grito", 
                "parte_3/quiz_app/midias/imagens/o_grito.jpg", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaAberta("Qual o movimento artístico de Salvador Dalí?", 
                "Surrealismo", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaComImagem("Quem pintou esta obra cubista?", 
                ["Picasso", "Van Gogh", "Rembrandt", "Goya"], 
                "Picasso", 
                "parte_3/quiz_app/midias/imagens/guernica.jpg", 
                dificuldade=DIFICULDADE_MEDIO
                ),

            # Artes – Difícil
            PerguntaAberta("Qual artista é conhecido por suas latas de sopa Campbell?", 
                "Andy Warhol", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("Qual estilo caracteriza a arte de Jackson Pollock?", 
                ["Expressionismo Abstrato", "Cubismo", "Rococó", "Barroco"], 
                "Expressionismo Abstrato", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaAberta("Qual o nome da obra de Leonardo da Vinci que retrata uma ceia?", 
                "A Última Ceia", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaComImagem("Que pintor impressionista é autor de 'Impressão, nascer do sol'?", 
                ["Monet", "Degas", "Cézanne", "Renoir"], 
                "Monet", 
                "parte_3/quiz_app/midias/imagens/monet_nascer_sol.jpg", 
                dificuldade=DIFICULDADE_DIFICIL
            ),

        ]

    elif tema == "Geografia":
        todas = [
            PerguntaMultiplaEscolha("Qual a capital da Argentina?", 
                ["Lima", "Santiago", "Buenos Aires", "Montevidéu"], 
                "Buenos Aires",
                dificuldade=DIFICULDADE_FACIL
            ),
            # Geografia – Fácil
            PerguntaMultiplaEscolha("Qual a capital do Brasil?", 
                ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"], 
                "Brasília", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaMultiplaEscolha("Em que continente está o Egito?",
                ["Europa", "África", "Ásia", "América"], 
                "África", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaAberta("Qual é o maior oceano do mundo?",
                "Pacífico", 
                dificuldade=DIFICULDADE_FACIL
            ),

            # Geografia – Médio
            PerguntaMultiplaEscolha("Qual é o maior deserto do mundo?", 
                ["Saara", "Atacama", "Gobi", "Antártida"], 
                "Antártida", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaAberta("Quantos estados tem o Brasil?", 
                "26", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaMultiplaEscolha("Qual país tem a maior população do mundo?", 
                ["Índia", "China", "Estados Unidos", "Indonésia"], 
                "China", 
                dificuldade=DIFICULDADE_MEDIO
            ),

            # Geografia – Difícil
            PerguntaAberta("Qual a capital da Islândia?", 
                "Reykjavik", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("O rio Danúbio atravessa qual dessas cidades?", 
                ["Viena", "Paris", "Berlim", "Madrid"], 
                "Viena", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaAberta("Qual é o ponto mais alto do Brasil?", 
                "Pico da Neblina", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("Qual linha imaginária divide a Terra em hemisférios norte e sul?", 
                ["Meridiano de Greenwich", "Trópico de Câncer", "Linha do Equador", "Trópico de Capricórnio"], 
                "Linha do Equador", 
                dificuldade=DIFICULDADE_DIFICIL
            ),

                
        ]
    elif tema == "Literatura":
        todas = [
            # Literatura – Fácil
            PerguntaAberta("Quem escreveu 'Dom Casmurro'?",
                "Machado de Assis", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaMultiplaEscolha("Quem escreveu 'O Pequeno Príncipe'?", 
                ["Monteiro Lobato", "Machado de Assis", "Saint-Exupéry", "J.K. Rowling"], 
                "Saint-Exupéry", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaMultiplaEscolha("Qual é o gênero do livro 'Harry Potter'?", 
                ["Romance", "Fantasia", "Drama", "Aventura"], 
                "Fantasia", 
                dificuldade=DIFICULDADE_FACIL
            ),

            # Literatura – Médio
            PerguntaAberta("Quem escreveu 'A Metamorfose'?", 
                "Franz Kafka", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaMultiplaEscolha("Qual é o pseudônimo de Fernando Pessoa?", 
                ["Ricardo Reis", "Clarice Lispector", "Machado", "Camões"], 
                "Ricardo Reis", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaMultiplaEscolha("Em que século viveu William Shakespeare?", 
                ["XIV", "XV", "XVI", "XVII"], 
                "XVI", 
                dificuldade=DIFICULDADE_MEDIO
            ),

            # Literatura – Difícil
            PerguntaAberta("Qual autor é conhecido por criar o personagem Sherlock Holmes?", 
                "Arthur Conan Doyle", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("O romance 'Grande Sertão: Veredas' é de qual autor?", 
                ["Guimarães Rosa", "Graciliano Ramos", "Drummond", "Jorge Amado"], 
                "Guimarães Rosa", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaAberta("Qual é o nome completo de Machado de Assis?", 
                "Joaquim Maria Machado de Assis", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("Qual é o movimento literário de 'Os Lusíadas'?", 
                ["Romantismo", "Barroco", "Classicismo", "Arcadismo"], 
                "Classicismo", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("Qual é o gênero literário de 'O Alienista'?",
                ["Romance", "Crônica", "Conto", "Drama"],
                "Conto", 
                dificuldade=DIFICULDADE_DIFICIL
            ),

        ]
    elif tema == "Tecnologia":
        todas = [
            # Tecnologia – Fácil
            PerguntaMultiplaEscolha("Qual linguagem é usada pelo Flutter?", 
                ["Java", "Python", "Dart", "C++"], 
                "Dart", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaAberta("Quem criou o sistema operacional Linux?", 
                "Linus Torvalds", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaMultiplaEscolha("O que significa HTML?", 
                ["HyperText Markup Language", "HighText Machine Language", "Hyperlink Text Module Language", "Hyper Tool Markup Language"], 
                "HyperText Markup Language", 
                dificuldade=DIFICULDADE_FACIL
            ),

            # Tecnologia – Médio
            PerguntaMultiplaEscolha("O que é Git?", 
                ["Um sistema de controle de versões", "Um sistema operacional", "Um banco de dados relacional", "Uma linguagem de programação"], 
                "Um sistema de controle de versões", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaMultiplaEscolha("Qual dessas é uma linguagem de banco de dados?", 
                ["SQL", "CSS", "HTML", "C#"], 
                "SQL", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaAberta("Quem fundou a Microsoft?", 
                "Bill Gates", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            
            # Tecnologia – Difícil
            PerguntaAberta("Qual é o sistema operacional de código aberto mais usado?", 
                "Linux", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("O que é uma API?",
            ["Um banco de dados relacional", "Uma interface para comunicação entre sistemas", "Um framework de desenvolvimento web", "Um tipo de linguagem de programação"],
            "Uma interface para comunicação entre sistemas",
            dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("Qual empresa desenvolveu o navegador Chrome?", 
                ["Mozilla", "Microsoft", "Google", "Apple"], 
                "Google", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaMultiplaEscolha("O que é um algoritmo?",
                ["Um tipo de hardware", "Um software de edição de texto", "Uma sequência de passos para resolver um problema", "Um banco de dados online"],
                "Uma sequência de passos para resolver um problema",
                dificuldade=DIFICULDADE_DIFICIL
            ),
    

        ]
    elif tema == "Sons":
        # Sons – Fácil
        todas = [
            PerguntaComAudio("Qual animal faz este som?", ["Gato", "Cachorro", "Vaca", "Cavalo"], 
                "Vaca", 
                "parte_3/quiz_app/midias/sons/vaca_muu.mp3", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaComAudio("Que animal emite este som?", 
                ["Leão", "Elefante", "Gato", "Cobra"], 
                "Gato", 
                "parte_3/quiz_app/midias/sons/gato_miau.mp3", 
                dificuldade=DIFICULDADE_FACIL
            ),
            PerguntaAberta("Qual é o som típico de um cachorro?", 
                "Latido", 
                dificuldade=DIFICULDADE_FACIL
            ),

            # Sons - Méddio
            PerguntaComAudio("Identifique o som do instrumento:", 
                ["Violão", "Piano", "Flauta", "Bateria"], 
                "Violão", 
                "parte_3/quiz_app/midias/sons/violao.mp3", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaAberta("Qual animal emite o som 'relincho'?", 
                "Cavalo", 
                dificuldade=DIFICULDADE_MEDIO
            ),
            PerguntaComAudio("Qual é este som da natureza?", 
                ["Chuva", "Vento", "Trovão", "Rio"], 
                "Chuva", 
                "parte_3/quiz_app/midias/sons/chuva.mp3", 
                dificuldade=DIFICULDADE_MEDIO
            ),

            # Sons - Difícil
            PerguntaMultiplaEscolha("Qual pássaro é conhecido pelo seu canto melodioso e é símbolo da música popular brasileira?",
                ["Sabiá", "Papagaio", "Coruja", "Bem-te-vi"],
                "Sabiá",
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaAberta("Qual instrumento musical é conhecido por seu som metálico e notas longas?", 
                "Trompete", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaComAudio("Identifique o som deste transporte:", 
                ["Trem", "Carro", "Avião", "Navio"], 
                "Trem", 
                "parte_3/quiz_app/midias/sons/trem.mp3", 
                dificuldade=DIFICULDADE_DIFICIL
            ),
            PerguntaAberta("Qual animal produz o som 'rugido'?", 
                "Leão", 
                dificuldade=DIFICULDADE_DIFICIL
            ),

        ]
        



    # filtros
    if dificuldade and dificuldade.lower() != "todos":
        todas = [p for p in todas if p.get_dificuldade() == dificuldade]

    random.shuffle(todas)
    return todas


def carregar_todas_perguntas():
    """
    Carrega todas as perguntas de todos os temas, independentemente da dificuldade.
    Retorna uma lista embaralhada.
    """
    todas = []
    for tema in TODOS_TEMAS:
        todas.extend(carregar_perguntas_por_tema(tema))
    
    random.shuffle(todas)
    return todas


def carregar_todas_perguntas_por_dificuldade(dificuldade):
    """
    Carrega todas as perguntas de todos os temas filtradas por dificuldade.
    
    """
    return [p for p in carregar_todas_perguntas() if p.get_dificuldade() == dificuldade]

