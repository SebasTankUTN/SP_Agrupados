from ..data.show import *

def perder_vida(vidas: int, mostrar = True):
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




def puntuacion_nivel(reinicios: int, vidas: int, valor_1: int, valor_2: int, valor_3: int, valor_4: int)-> int:
    
    valor_puntuacion = 0

    if reinicios > 2:
        if vidas == 3:
            valor_puntuacion = valor_1
        else:
            valor_puntuacion = valor_2
    else:
        if vidas == 3:
            valor_puntuacion = valor_3
        else:
            valor_puntuacion = valor_4
    
    return valor_puntuacion
            
def estado_puntuacion(puntuacion: int):

    if puntuacion < 0:
        puntuacion = 0
    
    return puntuacion



def sumar_puntuacion(puntuacion: int, nivel: int, vidas: int, reinicios: int)-> int:
    
    suma_puntuacion = 0
    puntuacion = estado_puntuacion(puntuacion)

    match nivel:
        case 1:
            suma_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 30, valor_2 = 15, valor_3 = 22, valor_4 = 8)

        case 2:
            suma_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 50, valor_2 = 25, valor_3 = 35, valor_4 = 15)
        
        case 3:
            suma_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 75, valor_2 = 35, valor_3 = 50, valor_4 = 21)

        case 4:
            suma_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 100, valor_2 = 80, valor_3 = 85, valor_4 = 80)
        
        case 5:
            suma_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 150, valor_2 = 100, valor_3 = 120, valor_4 = 75)


    return puntuacion + suma_puntuacion

def perder_puntuacion(puntuacion: int, nivel: int, reinicios: int, vidas: int)-> int:
    resta_puntuacion = 0
    

    if puntuacion > 0:
        match nivel:
            case 1:
                resta_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 16, valor_2 = 20, valor_3 = 14, valor_4 = 18)

            case 2:
                resta_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 14, valor_2 = 18, valor_3 = 12, valor_4 = 16)

            case 3:
                resta_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 10, valor_2 = 14, valor_3 = 8, valor_4 = 12)

            case 4:
                resta_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 7, valor_2 = 11, valor_3 = 6, valor_4 = 10)

            case 5:
                resta_puntuacion = puntuacion_nivel(reinicios, vidas,valor_1 = 4, valor_2 = 8, valor_3 = 3, valor_4 = 5)
    else:
        resta_puntuacion = 0
    
    puntuacion-=resta_puntuacion
    puntuacion = estado_puntuacion(puntuacion)
    
    return puntuacion