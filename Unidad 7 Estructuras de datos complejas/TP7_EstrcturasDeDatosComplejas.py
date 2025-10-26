#Ejercicio 1: Dado el diccionario precios_frutas, añadir las siguientes frutas con sus respectivos precios:
#Naranja = 1200 Manzana = 1500 Pera = 2300

#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#precios_frutas['Naranja'] = 1200
#precios_frutas['Manzana'] = 1500
#precios_frutas['Pera'] = 2300

#print(precios_frutas)


#Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330 Manzana = 1700 Melón = 2800

#precios_frutas['Banana'] = 1330
#precios_frutas['Manzana'] = 1700
#precios_frutas['Melón'] = 2800

#print(precios_frutas)


#Ejercicio 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

#lista_frutas = []

#for fruta in precios_frutas:
#    lista_frutas.append(fruta)


#Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos.
#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#Luego, pedí un nombre y mostrale el número asociado, si existe.

#contactos = {}

#for contacto in range(5):
#    contacto = input("Escriba el nombre del contacto ").lower()
#    contactos[contacto] = input("Escriba el número del contacto ")


#print(contactos[input("Escriba el nombre del contacto que desea consultar su número ").lower()])


#Ejercicio 5: Solicita al usuario una frase e imprime:
#Las palabras únicas (usando un set) y Un diccionario con la cantidad de veces que aparece cada palabra.

#frase = input("Escriba una frase: ").lower()

#palabras = frase.split( )

#palabras_unicas = set(palabras)

#recuento = {}

#for palabra in palabras:
#    recuento[palabra] = palabras.count(palabra)

#print(recuento)


#Ejercicio 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

#alumnos = {}

#for alumno in range(1):
#    alumno = input("Escribe el nombre del alumno ").lower()
#    alumnos[alumno] = tuple(float(input(f"Escribe la nota {i + 1} del alumno {alumno}" )) for i in range(3)) 

#for alumno in alumnos:
#    print(f"El promedio de {alumno} es {sum(alumnos[alumno]) / len(alumnos[alumno])}")


#Ejercicio 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

parcial_1 = {1,2,3,4,5}
parcial_2 = {1,2,6,7,8,9}

print(f"Ambos parciales: {parcial_1 & parcial_2}")
print(f"Solo uno: {parcial_1 ^ parcial_2 }")
print(f"Al menos uno: {parcial_1 | parcial_2}")