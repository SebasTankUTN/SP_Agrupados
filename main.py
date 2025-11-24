from data.procesamiento_partidas import *
import src.core.engine as engine
import src.data.show as show
import src.data.loader as datos
import data.src.processor_usuarios as load
import data.engine_user as up
import data.src.loader_usuarios as down


mensaje = datos.init_mensaje_juego()
plantilla_usuario = datos.init_dict_usuario()
planilla_stast = datos.init_dict_estadisticas()
estado_json = down.validar_json('lista_usuarios')


sesion_iniciada = False
salir=True
while salir:

    Menu_Juego = datos.get_string(mensaje['msj_menu_opcion'], mensaje['msj_menu_error'], 52, datos.validar_numeros)
    match Menu_Juego:
        case '1':
            estado_json = down.validar_json('lista_usuarios')
            if estado_json == False:
                print("NO HAY DATOS REGISTRADOS, Registre UN USUARIO.")
            
            if sesion_iniciada == False and estado_json == True:
                usuario = load.inicio_sesion(mensaje)
                sesion_iniciada = True
        case '2':
            if sesion_iniciada == True:
                print(usuario)
                game = datos.init_game_values()
                grupos_de_elementos = cargar_elementos('data/archivo_partidas.csv')
                engine.jugar_agrupados(game, grupos_de_elementos)
                up.cargar_estadisticas(planilla_stast, usuario, game)
            else:
                print("Sesion no iniciada.")
        case '3':
            up.cargar_usuario(mensaje)
        case '4':
            salir = False