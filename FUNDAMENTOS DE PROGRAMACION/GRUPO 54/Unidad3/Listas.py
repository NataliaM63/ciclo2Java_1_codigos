    ###*** LISTAS 

# lista = [1, 2.5, 'DevCode', [5,6] ,4]

# print(lista[0]) # 1
# print(lista[1]) # 2.5
# print(lista[2]) # DevCode
# print(lista[3]) # [5,6]
# print(lista[3][0]) # 5
# print(lista[3][1]) # 6
# print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode']
# print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
# print(lista[1:6:2]) # [2.5, [5, 6]]
# print("Hola Estructura de Lenguajes") 

    ###*** LISTA VACIA 
# lista = [ ]
# print(lista)


    #### ejemplo 
# ##*** aunque tengan el mismo valor en nombre en la memoria esta guardo el prmero valor (pepe)
# nombre = "PEPE"
# edad = 25
# listas = [nombre, edad]
# print(listas)

# nombre = "juan"
# print(listas)

# nombres = ["Ana", "Bernardo"]
# edades = [22, 21]
# lista = [nombres, edades]
# print(lista)

# nombres += ["Cristina"]
# print(lista)

# factura = ['Pan', 'huevos', 100, 1234]
# print(factura)

# print(factura[0])
# print(factura[3])

#     ### len() devuelve la longitud de la lista (su cantidad de elementos)

# print(len(factura))
# print(len(factura) -1)

# print(factura[-1])
# print(factura[-len(factura)])

# factura[1] = "carne"
# print(factura)

# factura[-1] = '1000'
# print(factura)

    ###*** METODOS
##** append()

# versiones_plone = [2.5, 3.6, 4, 5]
# print(versiones_plone)

# versiones_plone.append('j')
# print(versiones_plone)

# versiones_plone.append({'k':1000})
# print(versiones_plone)

##** count() "contar el numero de apariciones en la cadena"

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print("6 ->", versiones_plone.count(6))
# print("5 ->", versiones_plone.count(5))
# print("2.5 ->", versiones_plone.count(2.5))

##** extend() "los agraga o los extiende por separado"

# versiones_plone = [2.1, 2.5, 3.6]
# print(versiones_plone)

# versiones_plone.extend(['s'])
# print(versiones_plone)

# versiones_plone.extend(range(5,7))
# print(versiones_plone)

# versiones_plone.extend(range(0,10))
# print(versiones_plone)

##** index()

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
# print(versiones_plone.index(4))

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
# print(versiones_plone[2j])

##** insert()

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone)

# versiones_plone.insert(2, 3.7)
# print(versiones_plone)

##** pop()

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone.pop())
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone.pop(2))
# print(versiones_plone)

##** remove()

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 2.5]
# print(versiones_plone)

# versiones_plone.remove(2.5)
# print(versiones_plone)

##** reverse()

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 2.5]
# print(versiones_plone)

# versiones_plone.reverse()
# print(versiones_plone)

# num_inv = ''
# num = str('45625')
# l = list(num)
# l.reverse()
# for j in l:
#     num_inv += j 
# print(num, num_inv)
# if num == num_inv:
#     print('palindromo')
# else: 
#     print('no es palindromo')
    

# num_inv = ''
# num = str('1258521')
# l = list(num)
# l.reverse()
# for j in l:
#     num_inv += j 
# print(num, num_inv)
# if num == num_inv:
#     print('palindromo')
# else: 
#     print('no es palindromo')
    
# l2 = l
# print(l2)
# # if l1 == l2:
# #     print('palindromo')
# # else:
# #     print('no es palindromo')

##** sort()

# versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
# print(versiones_plone)

# versiones_plone.sort()
# print(versiones_plone)

# versiones_plone = ['s', 'a']
# print(versiones_plone)

# versiones_plone.sort()
# print(versiones_plone)

##** EJEMPLO

# lista = [2, "CMS", True, ["plone", 10]]
# print(lista, type(lista))

# l2 = lista[1]
# print(l2)

# l3 = lista[3][0]
# print(l3)

# lista[1] = 4
# print(lista)

# lista[1] = "CMS"
# print(lista)

# l3 = lista[0:3]
# print(l3)

# l4 = lista[0:3:2]
# print(l4)

# l5 = lista[1::2]
# print(l5)

##** ITERAR SOBRE UNA CADENA DE CARACTERES

# vocales = 'aeiou'
# for letra in 'hermosa':
#     if letra in vocales:
#         print(letra)

##** ITERAR SOBRE UNA LISTA 

# mensaje = "Hola, como estas tu?"
# m = mensaje.split()
# print(m)
# for palabra in mensaje.split():
#     print(palabra)

##** ITERAR SOBRE DOS O MAS SECUENCIAS

preguntas = ['nombre', 'objetivo', 'sistema operativo']
respuestas = ['leonardo', 'aprender python y plone', 'linux']
for preguntas, respuestas in zip(preguntas, respuestas):
    print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(preguntas, respuestas))



