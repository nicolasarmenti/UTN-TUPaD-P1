###
### UTN - TUPD 2025 - Programación 1 - TP Unidad 6 Recursividad
### Nicolás Corrado Armenti (Mat: 101035)
###

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

factoriales = int(input("Ingrese un número: "))
for i in range(1, factoriales + 1):
    print(f"El factorial de {i} es {factorial(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
fibonacci_hasta = int(input("Ingrese un número: "))
for i in range(1, fibonacci_hasta + 1):
    print(fibonacci(i), end=" ")
print("")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.
def potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)
    
base_prueba = 5
exponente_prueba = 6
print(f"{base_prueba} elevado a la {exponente_prueba} es {potencia(base_prueba, exponente_prueba)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2.
def dec2bin(num):
    if num < 2:
        return str(num)
    else:
        return dec2bin(num // 2) + str(num % 2)
print(f"10 en binario es {dec2bin(10)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
#   La solución debe ser recursiva.
#   No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return (palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1]))
    
palabra_prueba = input("Ingrese una palabra: ")
print(f"La palabra es un palíndromo: {es_palindromo(palabra_prueba)}")

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#   No se puede convertir el número a string.
#   Usá operaciones matemáticas (%, //) y recursión.
def suma_digitos(n):
    if n // 10 == 0:
        return n % 10
    else:
        return n % 10 + suma_digitos(n // 10)
    
print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero // 10 == 0:
        if (numero % 10) == digito:
            return 1
        else:
            return 0
    else:
        return contar_digito(numero % 10, digito) + contar_digito(numero // 10, digito)
    
print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))