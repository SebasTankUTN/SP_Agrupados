def vector(vector:list,vector2:list=False, muestreo_doble:bool=False):
    """Recorre un vector y lo muestra, si ingresa 2 vectores lo mostrara juntos.

    Args:
        vector (list): Vector a mostrar
        vector2 (list, optional): Si es false, se tiene que ingresar un segundo vector
        muestreo_doble (bool, optional): Si es False, mostrara los 2 vectores ingresado.
                                         Si es True, muestra solamente el primer vector.
    """
    if muestreo_doble:
        for i in range(len(vector)):
            print(f"{vector[i]}: { vector2[i]}")
    else:
        for i in range(len(vector)):
            print(vector[i])

def matriz (matriz:list):
    """recorrer la matriz y muestra cada valor de la misma.

    Args:
        matriz (list): Lista a mostrar al usuario.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:20}",end=' | ', )
        print()

def mostrar_vidas(vidas:int):
    """Muestrar los valores de un valor

    Args:
        vidas (int): Valor a mostrar
    """
    if vidas >=1:
        print(f"Perdiste una vida, {vidas}/3 vidas")
    else:
        print(f'Te quedaste sin vidas.')

def mostrar_estadisticas(lista: dict):

    print("======Estadisticas GAME OVER======")
    print(f"ID: {lista["id"]}")
    print(f"Nivel: {lista["nivel"]}")
    print(f"Stage: {lista["stage"]}")
    print(f"Vidas: {lista["vidas"]}")
    print(f"Reinicios: {lista["reinicios"]}")
    print(f"Puntuacion: {lista["puntuacion"]}")
    print(f"Errores: {lista["errores"]}")
    print("==================================")