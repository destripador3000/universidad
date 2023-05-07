    
import getpass     
    
    
    
    
usuario = 'juan'  
password = 'arroz2'


usuario = getpass.getuser()
contrasenna= getpass.getpass()
input('Presiona enter...')    
if contrasenna == password:
    print(f'Bienvenido {usuario}')
    input('Presiona enter...')
else:        
    print('Ocurrio un error fijate que si introdujiste todo correctamente...') 
    
    
    
input('Presiona enter...')





