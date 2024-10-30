# executar_predicao.py

import pickle
import pandas as pd
import os


def executar_predicao():
    caminho_do_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Caminho do modelo salvo
    modelo_caminho = os.path.join(caminho_do_projeto, "modelo", "modelo_gripe.pkl")

    # Verifica se o caminho do arquivo existe
    if not os.path.exists(modelo_caminho):
        print("Erro: Arquivo de modelo não existe")
        return

    # Carregar o modelo treinado
    with open(modelo_caminho, "rb") as arquivo_modelo:
        modelo = pickle.load(arquivo_modelo)

    # Perguntas salvas em perguntas.txt
    perguntas = []
    caminho_perguntas = os.path.join(caminho_do_projeto, "assets", "perguntas.txt")

    # Verifica se o caminho do arquivo existe
    if not os.path.exists(caminho_perguntas):
        print("Erro: O arquivo de perguntas não foi encontrado.")
        return

    with open(caminho_perguntas, "r", encoding="utf8") as arquivo_perguntas:
        for linha in arquivo_perguntas:
            perguntas.append(linha.strip())

    # Coletar respostas do usuário
    respostas_usuario = []
    for pergunta in perguntas:
        while True:
            try:
                resposta = int(input(f"{pergunta} "))
                if resposta in [0, 1]:
                    respostas_usuario.append(resposta)
                    break
                else:
                    print("Por favor, responda com 1 para sim ou 0 para não.")
            except ValueError:
                print(
                    "Entrada inválida! Por favor, responda com 1 para sim ou 0 para não."
                )

    # Transformar as respostas em um DataFrame com nomes de colunas
    colunas = []
    caminho_colunas = os.path.join(caminho_do_projeto, "assets", "colunas.txt")

    with open(caminho_colunas, "r", encoding="utf8") as arquivo_colunas:
        for linhas in arquivo_colunas:
            colunas.append(linhas.strip())

    respostas_df = pd.DataFrame([respostas_usuario], columns=colunas)

    # Fazer a previsão com base nas respostas
    predicao = modelo.predict(respostas_df)

    # Exibir o resultado
    if predicao[0] == 1:
        print("\nResultado: Você está com sintomas de gripe.")
    else:
        print("\nResultado: Você não apresenta sintomas suficientes de gripe.")
