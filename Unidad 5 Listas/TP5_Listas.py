#Ejercicio 1: Crea una lista con las notas de 10 estudiantes:
# Mostrar la lista completa, calcular y mostrar el promedio, 
# indicar la nota más alta y la mas baja

notas = [6.4,9,2.8,3.6,10,4.8,5.1,6.9,7.8,8.4]
print(f"Las notas de los alumnos son:")
suma = 0

for nota in notas:
    suma = suma + nota
    print(nota)

for indice_pasada in range(len(notas) - 1):
    for indice_actual in range(len(notas)- 1 - indice_pasada):
        if notas[indice_actual] > notas[indice_actual + 1]:
            notas[indice_actual], notas[indice_actual + 1] = notas[indice_actual + 1], notas[indice_actual]

print(f"El promedio de las notas de todo el curso fue {suma / len(notas)}")
print(f"La nota mas alta fue {notas[-1]} y la mas baja fue {notas[0]}")



#Ejercicio 2: Pedir al usuario que cargue 5 productos en una lista
# Mostrar la lista ordenada alfabeticamente (usando .sorted())
# Preguntar al usuario que producto desea eliminar y actualizar la lista

lista_compras = []

while len(lista_compras) < 5:
    lista_compras.append(input("Ingrese un producto "))

print(f"Su lista de compras ordenada:")
for producto in sorted(lista_compras):
    print(producto)

producto_removido = input("¿Desea remover un producto de la lista? Si es asi, escríbalo: ")

if producto_removido in lista_compras:
    lista_compras.remove(producto_removido)
    print(f"Su lista de compras final: ")
    for producto in sorted(lista_compras):
        print(producto)
else:
    print(f"No se han hecho cambios en su lista: ")
    for producto in sorted(lista_compras):
        print(producto)



#Ejercicio 3: Generar una lista con 15 números al azar entre 1 y 100
# - Crear una lista con los pares y otra con los impares
# - Mostrar cuántos números tiene cada lista

import random

lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(15):
    lista_numeros.append(random.randint(1,100))

print("Los números generados son los siguientes: ")

for numero in lista_numeros:
    print(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f"De los cuales {len(lista_pares)} son pares y {len(lista_impares)} son impares")



# Ejercicio 4: Dada una lista con valores repetidos
# - Crear una nueva lista sin elementos repetidos
# - Mostrar el resultado

lista_repetidos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_repetidos = []

for numero in lista_repetidos:
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

for numero in lista_sin_repetidos:
    print(numero)



# Ejercicio 5: Crear una lista con los nombres de 8 estudiantes presentes en clase
# - Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente
# - Mostrar la lista final actualizada

lista_nombres = ["Javi", "Dina", "Gonza", "Ari", "Jere", "Rocío", "Hernán", "Luis"]
print("Lista de alumnos")
for nombre in lista_nombres:
    print(nombre)

eleccion = str(input("Por favor, escriba A si desea agrega un alumno o R si desea removerlo de la lista: ")).lower()

if eleccion == "a":
    lista_nombres.append(input("Por favor, escriba el nombre del alumno que desea agregar: "))
elif eleccion == "r":
    lista_nombres.remove(input("Por favor, escriba el nombre del alumno que desea remover: "))
else:
    print("Valor incorrecto")

print("Lista actualizada")
for nombre in lista_nombres:
    print(nombre)



# Ejercicio 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# (el último pasa a ser el primero)

lista_num = [1, 2, 3, 4, 5, 6, 7]

lista_rotada = [lista_num[-1]] + lista_num[:-1]

print(lista_rotada)



# Ejercicio 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas
# mínimas y máximas de la semana
# - Calcular el promedio de las mínimas y el de las máximas
# - Mostrar en que día se registró la mayor amplitud térmica


temperaturas = [
  [17, 12],
  [21, 15],
  [17, 11],
  [20, 13],
  [21, 15],
  [21, 13],
  [18, 14]
]

dias_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

suma_maximas = 0
suma_minimas = 0
amplitud_termica = 0
amplitud_termica_max = 0
dia_mayor_amplitud = ""

for dia in temperaturas:
    suma_maximas = suma_maximas + dia[0]
    suma_minimas = suma_minimas + dia[1]
    amplitud_termica = dia[0] - dia[1]
    if amplitud_termica > amplitud_termica_max:
        amplitud_termica_max = amplitud_termica
        dia_mayor_amplitud = temperaturas.index(dia)

print(f"El promedio de las temperaturas máximas en la semana fue {suma_maximas / len(temperaturas)}")
print(f"El promedio de temperaturas mínimas en la semana fue: {suma_minimas / len(temperaturas)}")
print(f"El día con mayor amplitud térmica fue: {dias_semana[dia_mayor_amplitud]} con {amplitud_termica_max}°C de amplitud térmica")



#Ejercicio 8: crear una matriz con las notas de 5 estudiantes en 3 materias
# - Mostrar el promedio de cada estudiante
# - Mostrar el promedio de cada materia

estudiantes = ["Juan","Javi","Jose","Jorge","Julian"]
notas_estudiantes = [
    [4,3,10], # Matemática - Lengua - Cs Sociales
    [6,7,8],     
    [6,5,7], 
    [10,2,10], 
    [7,3,8] 
    ]

suma_matematica = 0
suma_lengua = 0
suma_sociales = 0

for notas in notas_estudiantes:
    promedio_estudiante = (notas[0] + notas[1] + notas[2]) / len(notas)
    suma_matematica = suma_matematica + notas[0]
    suma_lengua = suma_lengua + notas[1]
    suma_sociales = suma_sociales + notas[2]
    print(f"El promedio de {estudiantes[notas_estudiantes.index(notas)]} fue: {promedio_estudiante}")


print(f"El promedio de los alumnos en matemática fue: {suma_matematica / len(notas_estudiantes)}")
print(f"El promedio de los alumnos en lengua fue: {suma_lengua / len(notas_estudiantes)}")
print(f"El promedio de los alumnos en cs sociales fue: {suma_sociales / len(notas_estudiantes)}")



# Ejercicio 9: Representar un tablero de Ta-Te-Ti como una lista de listas 3x3
# - Inicializarlo con guiones "-" representando casillas vacías
# - Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O"
# - Mostrar el tablero después de cada jugada

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

cantidad_filas = len(tablero)
cantidad_columnas = len(tablero[0])

print("Tablero de ta-te-ti: ")
for fila in range(cantidad_filas):
    for columna in range(cantidad_columnas):
        print(tablero[fila][columna], end=' ')
    print(" ")

terminar = False

while not terminar:
    input_usuarios_fila = int(input("Elija la fila en la que desea escribir su símbolo: ")) - 1
    input_usuarios_columna = int(input("Elija la columna en la que desea dibujar su símbolo: ")) - 1 
    input_símbolo = str(input("Que símbolo quiere colocar?, X o O: ")).upper()
    if input_símbolo == "O" or input_símbolo == "X":
        tablero[input_usuarios_fila][input_usuarios_columna] = input_símbolo
        for fila in range(cantidad_filas):
            for columna in range(cantidad_columnas):
                print(tablero[fila][columna], end=' ')
            print(" ")
        if input("Si desea terminar el juego, coloque T, si desea continuar presione enter").upper() == "T":
            break
    


#Ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7
# - Mostrar el total vendido por cada producto
# - Mostrar el día con mayores ventas totales
# - Indicar cual fue el producto más vendido de la semana


ventas = [
    [10, 12, 15, 11, 9, 10, 14],   # Producto 1
    [5, 8, 6, 9, 10, 7, 11],       # Producto 2
    [20, 18, 19, 22, 25, 21, 23],  # Producto 3
    [7, 9, 8, 6, 10, 11, 12]       # Producto 4
]

productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

mayor_total = 0

for producto in ventas:
    total_vendido = 0
    for unidades in producto:
        total_vendido = total_vendido + unidades
    print(f"El total de unidades vendidas de {productos[ventas.index(producto)]} es {total_vendido}")
    indice = ventas.index(producto)
    if total_vendido > mayor_total:
        mayor_total = total_vendido
        producto_mas_vendido = productos[indice]
    print(f"El producto más vendido de la semana fue {producto_mas_vendido} con {mayor_total} unidades.")

mayor_total_dia = 0

for dia in range(len(dias)):
    total_dia = 0
    for producto in range(len(ventas)):
        total_dia = total_dia + ventas[producto][dia]
    print(f"El total vendido el {dias[dia]} es {total_dia}")
    if total_dia > mayor_total_dia:
        mayor_total_dia = total_dia
        indice_mayor_dia = dia    
print(f"El día con mayores ventas fue {dias[indice_mayor_dia]} con {mayor_total_dia} unidades.")