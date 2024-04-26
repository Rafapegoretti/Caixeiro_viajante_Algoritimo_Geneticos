import numpy as np

class AlgoritmoGeneticoPCV:
    def __init__(self, num_cidades, tamanho_populacao, taxa_mutacao, max_geracoes):
        self.num_cidades = num_cidades
        self.tamanho_populacao = tamanho_populacao
        self.taxa_mutacao = taxa_mutacao
        self.max_geracoes = max_geracoes
        self.distancias = np.random.randint(1, 100, size=(num_cidades, num_cidades))

    def inicializar_populacao(self):
        """Inicializa a população com permutações aleatórias das cidades."""
        self.populacao = np.array([np.random.permutation(self.num_cidades) for _ in range(self.tamanho_populacao)])

    def calcular_aptidao(self, rota):
        """Calcula a aptidão de uma rota, que é o inverso da distância total percorrida."""
        distancia_total = sum(self.distancias[rota[i], rota[i + 1]] for i in range(self.num_cidades - 1))
        distancia_total += self.distancias[rota[-1], rota[0]]  # Retorna à cidade inicial
        return 1 / distancia_total

    def selecionar_pais(self):
        """Seleciona dois pais aleatoriamente para o crossover, sem reposição."""
        indices = np.random.choice(range(self.tamanho_populacao), size=2, replace=False)
        return self.populacao[indices]

    def crossover(self, pai1, pai2):
        """Realiza o crossover de ordem entre dois pais para produzir um filho."""
        ponto_corte = np.random.randint(1, self.num_cidades)
        filho = np.empty(self.num_cidades, dtype=int)
        filho[:ponto_corte] = pai1[:ponto_corte]
        cidade_index = ponto_corte
        for cidade in pai2:
            if cidade not in filho[:cidade_index]:
                filho[cidade_index] = cidade
                cidade_index += 1
                if cidade_index == self.num_cidades:
                    break
        return filho

    def mutacao(self, filho):
        """Mutação por troca, trocando duas cidades na rota com uma dada probabilidade."""
        for i in range(self.num_cidades):
            if np.random.rand() < self.taxa_mutacao:
                j = np.random.randint(self.num_cidades)
                filho[i], filho[j] = filho[j], filho[i]

    def evoluir(self):
        """Executa o processo de evolução por um número definido de gerações."""
        self.inicializar_populacao()
        for geracao in range(self.max_geracoes):
            nova_populacao = np.zeros((self.tamanho_populacao, self.num_cidades), dtype=int)
            for i in range(0, self.tamanho_populacao, 2):
                pai1, pai2 = self.selecionar_pais()
                filho1 = self.crossover(pai1, pai2)
                filho2 = self.crossover(pai2, pai1)
                self.mutacao(filho1)
                self.mutacao(filho2)
                nova_populacao[i], nova_populacao[i + 1] = filho1, filho2
            self.populacao = nova_populacao
            melhor_rota = max(self.populacao, key=self.calcular_aptidao)
            melhor_aptidao = self.calcular_aptidao(melhor_rota)
            print(f"Geração {geracao + 1}: Melhor Aptidão = {melhor_aptidao:.4f}")

        melhor_rota = max(self.populacao, key=self.calcular_aptidao)
        melhor_aptidao = self.calcular_aptidao(melhor_rota)
        print(f"Melhor rota: {melhor_rota}")
        print(f"Melhor aptidão: {melhor_aptidao:.4f}")

if __name__ == "__main__":
    num_cidades = 10
    tamanho_populacao = 100
    taxa_mutacao = 0.01
    max_geracoes = 100
    ag_pcv = AlgoritmoGeneticoPCV(num_cidades, tamanho_populacao, taxa_mutacao, max_geracoes)
    ag_pcv.evoluir()
