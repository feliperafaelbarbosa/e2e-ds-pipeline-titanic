# Titanic Data Science Pipeline  

Este repositório implementa um pipeline de ciência de dados *end-to-end* para o conjunto de dados do Titanic. Ele abrange desde a ingestão e pré-processamento de dados até a visualização de insights.

Este projeto foi desenvolvido com o objetivo de apresentar as ferramentas e técnicas utilizadas nas atividades de um Cientista de Dados, servindo como uma introdução prática para amigos interessados em aprender mais sobre a área.

## Estrutura do Pipeline  
O pipeline é dividido em etapas bem definidas, conforme o arquivo `titanic-pipeline.py`.  

### 1. **Ingestão de Dados**  
Os dados são lidos a partir de uma url que fornece os dados em formato CSV utilizando o pandas.

### 2. **Exploração Inicial dos Dados**  
Análise inicial do conjunto de dados para entender a estrutura e identificar valores ausentes.

### 3. **Pré-Processamento**  
- Remoção de colunas irrelevantes.  
- Substituição de valores ausentes, como preencher a idade com a mediana.  
- Conversão de variáveis categóricas em numéricas.  

### 4. **Divisão de Dados**  
Separação em conjuntos de treino 80% e teste 20%.

### 5. **Treinamento do Modelo**  
Uso de um modelo de classificação baseado em Regressão Logística.

### 6. **Avaliação do Modelo**  
Medição do desempenho utilizando apenas a precisão do modelo.

### 7. **Visualização de Dados**  
Criação de gráficos para visualizar as distribuições variáveis, utilizando `matplotlib`.  

## Dependências  
As seguintes bibliotecas são necessárias para executar o pipeline:  
- pandas  
- numpy  
- matplotlib 
- scikit-learn  

Instale-as com:  
```bash
pip install -r requirements.txt
```  

## Licença  
Este projeto está licenciado sob a [MIT License](LICENSE).
