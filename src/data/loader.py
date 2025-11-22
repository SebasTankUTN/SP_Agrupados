from ..data.processor import * 
from ..core.life_and_points import *
from data.procesamiento_partidas import *
import src.core.engine as engine

def crear_matriz (ingreso:any,cantidad_columna:int,cantidad_filas:int):
    """Crear una matriz con un valor determinado y columnas por la cantidad de filas
    Args:
        ingreso (any): Valor que se ingresa en la matriz
        cantidad_columna (int): Numero entero que contendra la cantidad de columnas que tendra la matriz.
        cantidad_filas (int): Numero entero que contendra la cantidad de filas que tendra la matriz.

    Returns:
        _list_: devuelve una matriz con el valor determinado y con la cantidad de filas y columnas correspondida.
    """
    lista_matriz = [[ingreso] * cantidad_columna for _ in range(cantidad_filas)]
    
    return lista_matriz

def validar_numeros(cadena: str)->bool:
    """Se le ingresa una cadena y verificar con codigo ascii si pertenece desde un numero hasta otro numero.

    Args:
        cadena (str): La entrada de datos que se ingreso
    Returns:
        bool: Devuelve True si pertenece dentro de una medicion y False si no le pertenece.
    """
    encontro = False
    if len(cadena) == 1:
        numero = ord(cadena)
        if numero >= 49 and numero <= 51:
            encontro = True

    return encontro

def get_string(mensaje:str, mensaje_error: str, funcion):

    cadena = input(mensaje)
    while funcion(cadena) != True:
        print(mensaje_error)
        cadena = input(mensaje)

    return cadena


def tomar_valores(cantidad_valores:int):
    
    lista_valores = crear_vector(cantidad_valores,any)

    for i in range(len(lista_valores)):
        lista_valores[i] = input('Ingrese su eleccion: ')

    return lista_valores



def crear_vector(cantidad_filas:int,valor:any):
    """Realizar la creacion de un vector.

    Args:
        cantidad_filas (int): Numero entero para indicar la cantidad de filas que tendra.
        valor (any): Valor que contiene el vector en cada fila.

    Returns:
        _List_: devuelve una lista con la cantidad de filas y del valor indicado.
    """
    vector = [valor]*cantidad_filas
    
    return vector

def init_game_values():
    
    game ={
        "elementos_jugados": [],
        "matriz_a_jugar": [],
        "nivel" : 1,
        "stage" : 1,
        "vidas" : 3,
        "reinicios" : 2,
        "puntuacion" : 0,
        "errores": 0
    }
    return game

def init_dict_usuario():
    
    listado_usuario = {
        "usuario":str(),
        "password":str(),
        "id":int()
    }
    
    return listado_usuario

def init_dict_estadisticas():

    lista_estadisticas = {
            "id" : int(),
            "nivel" : int(),
            "stage" : int(),
            "vidas" : int(),
            "reinicios" : int(),
            "puntuacion" : int(),
            "errores": int()
    }
    return lista_estadisticas

def init_mensaje_juego():

    mensaje = {
        'mensaje_usuario': 'Ingrese su usuario: ',
        'mensaje_password': 'Ingrese su contraseña: ',
        'registro_usuario': 'Ingrese un usuario: ',
        'registro_password': 'Ingrese una contraseña',
        'mensaje_error': 'El valor ingresado debe contener entre 1 - 15 characteres. ',
        'usuario_disponible': 'Usuario no disponible',
        'msj_menu_opcion': '\n1-Iniciar Sesion\n2-Registrarse\n3-Salir\n\nEliga Una Opcion(1 - 3): ',
        'msj_menu_error': 'El valor ingresado debe ser entre 1 - 3',
        'msj_menu_juego': '\n1-Jugar Agrupados\n2-Salir\n\nEliga Una Opcion(1 - 2): ',
        'msj_submenu_error': 'El valor ingresado debe ser entre 1 - 2'
    }
    return mensaje

