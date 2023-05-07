#Nombres: Juan Esteban Valencia Londoño#
#         Liseth Yurani Ortega Hurtado#        
#         Julian Alberto Londoño Mesa        
#Profesor(a):Andrea Palomino Salcedo #
#Tecnología en desarrollo de software código: 2724#
#Laboratorio Número 2#
### Medidor de IMC ###

nombre =input('Escriba su nombre: ' )
peso = float(input('Escribe tu peso: ')) 
altura = float(input('Introduzca su altura '))
def medida(nombre,peso,altura):
    imc = peso/(altura * altura)
    if imc <= 18.5:
        print(" Paciente: ", nombre,"\n","IMC: ", imc,"\n","Categoría: Infrapeso" )
    elif imc <= 25 and imc >= 18.6:
        print(" Paciente: ", nombre,"\n","IMC: ", imc,"\n","Categoría: Normal" )
    else:
        print(" Paciente: ", nombre,"\n","IMC: ", imc,"\n","Categoría: Sobrepeso" )
        
        


medida(nombre,peso,altura) 


















