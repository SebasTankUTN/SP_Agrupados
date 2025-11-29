import random
import src.data.processor as processor
import src.data.loader as load 
import pygames.core as core
import src.core.life_and_points as points
import src.data.show as show

def mostrar_comodin_1(respuesta_comodin, juego):
    for objeto_matriz in juego["objetos_a_mostrar"]:
        if "boton_matriz" in objeto_matriz["nombre"] and objeto_matriz["valor"] == respuesta_comodin["elementos"]:
            objeto_matriz["color"] = (80, 110, 217)
        if objeto_matriz["nombre"] == "nombre_grupos":
            objeto_matriz["objeto"] = objeto_matriz["fuente"].render(respuesta_comodin["grupo"], True, objeto_matriz["color"])

def mostrar_comodines_2_y_3(respuesta_comodin, juego, tercer_comodin = False):
    for objeto_matriz in juego["objetos_a_mostrar"]:
        if "boton_matriz" in objeto_matriz["nombre"] and objeto_matriz["valor"] == respuesta_comodin[0]:
            objeto_matriz["color"] = (80, 110, 217)
        if "boton_matriz" in objeto_matriz["nombre"] and objeto_matriz["valor"] == respuesta_comodin[1]:
            objeto_matriz["color"] = (80, 110, 217)
        
        if tercer_comodin:
            if "boton_matriz" in objeto_matriz["nombre"] and objeto_matriz["valor"] == respuesta_comodin[0]:
                objeto_matriz["color"] = (80, 110, 217)
            if "boton_matriz" in objeto_matriz["nombre"] and objeto_matriz["valor"] == respuesta_comodin[1]:
                objeto_matriz["color"] = (227, 115, 39)
    pass



def grupo_acertado(juego,game,grupos_de_elementos):

    game["matriz_a_jugar"] = processor.ordenar_grupo_en_linea(game["matriz_a_jugar"], game["elecciones"], game["elementos_jugados"])
    game["puntuacion"] = points.sumar_puntuacion(game)
    
    core.generator(juego,game)
    pintar_lineas_acertadas(juego,game)
    
    game["elecciones"]=[]

    


def grupo_errado(juego,game,grupos_de_elementos):

    game["elecciones"]=[]
    game["puntuacion"] = points.perder_puntuacion(game)
    game["vidas"] = points.perder_vida(game["vidas"])
    if points.verificar_vidas(game["vidas"]) != True:
        game["reinicios"] = points.perder_vida(game["reinicios"])
        game["vidas"] = 3
        game["matriz_a_jugar"] = generar_nuevo_stage(grupos_de_elementos, game["elementos_jugados"],True)
        if points.verificar_vidas(game["reinicios"]) != True:
            juego["pantalla_juego"] = False
            juego["pantalla_perder"] = True
    
    core.generator(juego,game)
    pintar_lineas_acertadas(juego,game)

    




def generar_nuevo_stage(grupos_de_elementos:list, grupos_jugados:list, repetir_jugados:bool = False)->list: 

    if repetir_jugados:
        
        lista_auxiliar=[]
        stage = processor.separar_grupos(grupos_jugados, lista_auxiliar)
        stage = processor.desordenar_grupos(stage)
    else:
        stage = processor.separar_grupos(grupos_de_elementos, grupos_jugados)
        stage = processor.desordenar_grupos(stage)

    return stage

def pintar_lineas_acertadas(juego,game):

    for i in range(len(game["matriz_a_jugar"])-1):
        if processor.comprobar_grupo(game["matriz_a_jugar"][i],game["elementos_jugados"]):   
            for objeto_matriz in juego["objetos_a_mostrar"]:

                if "boton_matriz" in objeto_matriz["nombre"] and objeto_matriz["valor"] in game["matriz_a_jugar"][i]:
                    objeto_matriz["ordenado"] =True
                    objeto_matriz["color"] = (42, 222, 40)

                if  set(game["elecciones"]) == set(game["matriz_a_jugar"][3]):

                    objeto_matriz["ordenado"] =True
                    objeto_matriz["color"] = (42, 222, 40)
        else:
            break

def manejar_elecciones(juego,game,grupos_de_elementos):
    if len(game["elecciones"]) == 4:
        if processor.comprobar_grupo(game["elecciones"],game["elementos_jugados"]):
            grupo_acertado(juego,game,grupos_de_elementos)
            if processor.comprobar_stage(juego,game,grupos_de_elementos):
                core.generator(juego,game)
                                    
        else:
            grupo_errado(juego,game,grupos_de_elementos)



        


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
