###
### UTN - TUPD 2025 - Programación 1 - TP Unidad 1 Estructuras Secuenciales
### Nicolás Corrado Armenti
###

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
#   Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
#   Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla
nombre = input("Ingrese su nombre")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
#   Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
#   Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = input("Ingrese su edad")
residencia = input("Ingrese su lugar de residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro
pi = 3.14159265359
radio = int(input("Ingrese el radio del círculo"))
area = pi * radio ** 2
perimetro = pi * radio * 2
print(f"El área del círculo es: {area} y su perímetro {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
segundos = int(input("Ingrese una cantidad de segundos"))
horas = segundos / 60 / 60
print(f"{segundos} segundos equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número
numero = int(input("Ingrese un número"))
print(f"{numero} x 1 = {numero}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
numero1 = int(input("Ingrese un número entero distinto de cero"))
numero2 = int(input("Ingrese otro número entero distinto de cero"))
print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
#   Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso / altura^2
altura = int(input("Ingrese su altura en cm"))
peso = float(input("Ingrese su peso en kg"))
imc = (peso) / (altura / 100)**2
print(f"Su IMC es {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
#   Tener en cuenta la siguiente equivalencia: F = 9/5 * C + 32
temp_c = float(input("Ingrese una temperatura en grados Celsius"))
temp_f = 9/5 * temp_c + 32
print(f"{temp_c}°C equivalen a {temp_f}°F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números
num1 = float("Ingrese el primer número")
num2 = float("Ingrese el segundo número")
num3 = float("Ingrese el tercer número")
prom = (num1 + num2 + num3) / 3
print(f"El promedio de los 3 números es: {prom}")