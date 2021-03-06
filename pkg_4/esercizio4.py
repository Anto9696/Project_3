from TdP_collections.graphs.graph import Graph
from typing import Dict, List


def complete_bipartite(graph: Graph):
    """

    :param graph: grafo non diretto
    :returns: True/False se il grafo è bipartito o meno, x e y come partizioni contenenti i nodi (se bipartito)
    """
    discover = {}
    x = []
    y = []

    for vertex in graph.vertices():
        if vertex not in discover:
            discover[vertex] = 0
            x.append(vertex)
            if not bipartite(graph, vertex, x, y, discover):
                return False, None, None

    return True, x, y


def bipartite(graph: Graph, start: Graph.Vertex, x: List, y: List, discover: Dict):
    """

    :param graph: grafo non diretto
    :param start: nodo di partenza
    :param x: partizione sinistra dei nodi
    :param y: partizione destra dei nodi
    :param discover: nodi visitati
    :return: true se è bipartito, false se non lo è
    """
    level = [start]
    i = 0
    while len(level) > 0:
        next_level = []
        i = (i + 1) % 2
        for vertex in level:
            for edges in graph.incident_edges(vertex):
                opposite_vertex = edges.opposite(vertex)
                if opposite_vertex not in discover:
                    discover[opposite_vertex] = i
                    if i % 2 == 0:
                        x.append(opposite_vertex)
                    else:
                        y.append(opposite_vertex)
                    next_level.append(opposite_vertex)
                elif discover[opposite_vertex] == (i + 1) % 2:
                    # L'ho inserito nell'altro insieme e ora devo inserirlo in i ==> Errore
                    return False
        level = next_level
    return True
