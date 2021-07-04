# def compra_producto(valor_producto: int, nro_cuotas: int)->dict:
#      ''' Compra de producto con financiamiento
#  Parámetros:
#  valor_producto (int): Valor del producto
#  nro_cuotas (int): Número de cuotas a financiar el producto
#  Retorno:
#  dict: Diccionario con las siguientes llaves:
#  ‘valor_producto’: valor del producto (int),
#  'cuota_inicial': valor de la cuota inicial (int),
#  ‘nro_cuotas’: número de cuotas (0-18) (int)
#  ‘valor_cuota’: valor de la cuota (int),
#  ‘valor_final_producto’: valor total del producto incluyendo el valor adicional de los intereses (int)
#  '''
#  pass


def compra_producto(valor_producto: int, nro_cuotas: int)->dict:
    dic_compra = {}
    if nro_cuotas >= 1 and nro_cuotas <= 18:
        cuota_inicial = valor_producto * 15 / 100
        valor_deuda = valor_producto - cuota_inicial 
        valor_cuota = 0.0
        
        if nro_cuotas <= 6:
            valor_cuota = (valor_deuda * 1.10) / nro_cuotas
        elif nro_cuotas <= 12:
            valor_cuota = (valor_deuda * 1.12) / nro_cuotas
        else:
            valor_cuota = (valor_deuda * 1.15) / nro_cuotas
        valor_final = cuota_inicial + (valor_cuota * nro_cuotas)  
        
        return {'valor_producto': int (valor_producto),
                'cuota_inicial': int (cuota_inicial),
                'nro_cuotas': nro_cuotas,
                'valor_cuota': int (valor_cuota),
                'valor_final_producto': int (valor_final)}
    else: 
        if nro_cuotas <1 or nro_cuotas> 18:
            return dic_compra
        

print(compra_producto(1200000))
print(compra_producto(1200000, -1))
print(compra_producto(1200000, 29))













