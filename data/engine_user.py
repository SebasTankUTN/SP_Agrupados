import src.data.loader as load
import data.src.loader_usuarios as up
import data.src.processor_usuarios as process
import src.data.show as show

listado_usuario = load.init_dict_usuario()
game = load.init_game_values()
listado_estadisticas = load.init_dict_estadisticas()
mensaje = load.init_mensaje_juego()


def cargar_usuario(mensaje):

    listado_archivo = up.cargar_archivo_json("data/archivos_usuarios.json","r")

    usuario = process.ingreso_usuario(mensaje)
    listado_archivo["lista_usuarios"] += [usuario]
    
    up.guardar_json("data/archivos_usuarios.json",listado_archivo)

    return usuario

def cargar_estadisticas(listado,usuarios,game):
    
    listado_archivo = up.cargar_archivo_json("data/archivos_usuarios.json","r")

    estadisticas = process.archivo_estadisticas(listado,game,usuarios)
    listado_archivo["lista_estadisticas"] +=[estadisticas]

    up.guardar_json("data/archivos_usuarios.json",listado_archivo)

    show.mostrar_estadisticas(estadisticas)
    

# usuarios = cargar_usuario(listado_usuario)

# cargar_estadisticas(listado_estadisticas,usuarios,game)
