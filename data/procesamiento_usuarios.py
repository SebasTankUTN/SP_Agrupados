import src.data.loader as load
import data.src.loader_usuarios as up
import data.src.processor_usuarios as process

listado_usuario = load.init_dict_usuario()
game = load.init_game_values()
listado_estadisticas = load.init_dict_estadisticas()
mensaje = load.init_mensaje_juego()


def cargar_usuario(listado):

    datos = up.cargar_archivo_json("data/archivos_usuarios.json","r")

    usuario = process.archivo_usuario(listado)
    datos["lista_usuarios"] += [usuario]
    
    up.guardar_json("data/archivos_usuarios.json",datos)

    return usuario

def cargar_estadisticas(listado,usuarios,game):
    
    datos = up.cargar_archivo_json("data/archivos_usuarios.json","r")

    estadisticas = process.archivo_estadisticas(listado,game,usuarios)
    datos["lista_estadisticas"] +=[estadisticas]

    up.guardar_json("data/archivos_usuarios.json",datos)

# usuarios = cargar_usuario(listado_usuario)

# cargar_estadisticas(listado_estadisticas,usuarios,game)
