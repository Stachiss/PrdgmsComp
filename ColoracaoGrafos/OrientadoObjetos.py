class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = set()

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].add(destino)
            self.vertices[destino].add(origem)

    def colorir_grafo(self):
        # ordena os vértices em ordem decrescente pelo grau
        vertices = sorted(self.vertices, key=lambda x: len(self.vertices[x]), reverse=True)

        # inicializa um dicionário vazio para armazenar as cores dos vértices
        cores = {}

        # itera sobre os vértices e atribui cores
        for vertice in vertices:
            # inicializa um conjunto de cores disponíveis para o vértice
            cores_disponiveis = set(range(len(vertices)))

            # verifica as cores dos vértices adjacentes e remove as cores disponíveis
            for vizinho in self.vertices[vertice]:
                if vizinho in cores:
                    cor = cores[vizinho]
                    if cor in cores_disponiveis:
                        cores_disponiveis.remove(cor)

            # atribui a menor cor disponível ao vértice
            cor = min(cores_disponiveis)
            cores[vertice] = cor

        return cores


# exemplo de uso
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('A', 'D')
grafo.adicionar_aresta('B', 'C')
grafo.adicionar_aresta('C', 'D')
cores = grafo.colorir_grafo()
print(cores)
