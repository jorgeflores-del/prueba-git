"""1-1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
notas, cantidad de faltas, cantidad de amonestaciones recibidas.
Recomendación: Para llevar un registro de estos dato se puede
utilizar un diccionario estructurado de la siguiente manera:
{
“Alumnos” : [alumno1,alumno2,alumno3 ]
}
Donde cada alumno es otro diccionario estructurado de la
siguiente forma:
{
“Nombre”: nombre de alumno,
“Apellido” : apellido de alumno,
“DNI” : DNI de alumno
“Fecha de nacimiento”, fecha de nacimiento de alumno,
“Tutor” : nombre y apellido de tutor,
“Notas” : todas las notas del alumno,
“Faltas” : cantidad de faltas,
“amonestaciones” : cantidad de amonestaciones
}
En esta estructura:
Datos = {
“Alumnos” : [alumno1,alumno2,alumno3 ]
}
Para acceder por ejemplo al numero de DNI del tercer alumno
podríamos hacer algo así:
Datos[“Alumnos”][2][“DNI”]
Este es un ejemplo de estructura, se puede cambiar
completamente o hacer algunos cambios sobre el para mejorar el
orden (si lo consideran necesario)
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos
RECOMEDACIONN GENERAL:
El programa es extenso, hacer por partes.
Llevará mucho tiempo, la paciencia es importante.
Internet es una gran ayuda.
La prolijidad es fundamental
Las funciones tendrán que recibir como parámetros los diccionarios que
representan a los alumnos. """

Datos = {
    "Alumnos": []
}
def agregar_alumno(nombre, apellido, dni, fecha_nacimiento, tutor):
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    Datos["Alumnos"].append(alumno)
    print("Alumno",nombre,apellido,"agregado con éxito.")

def mostrar_alumnos():
    print (Datos)

def modificar_alumno(indice, campo, nuevo_valor):
    if 0 <= indice < len(Datos["Alumnos"]):
        if campo in Datos["Alumnos"][indice]:
            Datos["Alumnos"][indice][campo] = nuevo_valor
            print("Datos del alumno",indice + 1,"actualizados.")
        else:
            print("Campo no válido.")
    else:
        print("error.")

def expulsar_alumno(indice):
    if 0 <= indice < len(Datos["Alumnos"]):
        expulsado = Datos["Alumnos"].pop(indice)
        print("Alumno",expulsado['Nombre'],expulsado['Apellido'],"expulsado con éxito.")
    else:
        print("error.")

def menu():
    while True:
        print("bienvenido al menu, elige tu opcion")
        print("1. Agregar ")
        print("2. Mostrar ")
        print("3. Modificar ")
        print("4. Expulsar ")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            fecha_nacimiento = input("Fecha de nacimiento: ")
            tutor = input("Nombre y apellido del tutor: ")
            agregar_alumno(nombre, apellido, dni, fecha_nacimiento, tutor)
        
        elif opcion == "2":
            mostrar_alumnos()
        
        elif opcion == "3":
            indice = int(input("Índice del alumno a modificar (1 para el primer alumno): ")) - 1
            campo = input("Campo a modificar (Nombre, Apellido, DNI, Fecha de nacimiento, Tutor, Notas, Faltas, Amonestaciones): ")
            nuevo_valor = input("Nuevo valor: ")
            modificar_alumno(indice, campo, nuevo_valor)
        
        elif opcion == "4":
            indice = int(input("Índice del alumno a expulsar (1 para el primer alumno): ")) - 1
            expulsar_alumno(indice)       
        elif opcion == "5":
            print("Saliendo del programa.")
            break       
        else:
            print("Opción no válida. Intente de nuevo.")
menu()
