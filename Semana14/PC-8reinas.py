import math
import random
import os
import datetime

qty = 8  # numero de reinas y tamaño de la matriz

tiempo = datetime.datetime.now()


class Reina():
    def __init__(self, x, y):
        self.x = x
        self.y = y


reinas = [Reina(x, 0) for x in range(qty)]


def printMatriz():
    matriz = [[0] * qty for x in range(qty)]
    for i in reinas:
        matriz[i.y][i.x] = 1
    for i in range(qty):
        for j in range(qty):
            print(matriz[i][j], end=" ")
        print("")
    print("=======")


def detectarColisiones():
    colisiones = 0
    for i in range(qty):  # iterar por todas las columnas
        for j in range(i + 1, qty):  # solo comprobar columnas hacia adelante
            r1 = reinas[i]
            r2 = reinas[j]
            if (r1.x == r2.x or r1.y == r2.y):  # filas y columnas
                colisiones += 1
            else:
                if (math.fabs(r1.x - r2.x) == math.fabs(r1.y - r2.y)):  # diagonales
                    colisiones += 1
    return colisiones


def moverReinas(minimo):
    min = minimo
    x_move = 0
    y_move = 0
    for i in range(qty):
        y_ori = reinas[i].y
        for j in range(qty):
            if j != y_ori:
                reinas[i].y = j
                coli = detectarColisiones()
                printMatriz()
                if (coli < min):
                    min = coli
                    x_move = i
                    y_move = j
        reinas[i].y = y_ori  # "regresa al original"
    reinas[x_move].y = y_move
    return min


def main():
    printMatriz()
    colisiones = 10000000
    while (colisiones > 0):
        n_colisiones =moverReinas(colisiones)
        if n_colisiones == colisiones:
            print("Solucion Local: " + str(colisiones))
            return;
        colisiones = n_colisiones
    print("colisiones: " + str(colisiones))
    printMatriz()


main()

print(datetime.datetime.now() - tiempo)