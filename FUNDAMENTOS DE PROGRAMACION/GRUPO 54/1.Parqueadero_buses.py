# def parqueadero_buses(cantidad_buses: int, numero_bus: int)->int:
#     lote = numero_bus % 3
#     if lote == 0:
#         lote = 3
#     return lote

# cbuses = int(input("Ingrese la cantidad de buses: "))
# nbus = int(input("Ingrese el numero de bus: "))
# if nbus > cbuses:
#     print('El numero del bus no puede ser mayor a la cantidad de buses')
# else:
#     print('El bus {} debe parquear en el lote {}'.format(nbus, parqueadero_buses(cbuses, nbus)))
    
    
####*** si es bus es 6 el parqueo es en el 3 y asi ***### 


def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Megabus
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    pass
    total_personas = personas_bus + personas_estacion
    if total_personas > 200:
        return True
    # else:
    #     return False
    

print(despacho_buses(50,200))
print(despacho_buses(170,10))
print(despacho_buses(50,10))
print(despacho_buses(50,50))
       
     
     
     
     
     
     
     
