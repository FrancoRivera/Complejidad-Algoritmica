
class Nodo():
    def __init__(self, letra):
        self.letra = letra
        self.lista_adj = list()
        self.visitado = False

    def addAdj(self, nodo):
        self.lista_adj.append(nodo)

    def __str__(self):
        lista = [i for i in self.lista_adj]
        string = str(self.letra)
        for i in lista:
            string += " - " + str(i.letra)
        return string


def DFS(nodo, contador, done):
    print(nodo.letra, end=" ")
    nodo.visitado = True
    done += nodo

    if contador == 4:
        resetNodos(l_nodos, done)
        return

    for i in nodo.lista_adj:
        if i.visitado is False:
            DFS(i)


def main():

    l_nodos = list()
    l_nodos.append(Nodo("0"))
    l_nodos.append(Nodo("1"))
    l_nodos.append(Nodo("X"))
    l_nodos.append(Nodo("Y"))
    l_nodos.append(Nodo("Z"))
    l_nodos.append(Nodo("8"))
    l_nodos.append(Nodo("9"))

    l_nodos[0].addAdj(l_nodos[2])
    l_nodos[0].addAdj(l_nodos[3])
    l_nodos[0].addAdj(l_nodos[4])

    l_nodos[1].addAdj(l_nodos[2])
    l_nodos[1].addAdj(l_nodos[3])
    l_nodos[1].addAdj(l_nodos[4])

    l_nodos[2].addAdj(l_nodos[3])
    l_nodos[2].addAdj(l_nodos[4])
    l_nodos[2].addAdj(l_nodos[5])
    l_nodos[2].addAdj(l_nodos[6])

    l_nodos[3].addAdj(l_nodos[2])
    l_nodos[3].addAdj(l_nodos[4])
    l_nodos[3].addAdj(l_nodos[5])
    l_nodos[3].addAdj(l_nodos[6])

    l_nodos[4].addAdj(l_nodos[2])
    l_nodos[4].addAdj(l_nodos[3])
    l_nodos[4].addAdj(l_nodos[5])
    l_nodos[4].addAdj(l_nodos[6])

    for i in l_nodos:
        print(i)


    sources = [l_nodos[0], l_nodos[1]]

    for i in sources:
        done = list()
        DFS(i, 0, done)
        print("\n")
        resetNodos(l_nodos)

def resetNodos(nodos, done):
    for i in nodos:
        if i not in done:
            i.visitado = False

main()






