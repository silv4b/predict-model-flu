# Entendendo o Relatório de Classificação

🔙 [Voltar](../README.md)

Quando treinamos um modelo de classificação, como um modelo que prevê se uma imagem é de um cachorro ou um gato, nós queremos saber o quão bem ele está performando. Um dos jeitos mais comuns de avaliar o modelo é usando o "relatório de classificação", que nos dá várias métricas importantes. Vamos entender cada uma delas.

## Métricas do Relatório de Classificação

1. **Precisão (Precision)**
   - A precisão indica o quanto das previsões positivas do modelo estavam corretas.
   - Em outras palavras, de todas as vezes que o modelo disse "é um cachorro", quantas vezes ele acertou?
   - **Fórmula**: `Precisão = Previsões Corretas Positivas / Total de Previsões Positivas`

2. **Revocação (Recall)**
   - A revocação nos mostra o quanto o modelo encontrou dos verdadeiros exemplos positivos.
   - Aqui, queremos saber: de todos os cachorros que estavam nas imagens, quantos o modelo conseguiu detectar?
   - **Fórmula**: `Revocação = Previsões Corretas Positivas / Total de Positivos Reais`

3. **F1-Score**
   - O F1-Score combina Precisão e Revocação em uma única métrica. Ele é útil quando precisamos de um equilíbrio entre as duas métricas.
   - Se o F1-Score é alto, significa que o modelo consegue acertar as previsões positivas e não perde muitos dos exemplos positivos.
   - **Fórmula**: `F1-Score = 2 * (Precisão * Revocação) / (Precisão + Revocação)`

4. **Suporte (Support)**
   - Suporte é simplesmente a contagem de instâncias (ou amostras) reais de cada classe no conjunto de teste.
   - Ele nos ajuda a ver quantos exemplos de cada classe foram usados para calcular as métricas acima.

## Exemplo de Relatório de Classificação

Aqui está um exemplo típico de como esse relatório pode aparecer:

| Classe       | Precisão | Revocação | F1-Score | Suporte |
|--------------|----------|-----------|----------|---------|
| Cachorro     | 0.85     | 0.80      | 0.82     | 50      |
| Gato         | 0.78     | 0.85      | 0.81     | 45      |
| **Média**    | 0.82     | 0.82      | 0.82     | 95      |

### Interpretando o Exemplo

- Na linha "Cachorro", o modelo teve 85% de precisão e 80% de revocação para a classe "Cachorro".
- Isso significa que o modelo teve um bom equilíbrio em detectar "Cachorros" corretamente e sem muitos erros.
- A "Média" mostra a média das métricas para as duas classes, indicando a performance geral.

Essas métricas são importantes para entendermos o que melhorar no nosso modelo. Podemos querer focar em aumentar a Precisão ou Revocação dependendo do objetivo da aplicação.

Espero que essa explicação tenha ajudado! :)
