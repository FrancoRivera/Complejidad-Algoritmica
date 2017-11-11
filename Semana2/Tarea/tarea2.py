
import datetime

def swap(str, a, b):
    n_str = list(str)
    aux = n_str[a]
    n_str[a] = n_str[b]
    n_str[b] = aux
    return ''.join(n_str)


def permutaciones(str, i, n):
    if i == n-1:
        print(str)
        return

    for j in range(i, n):
        # if str[i] == str[j] and i != j:
        #    continue
        #
        str = swap(str, i, j)
        permutaciones(str, i+1, n)
        str = swap(str, i, j)

past = datetime.datetime.now()
string = "ABC"
permutaciones(string, 0, len(string))
present = datetime.datetime.now()
print(present-past)


M = 10
N = 10

def isSafe(matriz, visitados, x, y):
    if matriz[x][y] is 0 or visitados[x][y]:
        return False
    return True

def isValid(x, y):
    if x < M and y < N and x >= 0 and y >= 0:
        return True
    return False

def findLongestPath(matriz, visitados, i, j, x, y, max_dist, dist):
    if i is x and j is y:
        max_dist[0] = max(max_dist[0], dist)
        return
    visitados[i][j] = 1

    #abajo
    if isValid(i+1,j)and isSafe(matriz, visitados, i+1,j):
        findLongestPath(matriz, visitados, i+1, j, x,y, max_dist,dist+1)

    #derecha
    if isValid(i,j+1)and isSafe(matriz, visitados, i,j+1):
        findLongestPath(matriz, visitados, i, j+1, x,y, max_dist,dist+1)
    #arriba
    if isValid(i-1,j)and isSafe(matriz, visitados, i-1,j):
        findLongestPath(matriz, visitados, i-1, j, x,y, max_dist,dist+1)
    #izquierda
    if isValid(i,j-1)and isSafe(matriz, visitados, i,j-1):
        findLongestPath(matriz, visitados, i, j-1, x,y, max_dist,dist+1)
    #backtrack
    visitados[i][j] = 0;


matriz = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
           [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
           [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]];



visitados = [[0 for _ in range(M)] for _ in range(N)]

max_dist = [0]; #parapodermodificar la variable la paso como lista

findLongestPath(matriz, visitados, 0, 0, 5, 7, max_dist, 0);

print("Maximum length path is=> " + str(max_dist[0]))
