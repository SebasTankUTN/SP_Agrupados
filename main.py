from data.procesamiento_partidas import *
import src.core.engine as engine
import src.data.show as show
import src.data.loader as datos
import data.src.processor_usuarios as load
import data.procesamiento_usuarios as up
import data.src.loader_usuarios as down

game = datos.init_game_values()
grupos_de_elementos = cargar_elementos('data/archivo_partidas.csv')
mensaje = datos.init_mensaje_juego()
plantilla_usuario = datos.init_dict_usuario()
planilla_stast = datos.init_dict_estadisticas()
estado_json = down.validar_json('lista_usuarios')

salir=True
while salir:

    Menu_Juego = datos.get_string(mensaje['msj_menu_opcion'],mensaje['msj_menu_error'],datos.validar_numeros)
    match Menu_Juego:
        case '1':
            if estado_json == False:
                print("NO HAY DATOS REGISTRADOS, Registre UN USUARIO.")
            else:
                usuario = load.inicio_sesion(mensaje)
                engine.jugar_agrupados(game, grupos_de_elementos)
                up.cargar_estadisticas(planilla_stast, usuario, game)
        case '2':
            up.cargar_usuario(plantilla_usuario)
        case '3':
            break

    # game = engine.jugar_agrupados(game, grupos_de_elementos)

    condicional=input("salir: a, sino apreta enter: ")
    if condicional == "a":
        salir = False