from TdP_collections.graphs.graph import Graph
from pkg_4.esercizio4 import complete_bipartite

graph1 = Graph()
graph2 = Graph()
graph3 = Graph()
vertex = []

print("TEST GRAFO BIPARTIBILE")
for i in range(4):
    vertex.append(graph1.insert_vertex(i))

graph1.insert_edge(vertex[0], vertex[1])
graph1.insert_edge(vertex[0], vertex[2])
graph1.insert_edge(vertex[1], vertex[3])
graph1.insert_edge(vertex[2], vertex[3])

bipartibile, x, y = complete_bipartite(graph1)

if bipartibile:
    print("E' bipartibile ")
    print("Insieme di bipartizione X")
    for k in x:
        print(k)
    print("Insieme di bipartizione Y")
    for k in y:
        print(k)
else:
    print("Non e' bipartibile ")

print("_____________________________________________________")
print("TEST GRAFO NON BIPARTIBILE")
vertex = []
for i in range(4):
    vertex.append(graph2.insert_vertex(i))

graph2.insert_edge(vertex[0], vertex[1])
graph2.insert_edge(vertex[0], vertex[2])
graph2.insert_edge(vertex[1], vertex[3])
graph2.insert_edge(vertex[2], vertex[3])
graph2.insert_edge(vertex[1], vertex[2])

bipartibile, x, y = complete_bipartite(graph2)

if bipartibile:
    print("E' bipartibile ")
    print("Insieme di bipartizione X")
    for k in x:
        print(k)
    print("Insieme di bipartizione Y")
    for k in y:
        print(k)
else:
    print("Non e' bipartibile ")

print("_____________________________________________________")
print("TEST GRAFO NON BIPARTIBILE")
vertex = []
for i in range(8):
    vertex.append(graph3.insert_vertex(i))

graph3.insert_edge(vertex[0], vertex[1])
graph3.insert_edge(vertex[0], vertex[2])
graph3.insert_edge(vertex[0], vertex[3])
graph3.insert_edge(vertex[1], vertex[2])
graph3.insert_edge(vertex[1], vertex[3])
graph3.insert_edge(vertex[2], vertex[3])
graph3.insert_edge(vertex[3], vertex[5])
graph3.insert_edge(vertex[5], vertex[4])
graph3.insert_edge(vertex[4], vertex[6])
graph3.insert_edge(vertex[4], vertex[7])
graph3.insert_edge(vertex[6], vertex[7])

bipartibile, x, y = complete_bipartite(graph3)

if bipartibile:
    print("E' bipartibile ")
    print("Insieme di bipartizione X")
    for k in x:
        print(k)
    print("Insieme di bipartizione Y")
    for k in y:
        print(k)
else:
    print("Non e' bipartibile ")

print("_____________________________________________________")
print("TEST GRAFO BIPARTIBILE")
vertex = []
for i in range(8):
    vertex.append(graph3.insert_vertex(i))

graph3.insert_edge(vertex[0], vertex[1])
graph3.insert_edge(vertex[0], vertex[2])
graph3.insert_edge(vertex[0], vertex[3])
graph3.insert_edge(vertex[3], vertex[5])
graph3.insert_edge(vertex[5], vertex[4])
graph3.insert_edge(vertex[5], vertex[6])
graph3.insert_edge(vertex[4], vertex[7])

bipartibile, x, y = complete_bipartite(graph3)

if bipartibile:
    print("E' bipartibile ")
    print("Insieme di bipartizione X")
    for k in x:
        print(k)
    print("Insieme di bipartizione Y")
    for k in y:
        print(k)
else:
    print("Non e' bipartibile ")
