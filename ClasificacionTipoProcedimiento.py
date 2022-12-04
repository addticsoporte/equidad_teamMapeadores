import json
from Rankings import Ranking
from itertools import islice 

def TiposProcedimiento():
    archivo = open('./datos/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

    datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON

    counter = 0
    listatiposProcedimiento = [] #se crea una lista de puesto. 
    def retrieve(x): #Se busca ahora que se regrese el valor de ramo por cada registro.
        try:
            return x['tipoProcedimiento'][0]['valor'] #retorna el valor del puesto 
        except (KeyError, TypeError):
            return False
    for x in datos: #En cada registro
        valor = retrieve(x) #se ejecuta esta función que recupera el valor del ramo dependencia 
        listatiposProcedimiento.append(valor) #se inserta una dependencia a la lista

    listatiposProcedimiento = list(set(listatiposProcedimiento)) #se quitan los valores duplicados
    archivo.close()
    return listatiposProcedimiento


def TipoProcedimientoMenor():
    listatiposProcedimiento=TiposProcedimiento()
    # Se procede a contar el total de mujeres por dependencia. 
    
    archivo = open('./datos/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

    datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON

    listaRanking = [] #se crea una lista de rankings

    for tipoProcedimiento in listatiposProcedimiento:
        
        def filtro(x):
            #print(ramo)
            if(x['genero']['valor'] == 'FEMENINO' and x['tipoProcedimiento'][0]['valor'] == tipoProcedimiento):
            #  print(ramo)
                return True
            else:
                return False
        #en filter solo regresan los que dan true en la funcion    
        resultado = list(filter(filtro,datos)) #se busca filtrar por genero que será siempre 'FEMENINO' y por la dependencia en turno 
        q = len(resultado) #se captura la cantidad counteable de cada dependencia analizada

        listaRanking.append(Ranking(tipoProcedimiento,q))

    ##se procede a mostrar el orden ascendente, del mas bajo al mas alto.     
    #print("Los menos 5")
    listaRanking.sort(key=lambda x:x.cantidad)
    lest5 = islice(listaRanking,5)
    #for obj in lest5:
    #    print(obj.dependencia,obj.cantidad,sep=' => ')
    archivo.close()
    return lest5


def TipoProcedimientoMayor():
    listatiposProcedimiento=TiposProcedimiento()
    # Se procede a contar el total de mujeres por dependencia. 
    
    archivo = open('./datos/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

    datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON

    listaRanking = [] #se crea una lista de rankings

    for tipoProcedimiento in listatiposProcedimiento:
        
        def filtro(x):
            #print(ramo)
            if(x['genero']['valor'] == 'FEMENINO' and x['tipoProcedimiento'][0]['valor'] == tipoProcedimiento):
            #  print(ramo)
                return True
            else:
                return False
        #en filter solo regresan los que dan true en la funcion    
        resultado = list(filter(filtro,datos)) #se busca filtrar por genero que será siempre 'FEMENINO' y por la dependencia en turno 
        q = len(resultado) #se captura la cantidad counteable de cada dependencia analizada

        listaRanking.append(Ranking(tipoProcedimiento,q))

    ##se procede a mostrar el orden descendente, del mas bajo al mas alto.    
    #print("Top 5")
    listaRanking.sort(key=lambda x:x.cantidad,reverse=True)
    top5 = islice(listaRanking,5)
    #for obj in top5:
    #    print(obj.dependencia,obj.cantidad,sep=' => ')
    archivo.close()
    return top5

