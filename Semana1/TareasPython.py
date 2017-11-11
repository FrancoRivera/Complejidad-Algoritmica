
import math
#Calcule la complejidad para los algoritmos siguientes:

print("Tarea semana 1: \n======================\nA.A.: Tiempo asintotico \n\n")

#1.	Busca el mayor valor en un arreglo de tamaño n.
arreglo = [0,13,23,2,3,5,10,2]
mayor = 0
for i in range(0, len(arreglo)):
    if mayor <= arreglo[i]:
        mayor = arreglo[i]
print("1. El mayor elemento del arreglo " + str(arreglo) + " es: "+  str(mayor) + "\t A.A.: O(n)\n")

#2.	Calcula el factorial de un entero n utilizando un algoritmo lineal (secuencial).

numero = 10
factorial = 1
for i in range(numero, 1, -1):
    factorial *= i
print("2. El factorial de " + str(numero)  + " es " + str(factorial)+ "\t A.A.: O(n)\n")


#3.	Calcula la factorial de un entero n, utilizando una función recursiva.

def factorial(numero):
    if numero == 1:
        return 1
    return numero * factorial(numero-1)


print("3. El factorial (recursivo) de " + str(numero)  + " es " + str(factorial(numero))+ "\t A.A.: O(n)\n")

#4.	Calcula la serie de Fibonacci.

arreglo = list()

for i in range(0, 10):
    if i == 0:
        arreglo.append(1)
    elif i == 1:
        arreglo.append(1)
    else:
        arreglo.append(arreglo[i-2]+arreglo[i-1])

print("4. Fibonacci a 10 posiciones: " + str(arreglo) + "\t A.A.: O(n)\n")
# 5.	Dado un vector A de n números, calcular otro vector B, tal que, a
#  partir de una secuencia de números A, calculamos otra tal que cada
# uno de sus elementos es el promedio de todos los anteriores en A.

A = [10, 12,23,1,2,12,3,2]
B= list()
for i in range(0, len(A)):
    suma = 0
    for j in range(0, i+1):
        suma += A[j]
    avg = suma/(i+1)
    B.append(avg)

print("5. Arreglo original: A" + str(A) + ", nuevo arreglo B"+ str(B)+"\t A.A.: O(n^2)\n")


# 6.	Calcula la mediana de un conjunto ordenado es un elemento tal que
#  el número de elementos menores que la mediana difiere en cuando más
#  1 del número de elementos que son mayores, suponiendo que no hay empates.
#  El algoritmo halla la mediana de tres enteros distintos: a, b y c.

A = [1,2,3,4,5,6,7,8,9]

mediana = int(len(A)/2)

print("6: Mediana de elementos A" + str(A) + " es " +str(A[mediana])+"\t A.A.: O(1)\n")


# 7.	Halla el segundo elemento más grande de un conjunto que contiene n elementos.
# Asuma que los datos no están ordenados.

A = [10, 12,23,1,10,12,3,2]
max = 0
max2 = 0
for i in range(0, len(A)):
    if max < A[i]:
        max = A[i]
    elif max2 < A[i]:
        max2 = A[i]

print("7: Del arreglo: " + str(A) + " el maximo es: " + str(max) + " y el segundo maximo es: " + str(max2)+"\t A.A.: O(n)\n")


#8.	Halla el más pequeño y el más grande, de un conjunto de n elementos.


A = [10, 12,23,1,10,12,3,2]
max = 0
min = 99999999999
for i in range(0, len(A)):
    if max < A[i]:
        max = A[i]
    if min > A[i]:
        min = A[i]

print("8: Del arreglo: " + str(A) +  "el maximo es: " + str(max) + " y el minimo es: " + str(min)+"\t A.A.: O(n)\n")



print("================================:\n\n")
print("\tDel PPT \n\n")

#Encontrar el numero mayor en un arreglo de enteros

arreglo = [0,13,23,2,3,5,10,2]
mayor = 0
for i in range(0, len(arreglo)):
    if mayor <= arreglo[i]:
        mayor = arreglo[i]
print("El mayor elemento del arreglo " + str(arreglo) + " es: "+  str(mayor) + "\t A.A.: O(n)\n")


#Ordenar un arreglo de numeros enteros


arreglo = [0,13,23,2,3,5,10,2]
arreglo2 = arreglo
for i in range(0, len(arreglo)):
    for j in range(0, len(arreglo)):
        pass


print("Arreglo original: " + str(arreglo) + " arreglo ordenado (bubble sort): "+  str(arreglo2) + "\t A.A.: O(n^2)\n")


#Eliminar el elemento en una posicion de un arreglo

arreglo = [0,13,23,2,3,5,10,2]
numero = 23
arreglo2 = list()

for i in range(0, len(arreglo)):
    if arreglo[i] == numero:
        break
    arreglo2.append(arreglo[i])

print("Arreglo original: " + str(arreglo) + " arreglo sin el elemento "+ str(numero) +": "+  str(arreglo2) + "\t A.A.: O(n^2)\n")


#Buscar un numero en un arreglo

arreglo = [0,13,23,2,3,5,10,2]
existe = False
numero = 10
posicion = 0
for i in range(0, len(arreglo)):
    if arreglo[i] == numero:
        posicion = i
        existe = True
        break

print("El numero " + str(numero) + ((" esta en la posicion  "+ str(posicion+1) ) if existe else " no esta") + " en el arreglo "+ str(arreglo) +"\t A.A.: O(n)\n")


#Calcular el factorial de N

numero = 50
factorial = 1
for i in range(numero, 1, -1):
    factorial *= i
print("El factorial de " + str(numero)  + " es " + str(factorial)+ "\t A.A.: O(n)\n")


# Determinar si un numero existe en un arreglo de enteros.

arreglo = [0,13,23,2,3,5,10,2]
existe = False
numero = 10
for i in range(0, len(arreglo)):
    if arreglo[i] == numero:
        existe = True
        break

print("El numero " + str(numero) + (" si esta " if existe else " no esta ") + "en el arreglo "+ str(arreglo) +"\t A.A.: O(n)\n")


#Calcular cuantas veces se repite un numero X en un arreglo de enteros.

arreglo = [0,13,23,2,3,5,10,2]
numero = 2
existe = False
veces = 0
for i in range(0, len(arreglo)):
    if arreglo[i] == numero:
        existe = True
        veces +=1


print("El numero " + str(numero) + ((" esta " + str(veces) +" veces ") if existe else " no esta ") + "en el arreglo "+ str(arreglo) +"\t A.A.: O(n)\n")


#Sumar los digitos de un numero entero positivo.

numero = 434123123
suma = 0

for i in range(0, len(str(numero))):
    suma += int(str(numero)[i])

print("La suma de las cifras del numero " + str(numero) + " es: "+ str(suma)+ "\t A.A.: O(n)\n")

#Determinar si un numero es primo o no.

primo = True
numero = 393342743


for i in range(2, int(math.sqrt(numero))+1):
    if numero % i == 0:
        primo = False
        break
print ("El numero " + str(numero) + (" es primo" if primo else " no es primo")+ "\t A.A.: O(sqrt(n))\n")

#Determinar la cantidad de primos que existen en un arreglo de enteros.

arreglo = [19,13,23,2,3,5,10,2]
primos = list()

for j in range(0, len(arreglo)):
    numero = arreglo[j]
    primo = True
    for i in range(2, int(math.sqrt(numero)+1)):
        if numero % i== 0:
            primo = False
    if primo:
        primos.append(arreglo[j])

print ("Los primos del arreglo " + str(arreglo) + " son " + str(primos)+ "\t A.A.: O(n^2)\n")
