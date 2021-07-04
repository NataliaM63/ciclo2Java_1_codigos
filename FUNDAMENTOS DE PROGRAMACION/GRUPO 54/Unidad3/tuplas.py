        ###*** TUPLAS 

# t = ('esto es una cadena', 'b','c','d','e')
# print(t)
# print(t[0])
# print(type(t))

# t1 = ('a',)
# print(type(t1))

# t = tuple('lupines')
# print(t)

# txt = "but soft what light in yonder window breaks"
# palabras = txt.split()
# # palabras.sort
# print(palabras)

# l = list()
# for subcadena in palabras:
#     l.append((len(subcadena), subcadena))
# print(l)

# l.sort(reverse=True)
# print(l)

# res = list()

# for longitud, palabra in l:
#     res.append(palabra)

# print(res)


# m = ['have', 'fun'(si hay mas de tres sale error)]
# x, y = m     #o (x, y = m)

# print(x)
# print(y)

# addr = 'monty@python.org'
# uname, domain = addr.split('@')

# print(uname)
# print(domain)

    ##** DICCIONARIOS Y TUPLAS
    
# d = {'a':10, 'b':1, 'c':22}
# t = list(d.items())    # CON LA LISTA DE DUPLAS SI SE PUEDE ORDENAR EL DICCIONARIO
# print(t)

# t.sort()
# print(t)

    ##** USANDO TUPLAS COMO CLAVES EN LOS DICCIONARIOS

# directory = {}
# apellido = 'perez'
# nombre = 'pedro'
# numero = '311'
# directory[apellido, nombre] = numero
# print(directory)

# for last, first in directory:
#     print(first, last, directory[last, first])


    ##"EJEMPLO"

def RutaInicialVecinoMasCercano(distancias: dict, nodos: list) -> dict:
    # preparar las variables de salidad
    rutaSolucion = []
    kilometros = 0
    # modelar los nodos ya visitados
    yaesta = {}
    for nodo in nodos:
        yaesta.update({nodo:0})
    # inicializar el nodo de trabajo
    nodoActual = nodos[0]
    # iterar cuantos arcos debamos agregar
    for i in range(1,len(nodos)):
        # crear unicamente las llaves que me interesan 
        listallaves = []
        for nodo in nodos:  
            if nodo != nodoActual and yaesta[nodo]==0:
                arco = (nodoActual, nodo)
                listallaves.append(arco)
        # encontrar el minimo
        minimadistacia = 999999
        for arco in listallaves:
            if distancias[arco]<minimadistacia:
                minimadistacia = distancias[arco]
                minimoarco = (minimadistacia, arco)
        # actualizar las listas de solucion y de yaesta
        rutaSolucion.append(minimoarco[1])
        kilometros = kilometros + minimoarco[0]
        yaesta[minimoarco[1][0]]=1
        yaesta[minimoarco[1][1]]=1
        nodoActual = minimoarco[1][1]
    #tenemos que crear el ultimo
    ultimoarco = (nodoActual, nodos[0])
    rutaSolucion.append(ultimoarco)
    kilometros = kilometros + distancias[ultimoarco]
    #dar la salida
    salida = {}
    salida.update({"ruta":rutaSolucion})
    salida.update({"kilometraje":kilometros})
    
    return salida

distanciasEjemplo = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

nodosEjemplo = ['H', 'A', 'B', 'C', 'D', 'E', 'F']


print(RutaInicialVecinoMasCercano(distanciasEjemplo, nodosEjemplo))


















