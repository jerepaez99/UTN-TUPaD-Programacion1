#Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
#en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


#Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

contador_de_digitos = 0
numero_entero = int(input("Por favor, escribe un número entero del cual desea saber la cantidad de dígitos que contiene: "))
while (numero_entero >= 1):
    numero_entero = numero_entero / 10
    contador_de_digitos += 1
print(contador_de_digitos)


#Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("Este programa suma todos los números enteros comprendidos entre dos valores")
numero_1 = int(input("Por favor, ingrese el primer número entero: "))
numero_2 = int(input("Por favor, ingrese el primer número entero: "))

##Vamos a ordenar los números primero
if numero_2 < numero_1:
    temporal = numero_2
    numero_2 = numero_1
    numero_1 = temporal

##Ahora, para excluir el extremo inicial vamos a sumarle 1
inicio = numero_1 + 1
suma_3 = 0

while inicio < numero_2:
    suma_3 = suma_3 + inicio
    inicio = inicio + 1

print(suma_3)


#Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

print("Sumador de números enteros")
numero_ingresado = float("inf")
suma = 0
while numero_ingresado != 0:
    numero_ingresado = int(input("Ingrese un número entero, escriba 0 si desea ver el resultado de la suma: "))
    suma = suma + numero_ingresado
print("El resultado de la suma es",suma)


#Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("Adivine un número aleatorio del 0 al 9")
import random
adivinalo = int(random.randint(0,9))
numero_usuario = int(input("Escriba su número: "))
intentos = 1

if numero_usuario <= 0 or numero_usuario >= 9:
    print("Por favor, intruduzca un número válido")
else:
    while numero_usuario != adivinalo:
        numero_usuario = int(input("No pudo adivinar, por favor otro número: "))
        intentos +=1

print("Felicidades! Solo te llevó",intentos,"intentos adivinar el número")



#Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente

print("Este programa imprime en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente")
for i in range(100,0,-2):
    print(i)



#Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

print("Este programa calcula la suma de todos los números comprendidos entre 0 y un numero entero positivo ingresado por el usuario")
numero_entero_positivo = int(input("Ingrese un número entero positivo: "))
suma = 0

if numero_entero_positivo > 0:
#Si se desea incluir el extremo se le suma 1 al rango
    for i in range(numero_entero_positivo + 1):
        suma = suma + i
    print("La suma de todos los numeros enteros positivos entre 0 y",numero_entero_positivo,"es",suma)        
else:
    print("Ingrese un número válido")



#Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

max_numeros = 5
print("Este progrma indica cuantos de los",max_numeros,"números ingresados son pares, cuantos impares, cuantos negativos y cuantos positivos")
negativos = 0
positivos = 0
impares = 0
pares = 0

for i in range(max_numeros):
    input_usuario = int(input("Por favor, ingrese un número entero: "))
    if input_usuario < 0:
        negativos += 1
    else:
        positivos += 1
    
    if input_usuario % 2 == 0:
        pares += 1
    else:
        impares += 1

print("La cantidad de números pares ingresada fue:",pares,"Y la cantidad de números impares ingresada fue:",impares)
print("La cantidad de números positivos ingresada fue:",positivos,"Y la cantidad de números negativos ingresada fue:",negativos)



#Ejercicio 9: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

max_numeros_media = 5
print("Este programa indica la media entre",max_numeros_media,"numeros ingresados por el usuario")
suma_media = 0

for i in range(max_numeros_media):
    numero_usuario = int(input("Por favor, ingrese un número entero: "))
    suma_media = suma_media + numero_usuario

print("La media de los valores ingresados es",suma_media/max_numeros_media)



#Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Voy a utilizar una fórmula parecida a la que utilizamos en el curso de preingreso, requiere la posibilidad de extraer el valor truncado de un número
#por lo que voy a importar el módulo math
numero_usuario_invertir = int(input("Ingrese un número el cual desea invertir sus dígitos: "))
inverso = ""
import math

while numero_usuario_invertir > 0:
    digito = numero_usuario_invertir % 10 
    inverso = inverso + str(digito)
    numero_usuario_invertir = math.trunc(numero_usuario_invertir/10)

print(inverso)
