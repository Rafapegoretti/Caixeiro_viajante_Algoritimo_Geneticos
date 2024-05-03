import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calcular_distancia(percurso, distancias):
    """Calcula a distância total de um dado percurso."""
    return sum(distancias[percurso[i], percurso[(i + 1) % len(percurso)]] for i in range(len(percurso)))

def selecao_torneio(populacao, distancias, tamanho_torneio=3):
    """Seleciona um indivíduo via torneio."""
    competidores = np.random.choice(len(populacao), tamanho_torneio, replace=False)
    vencedor = min(competidores, key=lambda x: calcular_distancia(populacao[x], distancias))
    return populacao[vencedor].copy()

def pmx(parent1, parent2):
    """Realiza o crossover PMX entre dois pais."""
    size = len(parent1)
    child = [None]*size
    cx1, cx2 = sorted(np.random.choice(size, 2, replace=False))
    mapping = {}
    for i in range(cx1, cx2 + 1):
        child[i] = parent1[i]
        mapping[parent1[i]] = parent2[i]

    for i in range(size):
        if child[i] is None:
            while parent2[i] in mapping:
                parent2[i] = mapping[parent2[i]]
            child[i] = parent2[i]
    return child

def mutacao_swap(percurso):
    """Realiza uma mutação de troca em um percurso."""
    idx1, idx2 = np.random.choice(len(percurso), 2, replace=False)
    percurso[idx1], percurso[idx2] = percurso[idx2], percurso[idx1]
    return percurso

def atualizar_populacao(populacao, nova_populacao, distancias, n_elites=1):
    """Atualiza a população com a nova geração, mantendo os melhores indivíduos."""
    combinado = populacao + nova_populacao
    combinado.sort(key=lambda x: calcular_distancia(x, distancias))
    return combinado[:len(populacao)]

def algoritmo_genetico(distancias, num_geracoes=100, tamanho_populacao=20):
    """Executa o algoritmo genético para o Problema do Caixeiro Viajante."""
    populacao = [np.random.permutation(len(distancias)) for _ in range(tamanho_populacao)]
    
    for _ in range(num_geracoes):
        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            p1 = selecao_torneio(populacao, distancias)
            p2 = selecao_torneio(populacao, distancias)
            filho = pmx(p1, p2)
            filho = mutacao_swap(filho)
            nova_populacao.append(filho)
        populacao = atualizar_populacao(populacao, nova_populacao, distancias)
    
    return populacao[0]

# Carregar a matriz de distâncias de um arquivo CSV
distancias = pd.read_csv('distancias.csv', header=None).values

# Executar o algoritmo genético
melhor_rota = algoritmo_genetico(distancias)
melhor_distancia = calcular_distancia(melhor_rota, distancias)

print("Melhor rota:", melhor_rota)
print("Distância da melhor rota:", melhor_distancia)

# Plotar a rota
coordenadas = np.random.rand(len(distancias), 2) * 10
plt.figure(figsize=(8, 6))
plt.scatter(coordenadas[:, 0], coordenadas[:, 1], color='red')
plt.title("Mapa das Cidades com Melhor Rota do Caixeiro Viajante")
for i in range(len(distancias)):
    start = melhor_rota[i]
    end = melhor_rota[(i + 1) % len(distancias)]
    plt.plot([coordenadas[start, 0], coordenadas[end, 0]], [coordenadas[start, 1], coordenadas[end, 1]], 'k-')
    plt.annotate(str(start), (coordenadas[start, 0], coordenadas[start, 1]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.grid(True)
plt.show()
