productos = []

def menu():
    print("\n=====  M E N Ú  P R I N C I P A L  ===== \n   1. Agregar producto. \n   2. Buscar producto. \n   3. Eliminar producto. \n   4. Actualizar disponibilidad. \n   5. Mostrar productos. \n   6. Salir. \n========================================")

def leer_opcion():
    try:
        opcion = int(input("   (1-6) : "))

        if opcion in [1, 2, 3, 4, 5, 6]:
            return opcion
        
        else:
            print("Opción invalida: Ingrese un número del 1 al 6.")
    
    except ValueError:
        print("Error: El valor ingresado no es un número entero positivo.")

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_stock(stock):
    return stock % 1 == 0 and stock >= 0

def validar_precio(precio):
    return precio > 0

def agregar_producto(productos):
    try: 
        nombre = input("\nNombre del producto: ").capitalize()
        if not validar_nombre(nombre):
            print("El nombre no cumple con los requisitos, intente nuevamente.")
            return
        
        stock = int(input("\nStock: "))
        if not validar_stock(stock):
            print("La cantidad (el stock) no cumple con los requisitos, intente nuevamente.")
            return
        
        precio = float(input("Nota del estudiante: "))
        if not validar_precio(precio):
            print("El precio no cumple con los requisitos, intente nuevamente.")

    except ValueError:
        print("Error: El valor ingresado no coincide con su tipo.")

    producto = {"Nombre" : nombre,
                  "Stock" : stock,
                  "Precio" : precio,
                  "Estado" : False}
    
    productos.append(producto)

def buscar_producto(productos, nombre):
    for i in range(len(productos)):
        if productos[i]["Nombre"] == nombre:
            return i
    return -1

def eliminar_productos(productos, nombre):
    posicion = buscar_producto(productos, nombre)

    if posicion != -1:
        productos.pop(posicion)
        print("\nEl producto ha sido eliminado correctamente.")

    else:
        print(f"El producto {nombre} no se encuentra registrado.")

def actualizar_estado(productos):
    for i in range (len(productos)):
        if productos[i]["Stock"] > 0:
            if productos[i]["Estado"] == False:
                productos[i]["Estado"] = True
            
            else:
                print("El producto ya se encuentra disponible.")
        
        else:
            print("No hay stock del producto.")

def mostrar_productos(productos):
    actualizar_estado()

    print("\n===  L I S T A  D E  P R O D U C T O S  ===")

    for producto in productos:

        if producto[i]["Estado"] == True:
            estado = "Disponible"
        else:
            estado = "Sin stock"
        
        print(f"\n========================================================== \nNombre: {producto["Nombre"]} \nStock: {producto["Stock"]} \nPrecio: {producto["Precio"]} \nEstado: {producto["Estado"]} \n==========================================================")

while True:
    menu()
    opcion = leer_opcion()

    if opcion == 1: #Agregar producto
        agregar_producto()

    elif opcion == 2: #Buscar productos
        if len(productos) == 0:
            print("No hay productos registrados, no puede usar esta función.")

        else:
            nombre = input("Nombre del producto a buscar: ").capitalize()
            
            posicion = buscar_producto(productos, nombre)
            if posicion != -1:
                print("Producto encontrado.") #Mostrar datos
                producto = productos[posicion]
                print(f"\n========================================================== \nNombre: {producto["Nombre"]} \nStock: {producto["Stock"]} \nPrecio: {producto["Precio"]} \nEstado: {producto["Estado"]} \n==========================================================")


            else:
                print("El producto no se encontro.")

    elif opcion == 3: #Eliminar productos
        if len(productos) == 0:
            print("No hay productos registrados, no puede usar esta función.")

        else:
            nombre = input("Nombre del producto a eliminar: ").capitalize()
            eliminar_productos(productos, nombre)
            print("El producto ha sido eliminado.")

    elif opcion == 4: #Actualizar estado
        if len(productos) == 0:
            print("No hay productos registrados, no puede usar esta función.")

        else:
            actualizar_estado(productos)
            print("La lista de productos ha sido actualizada.")

    elif opcion == 5: #Mostrar productos
        if len(productos) == 0:
            print("No hay productos registrados, no puede usar esta función.")

        else:
            mostrar_productos(productos)

    else:
        print("\nGracias por usar el sistema. Vuelva pronto.")
        break