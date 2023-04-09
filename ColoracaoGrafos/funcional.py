from functools import reduce


def colorir_grafo(graph):
    # ordene os vértices em ordem decrescente pelo grau
    vertices = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)

    # atribua uma cor para o primeiro vértice
    colors = {vertices[0]: 0}

    # itere sobre os vértices restantes e atribua cores
    def color_vertex(colors, vertex):
        # encontre as cores já atribuídas aos vértices adjacentes
        neighbor_colors = set(colors[neighbor] for neighbor in graph[vertex] if neighbor in colors)

        # encontre a menor cor disponível
        available_color = reduce(lambda c1, c2: c1 if c1 not in neighbor_colors else c2, range(len(vertices)))

        # crie um novo dicionário com as cores atualizadas
        new_colors = dict(colors)
        new_colors[vertex] = available_color

        return new_colors

    # aplique a função color_vertex para cada vértice restante
    colored_vertices = reduce(color_vertex, vertices[1:], colors)

    return colored_vertices


# exemplo de uso
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

colors = colorir_grafo(graph)
print(colors)
