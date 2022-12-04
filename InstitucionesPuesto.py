import json
from Regpearyears import Regpearyear
from flask import session

def InstitucionesPuesto():
    archivo = open('./datos/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 
    datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
    counter = 0
    years = ["2018","2019","2020","2021","2022"] #se crea una lista de años. 
    listaregYear = []
    for year in years:
        
        def filtro(x):
            if(x['genero']['valor'] == 'FEMENINO' and x['puesto']['nivel'] ==  session["InstitucionesPuesto2"] and x['ejercicioFiscal'] == year):
                return True
            else:
                return False
        #en filter solo regresan los que dan true en la funcion    
        resultado = list(filter(filtro,datos)) #se busca filtrar por genero que será siempre 'FEMENINO' y por la dependencia en turno 
        q = len(resultado) #se captura la cantidad counteable de cada dependencia analizada

        listaregYear.append(Regpearyear(year,q))

    #for obj in listaregYear:
    #    print(obj.year,obj.cantidad,sep=' => ')
    archivo.close()
    return listaregYear