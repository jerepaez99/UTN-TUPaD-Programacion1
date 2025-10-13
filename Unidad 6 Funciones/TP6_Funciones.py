#Ejercicio 1: Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#def imprimir_hola_mundo():
#    print("Hola Mundo!")

#imprimir_hola_mundo()


#Ejercicio 2: Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
#“Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#def saludar_usuario(nombre):
#    print(f"Hola {nombre_usuario}!")

#nombre_usuario = input("Introduce tu nombre: ")

#saludar_usuario(nombre_usuario)


#Ejercicio 3: Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
#los datos al usuario y llamar a esta función con los valores ingresados.

#def informacion_personal(nombre, apellido, edad, residencia):
#    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#nombre_usr = input("Introduce tu nombre de pila: ")
#apellido_usr = input("Introduce tu primer apellido: ")
#edad_usr = input("Introduce tu edad: ")
#residencia_usr = input("Introduce tu lugar de residencia: ")

#informacion_personal(nombre_usr, apellido_usr, edad_usr, residencia_usr)


#Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados.

#def calcular_area_circulo(radio):
#    return 3.14 * (radio ** 2)

#def calcular_perimetro_circulo(radio):
#    return (3.14 * 2) * radio

#radio = float(input("Escribe el radio del círculo: "))

#print(f"El área del círculo es {calcular_area_circulo(radio)}")
#print(f"El perímetro del círculo es {calcular_perimetro_circulo(radio)}")


#Ejercicio 5: Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar
#el resultado usando esta función.

#def segundos_a_horas(segundos):
#    return segundos/3600

#segundos_usr = int(input("Escriba la cantidad de segundos: "))

#print(f"{segundos_usr} equivalen a {segundos_a_horas(segundos_usr)} horas")


#Ejercicio 6: Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#def tabla_de_multiplicar(numero):
#    for i in range(11):
#        producto = i * numero
#        print (f"{numero} x {i} = {producto}")

#numero_usr = int(input("Escriba el número del que desea saber la tabla de multiplicar: "))

#tabla_de_multiplicar(numero_usr)


#Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
#de forma clara.

#def operaciones_basicas(a, b):
#    print(f"{a} + {b} es = {a + b}")
#    print(f"{a} - {b} es = {a - b}")
#    print(f"{a} x {b} es = {a * b}")
#    print(f"{a} / {b} es = {a / b}")

#numA = int(input("Escribe el primer número: "))
#numB = int(input("Escribe el segundo número: "))    

#operaciones_basicas(numA, numB)


#Ejercicio 8: Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales.

#def calcular_imc(peso, altura):
#    return peso / (altura ** 2) 

#altura = float(input("Escribe tu altura expresada en metros (por ejemplo 1.75): "))
#peso = float(input("Escribe tu peso expresado en kilogramos (por ejemplo 80): "))

#print(f"Tu IMC es {round(calcular_imc(peso, altura),2)}")


#Ejercicio 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#def celsius_a_fahrenheit(celsius):
#    return (celsius * (9/5)) + 32

#celsius = int(input("Escriba la cantidad de grados celcius que desea convertir a fahrenheit: "))

#print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius)}°F")


#Ejercicio 10: Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

aNum = int(input("Escriba el primer número: "))
bNum = int(input("Escriba el segundo número: "))
cNum = int(input("Escriba el tercer número: "))

print(f"El promedio entre {aNum}, {bNum} y {cNum} es {round(calcular_promedio(aNum,bNum,cNum),2)}")

