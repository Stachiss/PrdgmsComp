def colorir_grafo(grafo):
    # ordena os vértices em ordem decrescente pelo grau
    vertices = sorted(grafo, key=compara_grau, reverse=True)

    # inicializa um dicionário vazio para armazenar as cores dos vértices
    cores = {}

    # itera sobre os vértices e atribua cores
    for vertice in vertices:
        # inicializa um conjunto de cores disponíveis para o vértice
        cores_disponiveis = set(range(len(vertices)))

        # verifica as cores dos vértices adjacentes e remove as cores disponíveis
        for vizinho in grafo[vertice]:
            if vizinho in cores:
                cor = cores[vizinho]
                if cor in cores_disponiveis:
                    cores_disponiveis.remove(cor)

        # atribui a menor cor disponível ao vértice
        cor = min(cores_disponiveis)
        cores[vertice] = cor

    return cores

def compara_grau(v):
    return len(grafo[v])

# Grafo
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

cores = colorir_grafo(grafo)
print(cores)
