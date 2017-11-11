import operator
class Graph():
    def __init__(self, qty):
        self.NODES = qty;
        self.d = [0]*qty;
        self.EDGES = []
        self.P = [0]*qty;
        self.dict ={}
        self.key = 0

    def addEdge(self, u, v, w):
        if u not in self.dict:
            self.dict[u] = self.key
            self.key += 1
        if v not in self.dict:
            self.dict[v] = self.key
            self.key += 1

        self.EDGES.append([self.dict[u],self.dict[v],w])

    def BellmanFord(self, source):
        for i in range(self.NODES):
            self.d[i] = 99999999;
        self.d[self.dict[source]] = 0;

        for i in range(self.NODES-1):
            for j in range(len(self.EDGES)):
                if self.d[self.EDGES[j][0]] + self.EDGES[j][2] < self.d[self.EDGES[j][1]]:
                    self.d[self.EDGES[j][1]] = self.d[self.EDGES[j][0]] + self.EDGES[j][2]
                    self.P[self.EDGES[j][1]] = list(self.dict.keys())[list(self.dict.values()).index(self.EDGES[j][0])]
        for i in range(self.NODES - 1):
            for j in range(len(self.EDGES)):
                if self.d[self.EDGES[j][0]] + self.EDGES[j][2] < self.d[self.EDGES[j][1]]:
                    print("Graph contains negative cycle \n");

    def output(self):
        import operator
        dict = self.dict
        ordenado = sorted(dict.items(), key=operator.itemgetter(1))

        for i in ordenado:
            key = i[0]
            i = i[1]
            print(str(key) + " \tD: " + str(self.d[i]) + " \tP: "+ str(self.P[i]))
        print("================")

    def Example(self):
        self.addEdge("A", "B", 5)
        self.addEdge("B", "C", -1)
        self.addEdge("C", "A", -3)
        self.addEdge("C", "D", 3)
        self.addEdge("C", "E", -4)
        self.addEdge("D", "E", 2)

        print(self.dict)
        print(self.d)
        self.BellmanFord("S")

        print(self.d)
        print(self.P)
        print(self.dict.items())

'''
f =  open("in.txt", "r");
for line in f.readlines():
    if line != "":
        print("----" + str(line) +"---")
'''

grafo = Graph(6);


