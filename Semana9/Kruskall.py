from Semana9 import UDFS
from operator import itemgetter
class Graph:
    def __init__(self, n, m):
        self.n = n; #nodos
        self.m = m; #arisatas
        self.edges = list()

    def addEdge(self, u, v, w):
        self.edges.append((w,(u,v)))

    def kruskalMST(self):
        MST_weight = 0
        self.edges.sort(key=itemgetter(0)) # sorts

        ds = UDFS.UfdsRankPathCom(self.n)

        for w, (u, v) in self.edges:
            set_u = ds.findSet(u)
            set_v = ds.findSet(v)

            if set_u is not set_v:
                print (str(u) + " - " + str(v))
                MST_weight += w
                ds.unionSet(u,v)
        return MST_weight



def main():
    gr = Graph(9, 14)
    gr.addEdge(0, 1, 4)
    gr.addEdge(0, 7, 8)
    gr.addEdge(1, 2, 8)
    gr.addEdge(1, 7, 11)
    gr.addEdge(2, 3, 7)
    gr.addEdge(2, 8, 2)
    gr.addEdge(2, 5, 4)
    gr.addEdge(3, 4, 9)
    gr.addEdge(3, 5, 14)
    gr.addEdge(4, 5, 10)
    gr.addEdge(5, 6, 2)
    gr.addEdge(6, 7, 1)
    gr.addEdge(6, 8, 6)
    gr.addEdge(7, 8, 7)

    print("El MST es: ")
    mst_weight = gr.kruskalMST()
    print("El costo total es: " + str(mst_weight))


main()