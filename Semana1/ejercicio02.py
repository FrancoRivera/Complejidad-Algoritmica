from datetime import datetime
import math

def CalcularAreaCirculo():
	radio = float(0.0)
	PI = float(3.14159)

	print("Ingrese el radio del circulo")
	radio = input()

	area = radio * radio * PI

	print("El area del circulo es: " + str(area))


startTime = datetime.now()


"""
CalcularAreaCirculo()
print("tardaste: " + str(datetime.now()-startTime))
"""

def EsCapicua():
	numero = int(161)
	centena = decena = unidad = int(0)
	centena = math.trunc(numero/100)
	decena = (numero%100)/10
	unidad = (numero%100)%10

	if centena == unidad:
		print("El numero es capicua")
	else:
		print("El numero NO es capicua")


