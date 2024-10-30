# gerar_dados.py

import pandas as pd
import numpy as np
import os
import shutil as st
import matplotlib.pyplot as plt
import seaborn as sns


def gerar_dados(quantidade_linhas=1000, exibir_df: bool = False):
    caminho_do_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

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

    if exibir_df:
        # Contagem de valores por coluna (0 e 1)
        contagens = dados.apply(pd.Series.value_counts).fillna(0)
        # Gráfico de barras das contagens de 0 e 1 por pergunta
        contagens.T.plot(kind="bar", stacked=True, figsize=(12, 6))
        plt.title("Contagem de Respostas (0 e 1) por Pergunta")
        plt.xlabel("Perguntas")
        plt.ylabel("Contagem")
        plt.legend(["Não (0)", "Sim (1)"])
        plt.xticks(rotation=45)
        plt.savefig(f"{caminho_do_projeto}/graficos/grafico_barras.png")
        plt.show()
        print("O gráfico foi salvo como 'grafico_barras.png'")

        # Exemplo para uma coluna específica (e.g., "febre")
        dados["febre"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
        plt.title("Proporção de Respostas sobre Febre")
        plt.ylabel("")  # Remove o rótulo do eixo y
        plt.savefig(f"{caminho_do_projeto}/graficos/grafico_pizza.png")
        plt.show()
        print("O gráfico foi salvo como 'grafico_pizza.png'")

        # Calcular a matriz de correlação
        correlacao = dados.corr()

        # Criar um mapa de calor
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlacao, annot=True, fmt=".2f", cmap="coolwarm", square=True)
        plt.title("Matriz de Correlação das Respostas")
        plt.savefig(f"{caminho_do_projeto}/graficos/grafico_correlacao.png")
        plt.show()
        print("O gráfico foi salvo como 'grafico_correlacao.png'")

    # Salvar os dados no arquivo CSV
    dados.to_csv(f"{caminho_do_projeto}\\dados\\dados_ficticios.csv", index=False)
    print(
        f"Dados fictícios gerados e salvos em {caminho_do_projeto}\\dados\\dados_ficticios.csv"
    )
