import json
from flask import session

def filtro(x):  #3. Se consulta por Institución (ramo) y se filtra para obtener solo a las mujeres
    try:
        return x['genero']['valor'] == 'FEMENINO' and x['puesto']['nivel'] == session["puesto"]
    except (KeyError, TypeError):
        return False
  
def CantidadPorPuesto():
  archivo = open('./datos/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 
  datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
  counter = 0
  resultado = filter(filtro, datos)
  archivo.close()
  return len(list(resultado))
