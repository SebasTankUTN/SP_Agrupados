import random
from ..data.processor import * 
import src.data.loader as load 
from ..core.life_and_points import *
import src.data.show as show

def comodin_revelar_categoria(game):

    matriz_desordenada = []
    for i in range(len(game["matriz_a_jugar"])):
        if comprobar_grupo(game["matriz_a_jugar"][i],game["elementos_jugados"]) != True:
            
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



def jugar_agrupados(game:dict, grupos_de_elementos:list):

    for i in range (5):
        if verificar_vidas(game["reinicios"]):

            print(f"Nivel {game["nivel"]}")

            jugar_nivel(game, grupos_de_elementos)
            game["nivel"] += 1

            game["stage"] = 1

        else:
            game["nivel"] -= 1
            print("Te haz quedado sin reinicios: GAME OVER")
            break

    if verificar_vidas(game['reinicios']):
        
        print('Has Ganado.')
        print(f'puntuacion: {game['puntuacion']}')




def jugar_nivel(game:dict, grupos_de_elementos:list):

    for i in range (3):
        
        if verificar_vidas(game["reinicios"]):

            if verificar_vidas(game["vidas"]):

                game["matriz_a_jugar"] = generar_nuevo_stage(grupos_de_elementos, game["elementos_jugados"])
                print(f"stage: {game["stage"]}")
                game = jugar_stage(game)
                game["stage"] += 1

            else:
                
                i -= 1
                game["reinicios"] -= 1
                print(f"Te haz quedado sin vidas, se te consume un reinicio, reinicios restantes: {game["reinicios"]+1}")
                
                game["vidas"] = 3
                game["matriz_a_jugar"] = generar_nuevo_stage(grupos_de_elementos, game["elementos_jugados"],True)
                game = jugar_stage(game)

        else:
            
            break

    return game


def jugar_stage(game:dict):

    show.matriz(game["matriz_a_jugar"])
    load.elegir_comodin(game)
    elecciones = load.tomar_valores(4)

    if comprobar_grupo(elecciones,game["elementos_jugados"]):
        game["matriz_a_jugar"] = ordenar_grupo_en_linea(game["matriz_a_jugar"], elecciones, game["elementos_jugados"])
        game["puntuacion"] = sumar_puntuacion(game)
        
        print(f"Muy bien!   Puntuacion: {game["puntuacion"]}")

    else:
        game["vidas"] = perder_vida(game["vidas"])
        game["puntuacion"] = perder_puntuacion(game)
        game["errores"] += 1
        print(f"Error, el grupo no esta bien hecho!   Puntuacion: {game["puntuacion"]}")

    if comprobar_stage(game["matriz_a_jugar"], game["elementos_jugados"]) != True:
        
        if verificar_vidas(game["vidas"]):
            game = jugar_stage(game)

    else: 
        game = ultimo_grupo(game)

    return game

def ultimo_grupo(game:dict):
    
    show.matriz(game["matriz_a_jugar"])
    elecciones = load.tomar_valores(4)
    game["puntuacion"] = sumar_puntuacion(game)

    print(f"Muy bien!   Puntuacion: {game["puntuacion"]}")

    return game

def generar_nuevo_stage(grupos_de_elementos:list, grupos_jugados:list, repetir_jugados:bool = False)->list: 

    if repetir_jugados:
        
        lista_auxiliar=[]
        stage = separar_grupos(grupos_jugados, lista_auxiliar)
        stage = desordenar_grupos(stage)
    else:
        stage = separar_grupos(grupos_de_elementos, grupos_jugados)
        stage = desordenar_grupos(stage)

    return stage


# grupos_de_elementos = datos.cargar_elementos('data/archivo_partidas.csv')
# mensajes = load.init_mensaje_juego

# def submenu_juego(game, mensaje, usuario ):
    
#     planilla_stast = load.init_dict_estadisticas()

#     seguir = True
#     while seguir:
#         menu_juego = get_string(mensaje['msj_menu_juego'],mensaje['msj_submenu_error'],load_usu.validacion_string)
#         match menu_juego:
#             case '1':
#                 engine.jugar_agrupados(game, grupos_de_elementos)
#                 up.cargar_estadisticas(planilla_stast, usuario, game)
#             case '2':
#                 seguir = False
