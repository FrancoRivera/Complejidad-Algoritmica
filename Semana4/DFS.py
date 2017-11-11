class Graph():
    def __init__(self, n):
        self.n = n
        self.listaAd = list()
        for i in range(0, n):
            self.listaAd.append(0)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print (" " + str(v) + " ")

        for i, k in enumerate(self.listaAd[v]):
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def addEdge(self, u,v ):
        self.listaAd[u].append(v)

    def DFS(self, s):
        visitados = [False] * self.n
        self.DFSUtis(s, )

