# Algoritmo Genético para o Problema do Caixeiro Viajante (PCV)

Este projeto implementa um algoritmo genético para resolver o Problema do Caixeiro Viajante (PCV).

## Descrição

O Problema do Caixeiro Viajante (PCV) é um problema clássico de otimização combinatória, onde o objetivo é encontrar o caminho mais curto que visita todas as cidades exatamente uma vez e retorna à cidade de origem.

Neste projeto, utilizamos um algoritmo genético para encontrar uma solução aproximada para o PCV. O algoritmo genético é uma técnica de otimização inspirada no processo de evolução natural, que utiliza conceitos de seleção natural, crossover e mutação para gerar novas soluções.

## Funcionamento

O algoritmo genético implementado neste projeto funciona da seguinte maneira:

1. **Inicialização da população**: Uma população inicial de soluções (rotas) é gerada aleatoriamente.
2. **Avaliação da aptidão**: A aptidão de cada solução é avaliada com base na distância total percorrida.
3. **Seleção de pais**: Pares de soluções são selecionados com base em sua aptidão para reprodução.
4. **Crossover**: Os pais selecionados são combinados para produzir novas soluções (filhos).
5. **Mutação**: As novas soluções podem sofrer mutações para introduzir variação na população.
6. **Substituição**: Os filhos são inseridos na população para a próxima geração.
7. **Iteração**: Os passos de 2 a 6 são repetidos por um número fixo de gerações.
8. **Resultado**: Ao final das iterações, a melhor solução encontrada é apresentada como a solução final.

## Como usar

Para executar o algoritmo, basta executar o script `main.py`. Você pode ajustar os parâmetros do algoritmo, como o número de cidades, tamanho da população, taxa de mutação e número máximo de gerações, no bloco `if __name__ == "__main__":`.

```python
if __name__ == "__main__":
    num_cidades = 10
    tamanho_populacao = 100
    taxa_mutacao = 0.01
    max_geracoes = 100
    ag_pcv = AlgoritmoGeneticoPCV(num_cidades, tamanho_populacao, taxa_mutacao, max_geracoes)
    ag_pcv.evoluir()

```

## Dependências

NumPy

