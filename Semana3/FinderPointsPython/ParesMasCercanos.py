from ..QuickSortPython.quicksort import *
import math
import sys

class Puntos():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class FinderPoints():

    def compareX(self,a,b):
        return a.x-b.x

    def compareY(self,a,b):
        return a.y-b.y

    def distance(self, p1, p2):
        return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)

    def min(self,x,y):
        return x if x < y else y

    def closestPairBF(self, puntos, n):
        min = sys.float_info.max
        min_1 = min_2 = Puntos(0,0)
        for i in range (0, n):
            for j in range(i+1, n):
                if self.distance(puntos[i], puntos[j]) < min:
                    min = self.distance(puntos[i], puntos[j])
                    min_1 = puntos[i]
                    min_2 = puntos[j]
        return (min_1, min_2, min)

    def stripClosest(self, strip, size, d):
        min = d
        Quicksort().sort(strip, size)
        for i in range(0, size):
            for j in range(i+1, size):
                if self.distance(strip[i], strip[j])< min:
                    min = self.distance(strip[i], strip[j])





puntos = list()

puntos.append(Puntos(2, 3))
puntos.append(Puntos(12, 30))
puntos.append(Puntos(40, 50))
puntos.append(Puntos(5, 1))
puntos.append(Puntos(12, 10))
puntos.append(Puntos(3, 4))

fp = FinderPoints()
cp = fp.closestPairBF(puntos, len(puntos))
print("the smallest distance is: " + str(cp[2]) +" Points: " + str(cp[0]) +" and " + str(cp[1]))







