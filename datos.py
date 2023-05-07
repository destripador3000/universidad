#Script en Python encargado de guardar datos guardados en un archivo de texto plano
from io import open

def menu():
    print(''' Estas son las opciones que tenemos: 
1) Ingresar Usuario
2) Modificar Archivo
3) Leer Archivo 
0) Salir
    
    ''')


info=[]
def feedback(info):
    usuarios=int(input('¿Cuantos usuarios vas a ingresar? '))
    for i in range(usuarios):
        correo=input('Ingresa tu correo: ')
        numero=int(input('Ingrese su número de celular: '))
        nombre=input('Ingrese su nombre: ')
        cuenta=int(input('Ingrese número de la cuenta: '))
        contraseña=input('Ingrese la contraseña: ')
        

        info.append(correo)
        info.append(numero)
        info.append(nombre)
        info.append(cuenta)
        info.append(contraseña)
        datas=open("base.txt","a")
        datas.write(f"{info} \n")
        datas.close()
    
def modificar_archivo(info):
    dato=open("base.txt","w")
    dato.write(info)
    dato.close()

def leer_archivo(info):
    dato=open("base.txt","r")
    data=info.read()
    dato.close()
    print(data)
    




def main():
    
    continuar=True
    while continuar:
        menu()
        opc=int(input('Ingrese una opcion: '))
        if opc == 1:
            feedback()
        elif opc == 2:
            modificar_archivo()
        elif opc ==3:
            leer_archivo()
        elif opc == 0:
            continuar == False
        else:
            print('Opción no válida') 
        input('Enter para continuar...') 

if __name__=='__main__':
    main()
                            