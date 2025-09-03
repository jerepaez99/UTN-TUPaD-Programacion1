#Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edadDelUsuario = int(input("Por favor, coloque su edad: "))
print(edadDelUsuario)
if edadDelUsuario >= 18: 
    print("Es mayor de edad")



#Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
#deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
#en caso contrario deberá mostrar el mensaje “Desaprobado”.

notaDelUsuario = int(input("Por favor, escriba la nota: "))
if notaDelUsuario >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")



#Ejercicio 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
#imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla
#"Por favor, ingrese un número par". 
#Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numeroDelUsuario = int(input("Por favor, ingrese un número: "))
if numeroDelUsuario % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")



#Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla 
#a cuál de las siguientes categorías pertenece:

edadDelUsuarioDos = int(input("Por favor, ingrese su edad: "))
if edadDelUsuarioDos < 12:
    print("Usted pertenece a la categoría 'Niño/a'")
elif edadDelUsuarioDos >= 12 and edadDelUsuarioDos < 18:
    print("Usted pertenece a la categoría 'Adolescente'")
elif edadDelUsuarioDos >= 18 and edadDelUsuarioDos < 30:
    print("Usted pertenece a la categoría 'Adulto/a Joven'")
else:
    print("Usted pertenece a la categoría 'Adulto/a'")



#Ejercicio 5: Escribir un programa que permita introducir contrasenas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
#Nota: investigue el uso de la funcion len() en Python para evaluar la cantidad de elementos que tiene
#un iterable tal como una lista o un string.

contrasenia = input("Por favor, ingrese una contraseña: ")
if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#Ejercicio 6: escribir un programa que tome la lista numeros_aleatorios, 
#calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
#negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
print(numeros_aleatorios)
if (mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Sesgo positivo")
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo Negativo")
else:
    print("No hay sesgo")



#Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, anadir un signo de exclamacion al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingreso el usuario e imprimirlo por
#pantalla.

vocales = "aeiouAEIOU"
palabra = input("Por favor, ingrese una palabra: ")
ultimaLetra = palabra[-1]
if ultimaLetra in vocales:
    print(f"{palabra}!")
else:
    print(palabra)



#Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de lo que desee

nombreDelUsuario = input("Por favor, ingrese su nombre: ")
numero = int(input("Si desea ver su nombre en mayúsculas, ingrese 1; si desea ver su nombre en minúsculas, ingrese 2; si desea ver su nombre con la primer letra mayúscula, ingrese 3: "))
if numero == 1:
    print(nombreDelUsuario.upper())
elif numero == 2:
    print(nombreDelUsuario.lower())
elif numero == 3:
    print(nombreDelUsuario.title())



#Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorias segun la escala de Richter e imprima el resultado
#por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto = float(input("Escriba la magnitud del terremoto en la escala de ritcher: "))
if terremoto <3:
    print("Muy leve (imperceptible)")
elif terremoto >= 3 and terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif terremoto >= 6 and terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")



#Ejercicio 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y que día es. El programa debera utilizar esa informacion para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

#los meses están ordenados en conjuntos, primero están los que tienen 31 dias, luego los que tienen 30 y por ultimo febrero,
#esto lo hice así para que sea mas sencillo validar el día que ingresó el usuario
meses = "enero","marzo","mayo","julio","agosto","octubre","diciembre","abril","junio","septiembre","noviembre","febrero"
mes = input("Ingrese el mes en el que se encuentra: ").lower()

if mes in meses:
    dia = int(input("Ingrese en que día del mes se encuentra: "))
    validadorDeDia = False

    if meses.index(mes) >= 0 and meses.index(mes) <= 6:
        if dia <= 31 and dia > 0:
            validadorDeDia = True
    elif meses.index(mes) > 6 and meses.index(mes) <= 10:
        if dia <= 30 and dia > 0:
            validadorDeDia = True
    elif meses.index(mes) == 11:
        if dia <= 29 and dia > 0:
            validadorDeDia = True

    if validadorDeDia:

        hemisferio = input("ingrese el hemisferio en el que se encuentra (S/N): ").upper()
        if hemisferio == "S" or hemisferio == "N":

            if hemisferio == "S":
                if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
                    print("Usted se encuentra en Verano")
                elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
                    print("Usted se encuentra en Otoño")
                elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
                    print("Usted se encuentra en Invierno")
                elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
                    print("Usted se encuentra en Primavera")

            if hemisferio == "N":
                if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
                    print("Usted se encuentra en Invierno")
                elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
                    print("Usted se encuentra en Primavera")
                elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
                    print("Usted se encuentra en Verano")
                elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
                    print("Usted se encuentra en Otoño")
        else:
            print("Por favor, coloque un hemisferio correcto")              
    else:
        print("Por favor, coloque un día correcto")
else:
    print("por favor, coloque un mes correcto")