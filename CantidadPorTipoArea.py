import json
from flask import session

def filtro(x):  #3. Se consulta por Institución (ramo) y se filtra para obtener solo a las mujeres
    try:
        return x['genero']['valor'] == 'FEMENINO' and x['tipoArea'][0]['valor'] == session["tipoarea"]
    except (KeyError, TypeError):
        return False

def CantidadPorTipoArea():
  archivo = open('./datos/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 
  datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
  counter = 0
  resultado = filter(filtro, datos)
  archivo.close()
  return len(list(resultado))
