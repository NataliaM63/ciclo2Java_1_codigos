# sacar el promedio de las notas de un estudiante utilizando una funcion 
# crear una funcion que imprima la tabla del 2

#1
def promedio():
    n1 = 5
    n2 = 3.5
    n3 = 4.5
    n4 = 5
    promedio_notas = (n1 + n2 + n3 + n4)/4
    print ("La nota promedio del estudiante es", int(promedio_notas))
    
promedio()

#2
def tabla(numero):
    for i in range (1, 11):
        print (2, "*", i, "=", 2*i)
        
tabla(2) 