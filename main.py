import numpy as np

class AlgoritmoGeneticoPCV:
    def __init__(self, num_cidades, tamanho_populacao, taxa_mutacao, max_geracoes):
        self.num_cidades = num_cidades
        self.tamanho_populacao = tamanho_populacao
        self.taxa_mutacao = taxa_mutacao
        self.max_geracoes = max_geracoes
        self.distancias = np.random.randint(1, 100, size=(num_cidades, num_cidades))

    def inicializar_populacao(self):
        self.populacao = np.zeros((self.tamanho_populacao, self.num_cidades), dtype=int)
        for i in range(self.tamanho_populacao):
            self.populacao[i] = np.random.permutation(self.num_cidades)

    def calcular_aptidao(self, rota):
        distancia_total = 0
        for i in range(self.num_cidades - 1):
            cidade_atual, proxima_cidade = rota[i], rota[i + 1]
            distancia_total += self.distancias[cidade_atual][proxima_cidade]
        distancia_total += self.distancias[rota[-1]][rota[0]]  # Volta à cidade inicial
        return 1 / distancia_total

    def selecionar_pais(self):
        indices = np.random.choice(range(self.tamanho_populacao), size=2, replace=False)
        return self.populacao[indices]

    def crossover(self, pai1, pai2):
        ponto_corte = np.random.randint(1, self.num_cidades)
        filho = np.zeros(self.num_cidades, dtype=int)
        filho[:ponto_corte] = pai1[:ponto_corte]
        for cidade in pai2:
            if cidade not in filho:
                filho[ponto_corte] = cidade
                ponto_corte += 1
                if ponto_corte == self.num_cidades:
                    break
        return filho

    def mutacao(self, filho):
        for i in range(self.num_cidades):
            if np.random.rand() < self.taxa_mutacao:
                j = np.random.randint(self.num_cidades)
                filho[i], filho[j] = filho[j], filho[i]

    def evoluir(self):
        self.inicializar_populacao()
        for geracao in range(self.max_geracoes):
            nova_populacao = np.zeros((self.tamanho_populacao, self.num_cidades), dtype=int)
            for i in range(0, self.tamanho_populacao, 2):
                pai1, pai2 = self.selecionar_pais()
                filho1 = self.crossover(pai1, pai2)
                filho2 = self.crossover(pai2, pai1)
                self.mutacao(filho1)
                self.mutacao(filho2)
                nova_populacao[i] = filho1
                nova_populacao[i + 1] = filho2
            self.populacao = nova_populacao
            melhor_rota = max(self.populacao, key=self.calcular_aptidao)
            melhor_aptidao = self.calcular_aptidao(melhor_rota)
            print(f"Geração {geracao + 1}: Melhor Aptidão = {melhor_aptidao}")

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