

def Ackerman(m, n):
    if m is 0:
        return n+1
    if m > 0:
        if n is 0:
            return Ackerman(m-1, 1)
        if n > 0:
            return Ackerman(m-1, Ackerman(m, n-1))


print(Ackerman(3, 3))
print("Algoritmo de Ackerman, Dos valores enteros m y n:")
m = input("Ingrese el valor de m: ")
n = input("Ingrese el valor de n: ")
print("Respuesta: " + str(Ackerman(int(m),int(n))))