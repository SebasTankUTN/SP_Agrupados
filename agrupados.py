import random
from funciones_generales import*


def separar_grupos(lista_grupos:list, grupos_jugados:list) -> list:

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

    nueva_matriz = crear_matriz("",4,4)

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            nueva_matriz[i][j] = matriz[j][i]
        
        nueva_matriz[i] = desordenar_vector(nueva_matriz[i])
        

    return nueva_matriz


def comprobar_grupo(elecciones:list, lista_jugados:list) -> bool:
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
    bandera = True
    for linea in matriz_elementos:
        if comprobar_grupo(linea, lista_jugados)!=True:
            bandera = False
    return bandera
    


