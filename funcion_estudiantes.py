estudiantes = []

def menu():
    print("\n=====  M E N Ú  P R I N C I P A L  ===== \n   1. Agregar estudiante. \n   2. Buscar estudiante. \n   3. Eliminar estudiante. \n   4. Actualizar estados. \n   5. Mostrar estudiantes. \n   6. Salir. \n========================================")

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

def validar_edad(edad):
    return edad % 1 == 0 and edad > 0

def validar_nota(nota):
    return 1 <= nota <= 7

def agregar_estudiante(estudiantes):
    try: 
        nombre = input("\nNombre del estudiante: ").capitalize()
        if not validar_nombre(nombre):
            print("El nombre no cumple con los requisitos, intente nuevamente.")
            return
        
        edad = int(input("\nEdad del estudiante: "))
        if not validar_edad(edad):
            print("La edad no cumple con los requisitos, intente nuevamente.")
            return
        
        nota = float(input("Nota del estudiante: "))
        if not validar_nota(nota):
            print("La nota no cumple con los requisitos, intente nuevamente.")

    except ValueError:
        print("Error: El valor ingresado no coincide con su tipo.")

    estudiante = {"Nombre" : nombre,
                  "Edad" : edad,
                  "Nota" : nota,
                  "Estado" : False}
    
    estudiantes.append(estudiante)

def buscar_estudiante(estudiantes, nombre):
    for i in range(len(estudiantes)):
        if estudiantes[i]["Nombre"] == nombre:
            return i
    return -1

def eliminar_estudiante(estudiantes, nombre):
    posicion = buscar_estudiante(estudiantes, nombre)

    if posicion != -1:
        estudiantes.pop(posicion)
        print("\nEl estudiante ha sido eliminado correctamente.")

    else:
        print(f"El estudiante {nombre} no se encuentra registrado.")

def actualizar_estado(estudiantes):
    for i in range (len(estudiantes)):
        if estudiantes[i]["Nota"] >= 4:
            if estudiantes[i]["Estado"] == False:
                estudiantes[i]["Estado"] = True
            
            else:
                print("El estudiante ya esta aprobado.")
        
        else:
            print("No se puede aprobar al estudiante por nota baja.")

def mostrar_estudiantes(estudiantes):
    actualizar_estado()

    print("\n===  L I S T A  D E  E S T U D I A N T E S  ===")
    
    for estudiante in estudiantes:
        
        if estudiante[i]["Estado"] == True:
            estado = "Disponible"
        else:
            estado = "Sin stock"

        print(f"\n========================================================== \nNombre: {estudiante["Nombre"]} \nEdad: {estudiante["Edad"]} \nNota: {estudiante["Nota"]} \nEstado: {estudiante["Estado"]} \n==========================================================")

while True:
    menu()
    opcion = leer_opcion()

    if opcion == 1: #Agregar estudiantes
        agregar_estudiante()

    elif opcion == 2: #Buscar estudiantes
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados, no puede usar esta función.")

        else:
            nombre = input("Nombre del estudiante a buscar: ").capitalize()
            
            posicion = buscar_estudiante(estudiantes, nombre)
            if posicion != -1:
                print("Estudiante encontrado.") #Mostrar datos
                estudiante = estudiantes[posicion]
                print(f"\n========================================================== \nNombre: {estudiante["Nombre"]} \nEdad: {estudiante["Edad"]} \nNota: {estudiante["Nota"]} \nEstado: {estudiante["Estado"]} \n==========================================================")


            else:
                print("El estudiante no se encontro.")

    elif opcion == 3: #Eliminar estudiantes
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados, no puede usar esta función.")

        else:
            nombre = input("Nombre del estudiante a eliminar: ").capitalize()
            eliminar_estudiante(estudiantes, nombre)
            print("El estudiante ha sido eliminado.")

    elif opcion == 4: #Actualizar estado
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados, no puede usar esta función.")

        else:
            actualizar_estado(estudiantes)
            print("La lista de estudiantes ha sido actualizada.")

    elif opcion == 5: #Mostrar estudiantes
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados, no puede usar esta función.")

        else:
            mostrar_estudiantes(estudiantes)

    else:
        print("\nGracias por usar el sistema. Vuelva pronto.")
        break