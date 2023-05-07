#Script en Python encargado en el fácil procesamiento de tareas y datos extraidos.

tareas=[]
def menu():
    print('''Este es un ejemplo básico de procesamiento de datos en el sistema
    Menú:
    1)  Mostrar Tareas
    2)  Mostrar datos introducidos
    3)  Asignar tarea a un usuario
    4)  Mostrar Usuario
    5)  Mostrar tareas asignadas a cada usuario.
    6)  Agregar tarea
    7)  Borrar Tarea
    8)  Asignar Usuario
    9)  Borrar Usuario
    0)  Salir

    ''')

#Problemas con la utilizacion de la lista y sus elementos
def agregar(tareas, tarea):
    tareas=[]
    print('Por favor sea breve con la tarea asignada...')
    tarea=input('Escriba una tarea...')
    tareas.append(tarea)

longitud=len(tareas)
#Problemas con la utilizacion de la lista y sus elementos
def mostrar(tareas):

    if longitud == 0:
        print('No hay elementos por mostrar...')
    else:
        print


    
