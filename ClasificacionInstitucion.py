import json
from Rankings import Ranking
from itertools import islice



# Se busca ahora que se regrese el valor de ramo por cada registro.
def retrieve(x):
    try:
        return x['ramo']['valor']  # retorna el valor del ramo
    except (KeyError, TypeError):
        return False


def ObtenerDependencias():
    # 1 . Se ubica el archivo JSON para abrirlo.
    archivo = open('./datos/data-0000000001.json', encoding="utf8")
    # 2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
    datos = json.load(archivo)
    counter = 0
    listaDependencias = []  # se crea una lista de dependencias.
    for x in datos:  # En cada registro
        # se ejecuta esta función que recupera el valor del ramo dependencia
        valor = retrieve(x)
        listaDependencias.append(valor)  # se inserta una dependencia a la lista

    # se quitan los valores duplicados
    listaDependencias = list(set(listaDependencias))
    archivo.close()
    return listaDependencias



# Se procede a contar el total de mujeres por dependencia.
def MujeresPorDependenciaMenor():
    listaDependencias=ObtenerDependencias()
    archivo = open('./datos/data-0000000001.json', encoding="utf8")
    # 2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
    datos = json.load(archivo)
    archivo.close()

    listaRanking = []  # se crea una lista de rankings

    for ramo in listaDependencias:
        def filtro(x):
            # print(ramo)
            if (x['genero']['valor'] == 'FEMENINO' and x['ramo']['valor'] == ramo):
                #  print(ramo)
                return True
            else:
                return False
        # en filter solo regresan los que dan true en la funcion
        # se busca filtrar por genero que será siempre 'FEMENINO' y por la dependencia en turno
        resultado = list(filter(filtro, datos))
        # se captura la cantidad counteable de cada dependencia analizada
        q = len(resultado)
        listaRanking.append(Ranking(ramo, q))

    # se procede a mostrar el orden ascendente, del mas bajo al mas alto.
    #print("Los menos 5")
    listaRanking.sort(key=lambda x: x.cantidad)
    lest5 = islice(listaRanking, 5)
    #for obj in lest5:
    #    print(obj.dependencia, obj.cantidad, sep=' => ')
    return lest5

# Se procede a contar el total de mujeres por dependencia.
def MujeresPorDependenciaMayor():
    listaDependencias=ObtenerDependencias()
    archivo = open('./datos/data-0000000001.json', encoding="utf8")
    # 2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
    datos = json.load(archivo)
    archivo.close()

    listaRanking = []  # se crea una lista de rankings

    for ramo in listaDependencias:
        def filtro(x):
            # print(ramo)
            if (x['genero']['valor'] == 'FEMENINO' and x['ramo']['valor'] == ramo):
                #  print(ramo)
                return True
            else:
                return False
        # en filter solo regresan los que dan true en la funcion
        # se busca filtrar por genero que será siempre 'FEMENINO' y por la dependencia en turno
        resultado = list(filter(filtro, datos))
        # se captura la cantidad counteable de cada dependencia analizada
        q = len(resultado)
        listaRanking.append(Ranking(ramo, q))

    # se procede a mostrar el orden descendente, del mas bajo al mas alto.
    #print("Top 5")
    listaRanking.sort(key=lambda x: x.cantidad, reverse=True)
    top5 = islice(listaRanking, 5)
    #for obj in top5:
    #    print(obj.dependencia, obj.cantidad, sep=' => ')
    return top5

