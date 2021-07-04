        ###*** LISTAS PARALELAS

    ##** EJERCICIO
    
# desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
# luego realizar la carga por teclado de todos los datos, imprimir los nombres de las personas
# mayores de edad (mayores o iguales a 18 años.)

# nombres = []
# edades = []
# for x in range(5):
#     nom =  input("ingrese el nombre de la persona:")
#     nombres.append(nom)
#     ed = int(input("ingrese la edad de dicha persona"))
#     edades.append(ed)

# print("nombre de la personas mayores de edad:")
# for x in range(5):
#     if edades [x] >= 18:
#         print(nombres[x])


        ###*** LISTAS COMPUESTAS
        
# notas = [[8], [6],[8]]
# alturas = [1.73, 1.55, 1.92]
# dias = ["lunes", "martes", "miercoles"]
# print(notas)

# lista = [[1,2,3,4], [4,5,6], [7,8,9]]
# print(lista[1])
# for x in range(len(lista[1])):
#     print(lista[1][x])
    
# for y in range(len(lista)):
#     for x in range(len(lista[y])):
#         print(lista[y][x])

    ###*** EJEMPLO 1: REQUERIMIENTO APLICANDO LOS CONCEPTOS ANTERIORES
# ° CREAR UNA LISTA POR ASIGNACION. (LA PONE EL MISMO PROGRAMA)
# ° LA LISTA TIENE QUE TENER CUATRO ELEMENTOS.
# ° CADA ELEMENTO DEBE SER UNA LISTA DE 3 ENTEROS.
# ° IMPRIMIR SUS ELEMENTOS ACCEDIENDO DE DIFERENTES MODOS. 

# lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# # imprimimos la lista completa
# print(lista)
# print("-----------")
# #  imprimimos la primera componente
# print(lista[0])
# print("-----------")
# # imprimimos la primera  componente de la lista contenida
# # en la primera componente de la lista principal
# print(lista[0][0])
# print("-----------")
# # imprimimos con un for la lista contenida en la primera componente
# for x in range(len(lista[0])):
#     print(lista[0][x])
# print("-----------")
# # imprimimos cada elemento entero de cada lista contenida en la lista 
# for k in range(len(lista)):
#     for x in range(len(lista[k])):
#         print(lista[k][x])


##** EJEMPLO 2 
# ° CREAR UNA LISTA POR ASIGNACION
# ° LA LISTA DEBE TENER 2 ELEMENTOS 
# ° CADA ELEMENTO DEBE SER UNA LISTA DE 5 ENTEROS 
# ° CALCULAR Y MOSTAR LA SUMA DE CADA LISTA CONTENIDA EN LA LISTA PRINCIPAL 

# lista = [[1,3,5,7,9], [2,4,6,8,10]]
# for k in range(len(lista)):
#     suma = 0
#     for x in range(len(lista[k])):
#         suma = suma + lista[k][x]
# print(suma)


##** EJEMPLO 3
# ° CREAR UNA LISTA POR ASIGNACION. LA LISTA DEBE TENER 5 ELEMENTOS 
# ° CADA ELEMENTOS DEBE SER UNA LISTA, LA PRIMERA LISTA TIENE QUE TENER UN ELEMENTO, LA SEGUNDA DOS ELEMENTOS Y ASI SUCESIVAMENTE 
# ° SUMAR TODOS LOS VALORES DE LAS LISTAS 

# lista = [[1],[1,2],[1,2,3,4],[1,2,3,4,5]]
# suma = 0
# for k in range(len(lista)):
#     for x in range(len(lista[k])):
#         suma = suma + lista[k][x]
# print(suma)


##** EJEMPLO 4 
# ° DEFINIR DOS LISTAS DE 3 ELEMENTOS 
# ° EN LA PRIMERA LISTA CADA ELEMENTO ES UNA SUBLISTA CON EL NOMBRE DEL PADRE Y LA MADRE DE UNA FAMILIA 
# ° LA SEGUNDA LISTA ESTA CONSTITTUIDA POR LISTAS CON LOS NOMBRES DE LOS HIJOS DE CADA FAMILIA (PUEDE
# HABER FAMILIAS SIN HIJOS)
# ° IMPRIMIR LOS NOMBRES DEL PADRE, LA MADRE Y SUS HIJOS. TAMBIEN IMPRIMIR SOLO EL NOMBRE DEL PADRE 
# Y LA CANTIDAD DE HIJOS QUE TIENE DICHO PADRE

# padres = []
# hijos = []
# for k in range(3):
#     pa = input('ingrese el nombre del padre: ')
#     ma = input('ingrese el nombre de la madre: ')
#     padres.append([pa, ma])
#     cant = int(input('cuantos hijos tiene esta familia: '))
#     hijos.append([])
#     for x in range(cant):
#         nom = input('ingre el nombre del hijo: ')
#         hijos[k].append(nom)

# print('listado del padre, madre y sus hijos')
# for k in range(3):
#     print('padre:', padres[k][0])
#     print('madre:', padres[k][1])
#     for x in range(len(hijos[k])):
#         print('hijos:', hijos[k][x])

print('listado del padre y cantidad de hijos que tiene')
for x in range(3):
    print('padre:', padres[x][0])
    print('cantidad de hijos:', len(hijos[x]))
    
print(padres)
print(hijos)























