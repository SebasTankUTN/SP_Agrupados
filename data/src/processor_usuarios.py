import data.src.loader_usuarios as load
import data.procesamiento_usuarios as datos

def encontrar_elemento(valor,posicion,ubicacion ):
    
    datos = load.cargar_archivo_json("data/archivos_usuarios.json","r")
    listado = datos[ubicacion]
    
    estado = False
    for i in range(len(listado)):
        if listado[i][posicion] == valor:
            estado = True
    
    return estado

def encontrar_id(nombre_usuario, ubicacion, valor):
    datos = load.cargar_archivo_json("data/archivos_usuarios.json","r")
    listado = datos[ubicacion]
    
    for i in range(len(listado)):
        if listado[i]['usuario'] == nombre_usuario:
            id_usuario = listado[i][valor]
    
    return id_usuario

def ingreso_usuario(mensaje: dict):
    listado = []
    
    
        
    
    nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)
    while encontrar_elemento(nombre_usuario,'usuario', 'lista_usuarios') != False:
            print("Usuario no disponible, Ingrese otro .... ")
            nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)


    valor_password = load.get_string(mensaje['mensaje_password'], mensaje["mensaje_error"], load.validacion_string)
    
    id_usuario = load.generar_id()
    while encontrar_elemento(id_usuario,'id', 'lista_usuarios') != False:
            id_usuario = load.generar_id()

    listado = [nombre_usuario,valor_password,id_usuario]

    return listado

def inicio_sesion(mensaje: dict):
    listado = []

    nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)
    valor_password = load.get_string(mensaje['mensaje_password'], mensaje["mensaje_error"], load.validacion_string)
    password_usuario = encontrar_id(nombre_usuario, 'lista_usuarios', 'password')
    
    while encontrar_elemento(nombre_usuario, 'usuario', 'lista_usuarios') !=True or password_usuario != valor_password:
        print("Datos Ingresados Incorrectos, Ingrese Correctamente")
        nombre_usuario = load.get_string(mensaje['mensaje_usuario'], mensaje["mensaje_error"], load.validacion_string)
        valor_password = load.get_string(mensaje['mensaje_password'], mensaje["mensaje_error"], load.validacion_string)
        password_usuario = encontrar_id(nombre_usuario, 'lista_usuarios', 'password')

    id_usuario = encontrar_id(nombre_usuario,"lista_usuarios","id")

    listado = [nombre_usuario,valor_password,id_usuario]

    return listado

def archivo_usuario(listado: dict):

    lista = ingreso_usuario(datos.mensaje)

    listado['usuario'] = lista[0]
    listado['password'] = lista[1]
    listado['id'] = lista[2]

    return listado


def archivo_estadisticas(listado: dict, game: dict, lista: list):

    listado['id'] = lista[2]
    listado['nivel'] = game['nivel']
    listado['stage'] = game['stage']
    listado['vidas'] = game['vidas']
    listado['puntuacion'] = game['puntuacion']
    listado['reinicios'] = game['reinicios']

    return listado