#Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los 
#números enteros entre 1 y el número que indique el usuario

#input_usuario = int(input("Escriba un número: "))

#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n - 1)
    
#def factoriales(n):
#    if n == 0:
#        return 1
#    else: 
#        print(factorial(n))
#        factoriales(n - 1)

#print(factorial(input_usuario))

#factoriales(input_usuario)


#Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci 
#en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que 
#el usuario especifique.

#input_usuario_fibonacci = int(input("Escriba un número: "))

#def fibonacci(n):
#    if n == 0 or n == 1:
#        return n
#    else:
#        return fibonacci(n - 1) + fibonacci (n - 2)

#def fibonaccis(n):
#    if n >= 0:
#        print(fibonacci(n))
#        fibonaccis(n - 1)

#print(fibonacci(input_usuario_fibonacci))

#fibonaccis(input_usuario_fibonacci)


#Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

#def potencia(base, exponente):
#    if exponente == 0:
#        return 1
#    else:
#        return base * potencia(base, exponente - 1)
    
#base = int(input("Ingrese la base: "))
#exponente = int(input("Ingrese un exponente: "))
#resultado_potencia = potencia(base, exponente)

#print(f"{base} elevado a la {exponente} es igual a: {resultado_potencia}")
