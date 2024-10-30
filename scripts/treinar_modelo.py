# treinar_modelo.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report,
)
import os
import shutil as st


def treinar_modelo():
    caminho_do_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(caminho_do_projeto)

    # Carregar os dados do arquivo CSV
    dados = pd.read_csv(f"{caminho_do_projeto}/dados/dados_ficticios.csv")

    # Separar variáveis independentes (X) e variável dependente (y)
    X = dados.drop("gripe", axis=1)
    y = dados["gripe"]

    # Dividir o dataset em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Instanciar e treinar o modelo
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_train, y_train)

    # Previsões e avaliação
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    # Exibir métricas de avaliação
    print(f"Acurácia: {acuracia:.2f}")
    print(f"Precisão: {precisao:.2f}")
    print(f"Recall: {recall:.2f}")
    print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

    # Removendo diretório de dados
    if os.path.exists(f"{caminho_do_projeto}/modelo"):
        st.rmtree(f"{caminho_do_projeto}/modelo")

    # Opcional: Salvar o modelo treinado
    os.makedirs(f"{caminho_do_projeto}/modelo", exist_ok=True)
    import pickle

    with open(f"{caminho_do_projeto}/modelo/modelo_gripe.pkl", "wb") as arquivo_modelo:
        pickle.dump(modelo, arquivo_modelo)
    print(f"Modelo treinado e salvo em {caminho_do_projeto}/modelo/modelo_gripe.pkl")
