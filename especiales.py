#Script en Python encargado de analizar que una contraseña solo contenga caracteres especiales.
import re

intento=input('Ingrese una contraseña con solo caracteres especiales: ')

comparacion='[a-zA-Z]+'
comparacion2='[0-9]+'
if re.findall(comparacion2, intento):
    print('Largate de aqui ')
elif re.findall(comparacion, intento):
    print('Largate de aqui')
else:
    print('Bienvenido..')

input('Presione enter...')        