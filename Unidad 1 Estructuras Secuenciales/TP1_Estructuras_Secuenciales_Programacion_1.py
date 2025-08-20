#Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”
nombreDelUsuario = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombreDelUsuario}!")

#Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugarDeResidencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}")

#Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input(f"Coloque el radio: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del círculo con radio {radio} es: {area}. El perímetro del círculo con radio {radio} es {perimetro}")

#Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número del que desea ver su tabla de multiplicar: "))
for multiplicador in range(11):
    producto = numero * multiplicador
    print (f"{numero} x {multiplicador} = {producto}")

#Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y
# muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

numeroUno = int(input("Por favor, escribe el primer número entero mayor a 0: "))
numeroDos= int(input("Por favor, escribe el segundo número entero mayor a 0: "))
print(f"Suma: {numeroUno} + {numeroDos} = {numeroUno + numeroDos}")
print(f"División: {numeroUno} / {numeroDos} = {numeroUno / numeroDos}")
print(f"Multiplicación: {numeroUno} x {numeroDos} = {numeroUno * numeroDos}")
print(f"Resta: {numeroUno} - {numeroDos} = {numeroUno - numeroDos}")

#Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal

altura = float(input("Por favor, escribe tu estarura, expresada en metros: "))
peso = float(input("Por favor, escribe tu peso expresado en kg: "))
print(f"Su índice de masa corporal es {int(peso / (altura * altura))}")

#Ejercicio 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit

celsius = float(input("Por favor, ingrese la temperatura en celsius: "))
farenheit = ((9/5) * celsius) + 32
print(f"{celsius} grados celsius equivalen a {farenheit} grados farenheit")

#Ejercicio 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numUno = int(input("Por favor, escribe el primer número entero: "))
numDos= int(input("Por favor, escribe el segundo número entero: "))
numTres= int(input("Por favor, escribe el tercer número entero: "))
promedio = (numUno + numDos + numTres) / 3
print(f"El promedio entre {numUno}, {numDos} y {numTres} es {promedio}")

