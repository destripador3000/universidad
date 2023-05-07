#Script en Python que analiza una contraseña contenga por lo menos un número 
import re

def contraseña():
    intento = input('Escribe una contraseña que solo contenga números: ')
    comparacion='[0-9]+'
    if re.findall(comparacion, intento):
        print('Por favor sigue...')
    else:
        print('Largate de aqui...')

contraseña()
input('Presiona enter....')    








