#1. Uva 10369 Arctic Network

import math

class Satelites():
    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.lista = []
        self.visitados = [0]*n
        self.d = []

    def insertarPuesto(self,tupla):
        self.lista.append(tupla)

    def distance(self,i,j):
        return math.hypot(i[0]-j[0], i[1]-j[1])

    def HallarD(self):
        for index, i in enumerate(self.lista):
            mini = 99999
            self.visitados[index] = 1
            for dos, j in enumerate(self.lista):
                if i == j:
                    continue
                if not self.visitados[dos]:
                    mini = min(mini, self.distance(i, j))

            self.d.append(mini)
        self.d.sort()
        return self.d[self.n-self.s-1]

s = Satelites(4,2)
s.insertarPuesto((0,100))
s.insertarPuesto((0,300))
s.insertarPuesto((0,600))
s.insertarPuesto((150,750))

print("Minima distancia: " + str(s.HallarD()))


#Ejercicio 2:

#UVA 714


class Scribes():
    def __init__(self, n, l):
        self.n = n
        self.l = l
        self.libros = list()

    def insertarLibro(self, paginas):
        self.libros.append(paginas)


    def AsignarLibros(self):
        suma = sum(self.libros)
        approx = suma/self.n
        print(self.libros)
        conta = 0
        n = 1
        for i in range(len(self.libros)):
            if n >= self.n:
                print(self.libros[i], end =" ")
                continue
            if (i+1) > len(self.libros)-1:
                print(self.libros[i])
                return
            conta += self.libros[i]
            if conta + self.libros[i+1] > approx:
                print(str(self.libros[i])+ " / ", end =" ")
                conta = 0
                n +=1
                continue
            print(self.libros[i], end=" ")




s = Scribes(3, 9)
s.insertarLibro(100)
s.insertarLibro(200)
s.insertarLibro(300)
s.insertarLibro(400)
s.insertarLibro(500)
s.insertarLibro(600)
s.insertarLibro(700)
s.insertarLibro(800)
s.insertarLibro(900)

s.AsignarLibros()


# UVA 679