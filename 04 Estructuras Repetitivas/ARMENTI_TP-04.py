###
### UTN - TUPD 2025 - Programación 1 - TP Unidad 4 Estructuras Repetitivas
### Nicolás Corrado Armenti (Mat: 101035)
###

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
entero = int(input("Ingrese un número entero"))
digitos = 0
while entero % (10**digitos) != entero:
    digitos += 1
print(f"El número {entero} tiene {digitos} digito(s)")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
cotaInferior = int(input("Ingrese la cota inferior"))
cotaSuperior = int(input("Ingrese la cota superior"))
sumatoria = 0

for i in range(cotaInferior + 1, cotaSuperior):
    sumatoria += i

print(f"La suma de los números enteros entre {cotaInferior} y {cotaSuperior} (sin incluirlos) es: {sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = int(input("Ingrese un número a sumar (0 para salir)"))
sumatoria = 0
while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese un número a sumar (0 para salir)"))

print(f"La suma de los números ingresados es: {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
from random import randint
valor = randint(0, 9)
print("Adivine el número aleatorio")
intento = int(input("Ingrese un intento"))
intentos = 1
while intento != valor:
    print("No adivinó")
    intentos += 1
    intento = int(input("Ingrese un intento"))

print(f"Adivinó correctamente en {intentos} intento(s)")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, 0, -2):
    print(i)
    
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
cotaSuperior = int(input("Ingrese la cota superior"))
sumatoria = 0

for i in range(0, cotaSuperior):
    sumatoria += i

print(f"La suma de los números enteros entre 0 y {cotaSuperior} es {sumatoria}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
n = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(n):
    numero = int(input("Ingrese un número"))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("De los números ingresados:")
print(f"{pares} son pares")
print(f"{impares} son impares")
print(f"{positivos} son positivos")
print(f"{negativos} son negativos")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
n = 100
sumatoria = 0

for i in range(n):
    sumatoria += int(input("Ingrese un valor"))

print(f"La media de los valores ingresados es {sumatoria / n}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un número"))
invertido = 0

while numero > 0:
    invertido = invertido * 10
    temp = numero % 10
    numero = numero // 10
    invertido += temp

print(invertido)