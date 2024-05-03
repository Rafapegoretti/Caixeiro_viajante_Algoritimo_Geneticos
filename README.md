# Algoritmo Genético para o Problema do Caixeiro Viajante

Este projeto implementa um algoritmo genético para resolver o Problema do Caixeiro Viajante (PCV), uma questão clássica de otimização combinatória. O código em Python utiliza bibliotecas como NumPy, Matplotlib e Pandas para criar e avaliar as rotas entre cidades, com o objetivo de encontrar a menor rota possível.

## Funcionalidades

- **Cálculo de Distância:** Função que calcula a distância total percorrida para um dado percurso, considerando uma matriz de distâncias entre cidades.
- **Seleção por Torneio:** Método de seleção de indivíduos para reprodução baseado em competição entre um grupo aleatório.
- **Crossover PMX (Partially Mapped Crossover):** Técnica de crossover que preserva a relação de ordem e posição entre os elementos.
- **Mutação por Troca:** Introduz variação na população por meio da troca de duas posições aleatórias no percurso.
- **Atualização de População:** Mantém os melhores indivíduos de cada geração durante a execução do algoritmo.
- **Visualização de Rotas:** Geração de um gráfico que mostra a melhor rota encontrada pelo algoritmo.

## Uso

Para utilizar este código, é necessário ter um arquivo `distancias.csv` que contém a matriz de distâncias entre as cidades. O código irá ler este arquivo, executar o algoritmo genético e exibir os resultados tanto no console quanto graficamente.

### Dependências

Instale as seguintes dependências para executar o código:

```bash
pip install numpy pandas matplotlib
