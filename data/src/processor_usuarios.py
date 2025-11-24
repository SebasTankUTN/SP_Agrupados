import data.src.loader_usuarios as load
import data.engine_user as datos

def encontrar_elemento(valor,posicion,ubicacion ):
    
    listado = load.cargar_archivo_json("data/archivos_usuarios.json","r")
    lista_filtrada = listado[ubicacion]
    
    estado = False
    for i in range(len(lista_filtrada)):
        if lista_filtrada[i][posicion] == valor:
            estado = True
    
    return estado

def encontrar_id(nombre_usuario, ubicacion, valor):
    listado = load.cargar_archivo_json("data/archivos_usuarios.json","r")
    lista_filtrada = listado[ubicacion]
    
    for i in range(len(lista_filtrada)):
        if lista_filtrada[i]['usuario'] == nombre_usuario:
            id_usuario = lista_filtrada[i][valor]
            break
        else:
             id_usuario = None
    
    return id_usuario

def ingreso_usuario(mensaje: dict):
    datos_usuario = dict()
    
    nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)
    while encontrar_elemento(nombre_usuario,'usuario', 'lista_usuarios') != False:
            print("Usuario no disponible, Ingrese otro .... ")
            nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)


    valor_contrasena = load.get_string(mensaje['mensaje_password'], mensaje["mensaje_error"], load.validacion_string)
    
    id_usuario = load.generar_id()
    while encontrar_elemento(id_usuario,'id', 'lista_usuarios') != False:
            id_usuario = load.generar_id()

    datos_usuario = {"usuario": nombre_usuario,"contrasena":valor_contrasena,"id":id_usuario}
    print('REGISTRO EXITOSO')

    return datos_usuario

def inicio_sesion(mensaje: dict):
    datos_usuario = dict()

    nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)
    valor_contrasena = load.get_string(mensaje['mensaje_password'], mensaje["mensaje_error"], load.validacion_string)
    contrasena_origen = encontrar_id(nombre_usuario, 'lista_usuarios', 'contrasena')
    
    while encontrar_elemento(nombre_usuario, 'usuario', 'lista_usuarios') !=True or contrasena_origen != valor_contrasena:
        print("Datos Ingresados Incorrectos, Ingrese Correctamente")
        nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)
        valor_contrasena = load.get_string(mensaje['mensaje_password'], mensaje["mensaje_error"], load.validacion_string)
        contrasena_origen = encontrar_id(nombre_usuario, 'lista_usuarios', 'contrasena')

    id_usuario = encontrar_id(nombre_usuario,"lista_usuarios","id")

    datos_usuario = {"usuario": nombre_usuario,"contrasena":valor_contrasena,"id":id_usuario}
    print("Inicio de sesion exitosa.")

    return datos_usuario




def archivo_estadisticas(listado: dict, game: dict, lista: list):

    listado['id'] = lista["id"]
    listado['nivel'] = game['nivel']
    listado['stage'] = game['stage']
    listado['vidas'] = game['vidas']
    listado['puntuacion'] = game['puntuacion']
    listado['reinicios'] = game['reinicios']
    listado["errores"] = game["errores"]

    return listado