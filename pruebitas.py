import random
from elements import elementos
from funciones_generales import *
# lista = ["papa", "cerbolla", "tomate", "pepino", "naranja"]
# random.shuffle(lista)
# print(lista)


def comprobar_grupo(elecciones:list, lista_jugados:list) -> bool:
    estado = False

    for grupo in lista_jugados:
        elementos_grupo = grupo["elementos"]
        contador = 0
        
        for eleccion in elecciones:
            if comprobar_elementos_en_lista(elementos_grupo, eleccion):
                contador += 1

        if contador == len(elecciones):
            estado = True

    return estado


# comprobar_grupo(elecciones = ["llama", "ola", "montana", "viento"],lista_jugados = elementos)


    
