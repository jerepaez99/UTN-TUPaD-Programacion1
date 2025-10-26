#Ejercicio 1: Crear archivo inicial con productos: 
#Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open ("productos.txt", "w") as archivo:
    archivo.write("libro,50000.0,5\n")
    archivo.write("lapicera,200.0,40\n")
    archivo.write("lapiz,250.0,50\n")


#Ejercicio 2: Leer y mostrar productos: Crear un programa que abra productos.txt, 
#lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:

with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")


#Ejercicio 3: Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida
#al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

flag = "t"

with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")

while flag:
    with open ("productos.txt", "a") as archivo:
        producto_usuario = input("Ingrese un nuevo producto: ").lower()
        precio_usuario = float(input("Ingrese el precio del producto: "))
        cantidad_usuario = input("Ingrese la cantidad de unidades del producto: ")
        archivo.write(f"{producto_usuario},{precio_usuario},{cantidad_usuario}\n")
        flag = input("Ingrese 't' si desea continuar agregando productos, presione cualquier otra tecla para salir: ")
        



#Ejercicio 4: Cargar productos en una lista de diccionarios: Al leer el archivo, 
#cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

productos = []

with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        productos.append({"nombre": producto[0], "precio": producto[1], "cantidad": producto[2]})

for p in productos:
    print(p)


#Ejercicio 5: Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
#Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

input_usuario = input("Por favor, escriba el producto del cual desea conocer su stock: ")

for diccionario in productos:
    if input_usuario in diccionario["nombre"]:
        print(f"Producto: {diccionario["nombre"]} | Precio: {diccionario["precio"]} | Cantidad: {diccionario["cantidad"]}")
    else:
        ValueError


#Ejercicio 6: Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
#sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

with open("productos.txt", "w") as archivo:
    for diccionario in productos:
        archivo.write(f"{diccionario["nombre"]},{diccionario["precio"]},{diccionario["cantidad"]}\n")