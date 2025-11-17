
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
        "reinicios" : 3,
        "puntuacion" : 0
    }
    return game
