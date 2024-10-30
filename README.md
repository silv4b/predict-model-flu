# Projeto de Previsão de Gripe

Este projeto utiliza Machine Learning para prever se uma pessoa está com gripe com base em um formulário de 10 perguntas sobre sintomas.

## Estrutura do Projeto

- `dados/`: Contém o arquivo `dados_ficticios.csv` com os dados fictícios para treinamento.
- `docs`: Pasta com arquivos markdown do questionário e explicação do relatório de classificação.
- `modelo/`: Diretório para salvar o modelo treinado (`modelo_gripe.pkl`).
- `scripts/`: Contém scripts Python para gerar dados e treinar o modelo.
  - `gerar_dados.py`: Gera dados fictícios e salva em CSV.
  - `treinar_modelo.py`: Treina o modelo de decisão com base nos dados.
  - `executar_predicao.py`: Pequeno formulário que interage com o modelo treinado e salvo.
- `main.py`: Pequena lógica para organizar os scripts citado de forma fácil para usuários.
- `README.md`: Este aquivo :).

## Como Rodar

1. Gere os dados fictícios:

   ```bash
   python main.py
   ```

## Entendendo o Relatório de Classificação

[Relatório de Classificação](./docs/relatorio_classificacao.md)

## Questionário usado para treinamento e aplicação

Os dados neste exemplo são fictícios. [Questionário](./docs/perguntas.md).
