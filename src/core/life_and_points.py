from ..data.show import *

def perder_vida(vidas: int, mostrar = False):
    """descuenta el valor de vidas a -1 y muestrar la cantidad de vidas que tiene.

    Args:
        vidas (int): numero entero utilizado para el descuento
        mostrar (bool, optional):   Si es True muestra la cantidad de vida que tendra. Defaults to True.
                                    Si es False no muestrar ningun dato.
    Returns:
        _int_: Devuelve la cantidad de vida que tendra.
    """
    vidas -=1

    if mostrar ==True:
        mostrar_vidas(vidas)
    
    return vidas

def verificar_reinicios(reinicio: int, vidas :int):
    """descuenta el valor de reinicios y actualizar el valor de vidas a 3.

    Args:
        reinicio (int): valor a descontar
        vidas (int): Valor a actualizar

    Returns:
        _list_: devuelve dos valores enteros en un diccionario cumpliendo con sus condiciones establecidas.
    """
    lista_valores = {}
    reinicio -=1
    
    if reinicio == 0:
        print("No te quedan reinicios")
    else:
        print(f'Te quedan {reinicio} reinicios')
        vidas = 3
        print(f"Nivel Restaurado, Vidas Restantes 3/{vidas}")
    
    lista_valores = {
        "valor_reinicios": reinicio, 
        "valor_vidas": vidas
    }

    return lista_valores

def verificar_vidas(vida: int):
    """Verificar el estado del valor vidas.

    Args:
        vidas (int): numero entero a analizar

    Returns:
        _bool_: devuelve un booleano si el valor se encuentra en las condiciones establecidas
    """
    estado = False
    
    if vida > 0:
        estado = True

    return estado

def verificar_reinicio(reinicio: int):
    """Verificar el estado del valor reinicio.

    Args:
        reinicio (int): numero entero a analizar

    Returns:
        _bool_: devuelve un booleano si el valor se encuentra en las condiciones establecidas
    """
    estado = False
    
    if reinicio > 0:
        estado = True

    return estado 




def calcular_puntuacion(game: dict, calculo = True):
    
    puntuacion_base = 5

    if calculo:
        puntuacion = puntuacion_base * game['reinicios'] + game['vidas'] * game['nivel']# Suma

    else:
        puntuacion = puntuacion_base * game['reinicios'] + game['vidas']  #Resta

    return puntuacion
        
def valida_puntuacion(game: dict):

    if game['puntuacion'] < 0:
        game['puntuacion'] = 0
    
    return game['puntuacion']



def sumar_puntuacion(game: dict)-> int:
    
    game['puntuacion'] += calcular_puntuacion(game)

    return game['puntuacion']


def perder_puntuacion(game: dict)-> int:

    game['puntuacion'] -= calcular_puntuacion(game, calculo=False)

    game['puntuacion'] = valida_puntuacion(game)

    return game['puntuacion']