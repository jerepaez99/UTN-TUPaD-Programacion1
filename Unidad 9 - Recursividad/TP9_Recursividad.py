#Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los 
#números enteros entre 1 y el número que indique el usuario

input_usuario = int(input("Escriba un número: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def factoriales(n):
    if n == 0:
        return 1
    else: 
        print(factorial(n))
        factoriales(n - 1)

print(factorial(input_usuario))

factoriales(input_usuario)


#Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci 
#en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que 
#el usuario especifique.

input_usuario_fibonacci = int(input("Escriba un número: "))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)

def fibonaccis(n):
    if n >= 0:
        print(fibonacci(n))
        fibonaccis(n - 1)

print(fibonacci(input_usuario_fibonacci))

fibonaccis(input_usuario_fibonacci)


#Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese un exponente: "))
resultado_potencia = potencia(base, exponente)

print(f"{base} elevado a la {exponente} es igual a: {resultado_potencia}")


#Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo
# en base decimal y devuelva su representación en binario como una cadena de texto.

decimal = int(input("Ingrese un número: "))

def decimalBinario(n):
    if n < 2:
        return n
    else:
        return str(decimalBinario(n // 2)) + str(n % 2)
    
print(decimalBinario(decimal))


#Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra)
#que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es
#un palíndromo o False si no lo es.
#- La solución debe ser recursiva
#- No se debe usar [::-1] ni la función reversed()

palabra = input("Escriba una palabra o frase sin tildes para checkear si es palíndroma: ")

def es_palindromo(palabra):
    palabra = palabra.strip()
    if len(palabra) <= 1:
        return True    
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:len(palabra)-1])    
        
print(es_palindromo(palabra))


#Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n)
# que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

numero_positivo = int(input("Escriba un número entero positivo: "))

def sumaDigitos(n):
    if n <= 10:
        return n
    else:
        return n % 10 + sumaDigitos(n // 10)
    
print(sumaDigitos(numero_positivo))


#Ejercicio 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo
#coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta
#llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

bloques = int(input("Escriba la cantidad de bloques: "))

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
    
print(contar_bloques(bloques))


#Ejercicio 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba
#un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece
#ese dígito dentro del número.

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar: "))

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo = numero % 10
    resto = numero // 10

    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
    
print(contar_digito(numero, digito))
    



    