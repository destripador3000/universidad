#Script en Python que Analiza que una contraseña contenga por lo menos una letra
import re

intento= input('Escribe una contraseña que solo contenga letras: ')
comparacion='[a-zA-Z]+'

if re.findall(comparacion, intento):
    print('Pasa, Binevenido')    
else:
    print('Largate de aqui por favor')  

input('Presione enter.....')

    