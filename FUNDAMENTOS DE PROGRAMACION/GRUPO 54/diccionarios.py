###*** DICCIONARIOS - DEFINICION Y ALMACENAMIENTO DE DATOS
###*** HAY QUE CEPARAR CADAD ELEMENTO CON ,


# diccionario = {}
# print(diccionario)

# diccionario = dict()
# print(diccionario)

## EJEMPLO

# diccionario = {"total": 55}
# print(diccionario)
# otrodiccionario = {"copia": 123.23}
# print(otrodiccionario)

# diccionario = {"total": 55, "descuento": True, 15: "15"}
# print(diccionario)
# diccionarioEjemploExcel = {"nombre": 5+2, "telefono": 3363692, "edad": 33, "ciudad": "pereira"}
# print(diccionarioEjemploExcel)

# diccionario = dict(total= 55, descuento= True, subtotal = 15) #dict coloca las comillas y se coloca los igaules en vez de dos puntos (: --> =)
# print(diccionario)

# diccionario = dict(total=55, descuento=True, descuento5=True, subtotal="15")

# print(diccionario)
# print(diccionario['subtotal'])


# diccionario = dict()
# print(diccionario)

# diccionario['marca'] = 'Mazda'
# print(diccionario['marca'])

# diccionario['marca'] = 'Subaru'
# print(diccionario['marca'])

# diccionario['color'] = 'rojo'
# print(diccionario['color'])

# print(diccionario)

# diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
# print(diccionario)
# # diccionario.keys()
# diccionario.values()


# def promedionotas2(dicnotas):

###*** METODOS 
# Los objetos de tipo diccionario tienen por defecto una serie de métodos integrados, a continuación:

# # clear()

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones.clear()
# print(versiones)

# # copy()

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# otra_versiones = versiones.copy()
# print(versiones == otra_versiones)
# print(versiones)
# print(otra_versiones)

# # fromkeys()

# secuencia = ('python', 'zope', 'plone')
# versiones = dict.fromkeys(secuencia)
# print("Nuevo Diccionario : %s" %  str(versiones))
# print("Nuevo Diccionario : {}".format(str(versiones)))

# versiones = dict.fromkeys(secuencia, 0.1)
# print("Nuevo Diccionario : %s" %  str(versiones))

# get()

#  versiones = dict(python=2.7, zope=2.13, plone=5.1)
# versiones.get('plone')
# print(versiones.get('plone'))
# print ['plone']
#print(versiones.get('php'))

# # items()

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones.items())

# # pop()

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# versiones
# print(versiones.pop('zope'))
# versiones

# # update()  se unen 

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones_adicional = dict(django=2.1)
# print(versiones_adicional)
# versiones.update(versiones_adicional)
# print(versiones)

# versiones_adicional.update(versiones)   
# print(versiones_adicional)


# usuario = {
#     'nombre': 'Nombre del usuario',
#     'edad' : 23, 
#     'curso': 'Curso de Python',
#     'skills':{
#         'programacion' : True,
#         'base_de_datos': False
#     },
#     'No medallas' : 10
# }

# print(usuario)
# print(usuario['curso'])
# print(usuario['skills'])
# print(usuario['skills']['base_de_datos'])



# from math import inf


# informacion = { 'alumno1': {'nombre': 'Daniel', 'edad': 11, 'estatura': 1.75, 'grado': 'Master'},
#                 'alumno2': {'nombre': 'David', 'edad': 32, 'estatura': 1.85, 'grado': 'Doctor'}  }

# print(informacion)


###*** COMPARAR LOS NOMBRES DE LOS ESTUDIANTES 
# if informacion ['alumno1']['nombre'] == informacion ['alumno2']['nombre']:
#     print("Los nombres son iguales")
# else:
#     print("Los nombres son diferentes")
     

###*** MIREMOS QUIEN ES MAYOR 
# if informacion ['alumno1']['edad'] > informacion ['alumno2']['edad']:
#     print(str(informacion['alumno1']['nombre']) + ' es mayor')
#     mayor = {'nombremayor': informacion['alumno1']['nombre'], 'edadmayor': informacion['alumno1']['nombre'] }
# elif informacion['alumno1']['edad'] < informacion['alumno2']['edad']:
#     mayor = {'nombremayor': informacion['alumno2']['nombre'], 'edadmayor': informacion['alumno2']['nombre'] }
#     print(str(informacion['alumno1']['nombre']) + ' es menor')
 
    
###*** EJEMPLO CINE UKUMARI (autocinema)  ####***tambien se puede colocar el elif
def desperdicio_de_gaseosa(amigo_1: dict, amigo_2: dict, amigo_3: dict, capacidad_boton: float)->str:
    capacidad_dip_a1 = amigo_1['capacidad_vaso']-amigo_1['capacidad_actual']   ###*** SE RESTA LOS VALORES a1
    capacidad_dip_a2 = amigo_2['capacidad_vaso']-amigo_2['capacidad_actual']
    capacidad_dip_a3 = amigo_3['capacidad_vaso']-amigo_3['capacidad_actual']
    if capacidad_boton > capacidad_dip_a1:
        return amigo_1['nombre']
    if capacidad_boton > capacidad_dip_a2:   
        return amigo_2['nombre']
    if capacidad_boton > capacidad_dip_a3:
        return amigo_3['nombre']
    else:
        return None
    
a1 = {
    'nombre': 'Mariana', 
    'capacidad_vaso': 150.0,
    'capacidad_actual': 50.0
}
    
a2 = {
    'nombre': 'Steve', 
    'capacidad_vaso': 250.0,
    'capacidad_actual': 200.0  
}    

a3 = {
    'nombre': 'Johana', 
    'capacidad_vaso': 200.0,
    'capacidad_actual': 160.0  
}    

cantidad = float(input('Ingrese la cantidad de gaseosa: '))

print('A {} se le riega la gaseosa'.format(desperdicio_de_gaseosa(a1, a2, a3, cantidad)))


