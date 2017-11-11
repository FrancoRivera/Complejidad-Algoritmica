import random


print("\nPregunta 2:\n")


def potencia(base, exponente):
    if exponente is 1: # si el exponente es 1 (caso base)
        return base
    return base*potencia(base,exponente-1)

# 2 a la 10 = 1024
print(potencia(2, 10))

# Pregunta 3

print("\nPregunta 3: \n")

sucesion = list()

for i in range(0, random.randint(10, 100)):
    sucesion.append(random.randint(0, 100))


sucesion = [10, 12, -5, 17, 38, -6, 7, 9]

## con BT

print("\nCon BT  \t O(n)\n")

lista_aux = list()

max = 0
def sumar(sucesion, posicion, suma, suma_max):
    if posicion >= len(sucesion): ##se acabo la lista
        print ("Maxima suma secuencial: " + str(suma_max))
        return
    if sucesion[posicion] < 0:
        if suma > suma_max:
            suma_max = suma
            suma = 0
    else:
        suma += sucesion[posicion]
    return sumar(sucesion, posicion+1, suma, suma_max)

sumar(sucesion, 0, 0, 0)


## con FB

print("\nCon FB  \t O(n)\n")

lista_mayor = list()
lista_aux = list()
max = 0
nuevo_max = 0
for i in sucesion:
    if i < 0:
        if nuevo_max > max:
            max = nuevo_max
            nuevo_max = 0
            lista_mayor = lista_aux
            lista_aux = list()
            continue
    nuevo_max += i
    lista_aux.append(i)

#print (lista_mayor) imprime lista secuencial que producen el maximo
print("Maxima suma secuencial: " + str(max))
