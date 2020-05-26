lista = ["a","b","c"]

def busqueda(valor_a_buscar):
    posicion = -1
    for n in lista:
        if(n == valor_a_buscar):
            posicion = lista.index(n)
    
    return posicion


valor = "b"
busqueda_valor = busqueda(valor)
if( busqueda_valor != -1):
    print("valor encontrado en la posicion: {}".format(busqueda_valor))