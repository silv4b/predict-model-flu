import pickle
import pandas as pd
import os


def executar_predicao():
    caminho_do_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Caminho do modelo salvo
    modelo_caminho = f"{caminho_do_projeto}\modelo\modelo_gripe.pkl"
    print(modelo_caminho)

    # Carregar o modelo treinado
    with open(modelo_caminho, "rb") as arquivo_modelo:
        modelo = pickle.load(arquivo_modelo)

    # Lista de perguntas do formulário
    perguntas = [
        "Você tem febre? (responda com 1 para sim e 0 para não): ",
        "Você sente dores no corpo? (responda com 1 para sim e 0 para não): ",
        "Você tem tosse? (responda com 1 para sim e 0 para não): ",
        "Você está com congestão nasal? (responda com 1 para sim e 0 para não): ",
        "Você sente cansaço extremo? (responda com 1 para sim e 0 para não): ",
        "Você apresenta dificuldade para respirar? (responda com 1 para sim e 0 para não): ",
        "Você tem dor de cabeça? (responda com 1 para sim e 0 para não): ",
        "Recentemente teve contato com alguém gripado? (responda com 1 para sim e 0 para não): ",
        "Você tem menos de 10 anos ou mais de 60? (responda com 1 para sim e 0 para não): ",
        "Você já teve gripe nos últimos 6 meses? (responda com 1 para sim e 0 para não): ",
    ]

    # Coletar respostas do usuário
    respostas_usuario = []
    for pergunta in perguntas:
        while True:
            try:
                resposta = int(input(pergunta))
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
    colunas = [
        "febre",
        "dores_corpo",
        "tosse",
        "congestao_nasal",
        "cansaco_extremo",
        "dificuldade_respirar",
        "dor_cabeca",
        "contato_gripado",
        "idade_risco",
        "historico_gripal",
    ]
    respostas_df = pd.DataFrame([respostas_usuario], columns=colunas)

    # Fazer a previsão com base nas respostas
    predicao = modelo.predict(respostas_df)

    # Exibir o resultado
    if predicao[0] == 1:
        print("\nResultado: Você está com sintomas de gripe.")
    else:
        print("\nResultado: Você não apresenta sintomas suficientes de gripe.")
