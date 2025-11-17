import random
from ..data.loader import *

def comprobar_elementos_en_lista(lista:list, elemento:any):
    """Comprueba si el elemento se encuentra en la lista

    Args:
        lista (list): vector a recorrer
        elemento (any): valor a encontrar

    Returns:
        _bool_: devuelve True si lo encontro.
                devuelve False no lo encontro.
    """
    bandera = False
    if elemento in lista:

        bandera = True

    return bandera

def desordenar_vector(vector:list) -> list:
    """recorrer un vector y utiliza el modulo random para intercambiar los valores de forma aleatoria con los elemento desordenados.
    Args:
        vector (list): Vector cuyos elemento estaran desordenados.

    Returns:
        list: _devuelve una nueva lista desordenada con elemento ubicados en un orden aleatoria
    """
    for i in range(len(vector)):

            posicion_aleatoria = random.randint(0,len(vector)-1)
            
            vector[i] , vector[posicion_aleatoria] = vector[posicion_aleatoria], vector[i]

    return vector


def separar_grupos(lista_grupos:list, grupos_jugados:list) -> list:
    """Asigna de forma aleatorio 4 grupo de  4 elementos cada uno a una matriz,verificar 
        Si se encuentran grupos repetidos, si se llega dar ese caso, se cambiar el grupo repetido
       y se reemplazar por otro que no pertenezcan a la matriz.

        Args:
        lista_grupos (list): Lista que contiene todos elementos que estan disponible para la matriz
        grupos_jugados (list): Lista de grupos que se utilizara para evitar las repeticiones.  

    Returns:
        list: devuelve la matriz con todos los elementos de cada grupo en una distanta fila.
    """
    matriz = []
    for i in range (0,4):

        numero_aleatorio = random.randint(0, len(lista_grupos) - 1)

        while comprobar_elementos_en_lista(grupos_jugados, lista_grupos[numero_aleatorio]):
            numero_aleatorio = random.randint(0, len(lista_grupos) - 1)

    
        grupos_jugados += [lista_grupos[numero_aleatorio]]

        lista_elementos = lista_grupos[numero_aleatorio]["elementos"]

        matriz += [lista_elementos]
    
    return matriz

def desordenar_grupos(matriz:list) -> list:
    """Recorre una matriz y desordenar aleatoriamente cada elemento de la matriz

    Args:
        matriz (list): Lista de lista que contiene los valores a desordenar.

    Returns:
        list: Una nueva matriz que contiene todos los elementos desordenados de manera aleatoria.
    """
    nueva_matriz = crear_matriz("",4,4)

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            nueva_matriz[i][j] = matriz[j][i]
        
        nueva_matriz[i] = desordenar_vector(nueva_matriz[i])
        

    return nueva_matriz


def comprobar_grupo(elecciones:list, lista_jugados:list) -> bool:
    """Comprueba si Los elementos elegidos por el usuario coinciden con algun grupo original
    previamente establecido.

    Args:
        elecciones (list): Lista con los elemento que ingreso el usuario.
        lista_jugados (list): lista que contiene todos los elementos de cada grupo de forma correcta.

    Returns:
        bool: Si es true, Todos los elementos coinciden con el mismo grupo.
            Si es false, Todos los elementos no coinciden con el mismo grupo.
    """
    bandera = False

    for grupo in lista_jugados:

        for i in range(len(elecciones)):
            if comprobar_elementos_en_lista( grupo["elementos"], elecciones[i] ):
                if i == 3:
                    bandera = True
                    break
            else:
                break
    return bandera

def ordenar_grupo_en_linea(matriz_elementos:list, vector_a_acomodar:list, lista_jugados:list) -> list:
    """Ordenar las elecciones del usuario si se realizo de forma correcta. Los grupos restantes se
    reorganizaran en las filas disponibles.

    Args:
        matriz_elementos (list): Matriz lista de lista con los elementos que estan utilizando en la partida.
        vector_a_acomodar (list): Lista que contiene las elecciones del usuario
        lista_jugados (list): Lista con los grupos originales utilizados para verificar la validez
        de las elecciones.

    Returns:
        list: matriz actualizada que contiene las elecciones correctas del usuario y lo que queda lo organizar 
        con las filas restantes.
    """
    bandera_acomodado = False
    vector_auxiliar=[]

    for i in range(len(matriz_elementos)):
        if comprobar_grupo(matriz_elementos[i], lista_jugados)!= True:
            if bandera_acomodado == False:
                
                for j in range(len(matriz_elementos[i])):
                    if matriz_elementos[i][j] not in vector_a_acomodar:
                        vector_auxiliar += [matriz_elementos[i][j]]

                matriz_elementos[i] = vector_a_acomodar
                bandera_acomodado = True
        
            if matriz_elementos[i] != vector_a_acomodar:
                for j in range(len(matriz_elementos[i])):                    
                    if matriz_elementos[i][j] in vector_a_acomodar:
                        
                        matriz_elementos[i][j] = vector_auxiliar[0]
                        vector_auxiliar.pop(0)
                        
    return matriz_elementos

def comprobar_stage(matriz_elementos:list, lista_jugados:list) -> bool:
    """Comprueba si la matriz de grupos contiene algun grupo repetido.
    en el caso de que haya alguno, se reemplazar por otro grupo no repetido.

    Args:
        matriz_elementos (list): Lista de listas con los grupos que se estan utilizando en la partida
        lista_jugados (list): Listas de listas que llevan un registro de los grupos jugados para evitar
        repeticiones

    Returns:
        bool: Si es true, Ninguno grupo se repite
              Si es False, los grupos se repiten.
    """
    bandera = True
    
    for i in range(len(matriz_elementos)):
        if comprobar_grupo(matriz_elementos[i], lista_jugados)!=True:
            bandera = False
    
    return bandera

