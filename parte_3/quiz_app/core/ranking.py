import json
import os

ARQUIVO_RANKING = "ranking.json"

def carregar_ranking():
    if not os.path.exists(ARQUIVO_RANKING):
        return []
    with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_pontuacao(nome, pontuacao):
    ranking = carregar_ranking()
    ranking.append({"nome": nome, "pontuacao": pontuacao})
    ranking.sort(key=lambda x: x["pontuacao"], reverse=True)
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
        json.dump(ranking, f, indent=2)

def exibir_ranking():
    ranking = carregar_ranking()
    print("\n🏆 RANKING DOS MELHORES:")
    for i, user in enumerate(ranking[:10], 1):
        print(f"{i}. {user['nome']} - {user['pontuacao']} pontos")
