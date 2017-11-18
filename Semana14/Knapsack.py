import operator
class KnapSack():
    def __init__(self, weight):
        self.weight = weight
        self.list_items = []
        self.matriz = []

    def add_item(self, name, value, weight):
        self.list_items.append([name,value,weight])

    def max_value(self):
        self.list_items = sorted(self.list_items, key=operator.itemgetter(2))
        self.matriz = [[0]*(self.weight+1)for x in range(len(self.list_items))]
        for fila in range(len(self.matriz)):
            valor_item = self.list_items[fila][1]
            peso_item = self.list_items[fila][2]
            for peso in range(len(self.matriz[0])):
                if peso_item <= peso:
                    if fila == 0: #si es la primera fila
                        nuevo_valor = valor_item
                    else:
                        nuevo_valor = max(valor_item+self.matriz[fila-1][peso-peso_item],self.matriz[fila-1][peso])
                else:
                    nuevo_valor = self.matriz[fila-1][peso]
                self.matriz[fila][peso] = nuevo_valor

    def get_items(self):
        filas = len(self.matriz)
        peso = len(self.matriz[0])-1
        for i in range(filas):
            if i > 1:
                if self.matriz[filas - i][peso] == self.matriz[filas - i-1][peso]:
                    continue
                else:
                    peso -= self.list_items[filas-i][2]
                    print(self.list_items[filas-i][0])

    def print_matriz(self):
        print("\t\t\t\t", end="")
        for i in range(self.weight+1):
            print(i, end= " ")
        print("")
        for i in range(len(self.matriz)):
            print(self.list_items[i], end="\t")
            for j in range(len(self.matriz[0])):
                print(self.matriz[i][j], end=" ")
            print("")


ks = KnapSack(7)

ks.add_item("Zapato", 4, 3)
ks.add_item("Canica", 1, 1)
ks.add_item("Perfume", 5, 4)
ks.add_item("iPad Pro", 7, 5)
'''
ks.add_item("A", 11, 2)
ks.add_item("B", 13, 3)
ks.add_item("C", 12, 4)
ks.add_item("D", 10, 5)
ks.add_item("E", 15, 6)
'''
ks.max_value()
ks.print_matriz()
ks.get_items()
