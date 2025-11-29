import random
import src.data.processor as processor
import src.data.loader as load 
import pygames.core as core
import src.core.life_and_points as points
import src.data.show as show
def comodin_revelar_categoria(game):

    matriz_desordenada = []
    for i in range(len(game["matriz_a_jugar"])):
        if processor.comprobar_grupo(game["matriz_a_jugar"][i],game["elementos_jugados"]) != True:
            
            matriz_desordenada += [game["matriz_a_jugar"][i]]

    indice_fila = random.randint(0,len(matriz_desordenada)-1)
    indice_columna = random.randint(0,len(matriz_desordenada[0])-1)

    elemento = matriz_desordenada[indice_fila][indice_columna]
    for grupo in game["elementos_jugados"]:
        if elemento in grupo["elementos"]:
            nombre_grupo = grupo["titulo"]
            break
        else:
            nombre_grupo = "x"

    encontrado = {"elementos":elemento,"grupo":nombre_grupo}
    
    return encontrado

def comodin_revelar_dos_elementos(game,igual_categoria = True):
    
    bandera_comparando = True
    while bandera_comparando:
        elemento1 = comodin_revelar_categoria(game)
        elemento2 = comodin_revelar_categoria(game)
        if igual_categoria:
            if elemento1["elementos"] != elemento2["elementos"] and elemento1["grupo"] == elemento2["grupo"]:
                bandera_comparando = False
                elementos_encontrados = [elemento1["elementos"],elemento2["elementos"]]
        else:
            if elemento1["elementos"] != elemento2["elementos"] and elemento1["grupo"] != elemento2["grupo"]:
                bandera_comparando = False
                elementos_encontrados = [elemento1["elementos"],elemento2["elementos"]]
    
    return elementos_encontrados