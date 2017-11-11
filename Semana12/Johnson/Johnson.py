from Semana12.BelmanFord.BellmanFord import Graph
class JohnsonGraph(Graph):
    def __init__(self, qty):
        super(JohnsonGraph, self).__init__(qty)

    def recalcularNuevosPesos(self):
        for i in self.EDGES:
            i[2] = i[2] + self.d[i[0]] -self.d[i[1]]

    def Johnson(self):
        lista = list(self.dict.keys())
        for key in lista:
            self.addEdge("S", key, 0)
        self.BellmanFord("S")
        self.recalcularNuevosPesos()
        self.Dijkstra()

    def Dijkstra(self):
        pass


grafo = JohnsonGraph(6)
grafo.addEdge("A", "B", 1)
grafo.addEdge("B", "C", 1)
grafo.addEdge("A", "D", 99)
grafo.addEdge("D", "B", -300)



grafo.output()
grafo.Johnson()
grafo.output()
