import pandas as pd
import numpy as np
import os
import shutil as st


def gerar_dados(quantidade_linhas=1000):
    caminho_do_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"\nCaminho do Projeto: {caminho_do_projeto}\n")

    # Removendo diretório de dados
    if os.path.exists(f"{caminho_do_projeto}/dados"):
        st.rmtree(f"{caminho_do_projeto}/dados")

    # Criar o diretório de dados, se ele ainda não existir
    os.makedirs(f"{caminho_do_projeto}/dados", exist_ok=True)

    print(f"Quantidade de linhas: {quantidade_linhas}")

    # Gerar dados fictícios
    np.random.seed(42)
    dados = pd.DataFrame(
        {
            "febre": np.random.randint(0, 2, quantidade_linhas),
            "dores_corpo": np.random.randint(0, 2, quantidade_linhas),
            "tosse": np.random.randint(0, 2, quantidade_linhas),
            "congestao_nasal": np.random.randint(0, 2, quantidade_linhas),
            "cansaco_extremo": np.random.randint(0, 2, quantidade_linhas),
            "dificuldade_respirar": np.random.randint(0, 2, quantidade_linhas),
            "dor_cabeca": np.random.randint(0, 2, quantidade_linhas),
            "contato_gripado": np.random.randint(0, 2, quantidade_linhas),
            "idade_risco": np.random.randint(0, 2, quantidade_linhas),
            "historico_gripal": np.random.randint(0, 2, quantidade_linhas),
        }
    )

    # Adicionar coluna de gripe (1 para gripado, 0 para não gripado)
    dados["gripe"] = (
        (
            dados["febre"]
            + dados["dores_corpo"]
            + dados["tosse"]
            + dados["congestao_nasal"]
            + dados["cansaco_extremo"]
        )
        >= 3
    ).astype(int)

    # Salvar os dados no arquivo CSV
    dados.to_csv(f"{caminho_do_projeto}/dados/dados_ficticios.csv", index=False)
    print("Dados fictícios gerados e salvos em dados/dados_ficticios.csv")
