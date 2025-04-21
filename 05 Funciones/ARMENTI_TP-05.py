###
### UTN - TUPD 2025 - Programación 1 - TP Unidad 4 Estructuras Repetitivas
### Nicolás Corrado Armenti (Mat: 101035)
###

import math

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Nico")

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal("Nicolás", "Armenti", 33, "CABA")

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return math.pi * radio * 2

radio = float(input("Ingrese el radio del círculo"))
print(f"El área es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / (60 * 60)

segundos = int(input("Ingrese una cantidad de segundos"))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.
# Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")

numero = int(input("Ingrese un número"))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

numero1 = int(input("Ingrese un número"))
numero2 = int(input("Ingrese otro número"))
resultados = operaciones_basicas(numero1, numero2)
print(f"La suma de ambos es {resultados[0]}")
print(f"La resta de ambos es {resultados[1]}")
print(f"La multiplicación de ambos es {resultados[2]}")
print(f"La división de ambos es {resultados[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / altura ** 2

peso = float(input("Ingrese su peso"))
altura = float(input("Ingerse su altura"))
print(f"Su IMC es {calcular_imc(peso, altura):.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

temperaturaC = float(input("Ingrese la temperatura en grados Celsius"))
print(f"La temperatura en grados Fahrenheit es {celsius_a_fahrenheit(temperaturaC)}")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

numero1 = int(input("Ingrese un número"))
numero2 = int(input("Ingrese otro número"))
numero3 = int(input("Ingrese otro número"))
print(f"El promedio de los 3 números es {calcular_promedio(numero1, numero2, numero3)}")