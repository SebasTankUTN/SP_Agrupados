import random


#toma un dato, lo manda a fijarse si es un numero, recien cuando lo confirma lo parcea y 
# lo manda a validar

def get_int (mensaje:str,minimo:int,maximo:int):
    numero_int = input(mensaje)
    while es_numero(numero_int) !=True:
        numero_int = input(mensaje)
    numero_int = int(numero_int)
    
    while validacion_entero (minimo, maximo, numero_int) !=True:
        numero_int = input(mensaje)
        while es_numero(numero_int) !=True:
            numero_int = input(mensaje)
        numero_int = int(numero_int)
    return numero_int

#verifica si la matriz esta cargada con algun valor que no sea 0
def verificar_matriz_cargada(matriz:list):
    bandera = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] !=0:
                bandera = True
                break
    return bandera


#toma un float
def get_float (mensaje):
    numero_float = float(input(mensaje))
    return numero_float

#toma un dato y lo manda a validar 
def get_string (mensaje, lista:list):
    ingreso_cadena = input(mensaje)
    while validacion_string(lista, ingreso_cadena) !=True:
        ingreso_cadena = input(mensaje)
    return ingreso_cadena

#agarra un valor y lo compara con el minimo y el maximo
def validacion_entero (minimo:int,maximo:int,numero:int):
    respuesta = False

    if numero >= minimo and numero <= maximo:
        respuesta = True
        
    return respuesta

#valida que un dato este dentro de la lista de cadenas aceptadas
def validacion_string (lista: list, dato: str):
    respuesta = False
    for i in range(len(lista)):
        if lista[i].lower() == dato.lower():
            respuesta = True
            break
    return respuesta

#busca un dato dentro de una lista y devuelve la posicion
def obtener_posicion_lista(lista:list, dato:str):
    for i in range(len(lista)):
        if lista[i].lower() == dato.lower():
            respuesta = i
            break
    return respuesta

#revisa que una cadena de texto tenga todos sus valores dentro de los ascii de numeros
def es_numero(numero:str):
    bandera=True
    for i in range(len(numero)):
        if ord(numero[i]) > 57 or ord(numero[i]) < 48:
            bandera = False
            break
    return bandera

#crea un vector con las posiciones ingresadas y las inicializa
def crear_vector(cantidad_filas:int,valor:any):
    vector = [valor]*cantidad_filas
    return vector

#recorre un vector y lo muestra, si ingresa 2 los muestra juntos
def mostrar_vector(vector:list,vector2:list=False, muestreo_doble:bool=False):
    if muestreo_doble:
        for i in range(len(vector)):
            print(f"{vector[i]}: { vector2[i]}")
    else:
        for i in range(len(vector)):
            print(vector[i])

#recorre la matriz y muestra cada valor, los muestra por fila y separa las columnas con |
def mostrar_matriz (matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}",end=' | ')
        print()

#crea una matriz con un valor iniciado y columnas por la cantidad de filas
def crear_matriz (ingreso:any,cantidad_columna:int,cantidad_filas:int):
    lista_matriz = [[ingreso] * cantidad_columna for _ in range(cantidad_filas)]
    return lista_matriz

#recorre un vector, suma todos sus valores y devuelve el acumulado
def acumulador_de_vector(vector:list):
    acumulador=0
    for i in range(len(vector)):
        acumulador+=vector[i]
    return acumulador

#recorre un vector y guarda el mayor valor que encontro y su posicion, devuelve otro vector con esos datos

def encontrar_mayor_en_vector(vector:list):
    mayor=crear_vector(2,0)
    for i in range(len(vector)):
        if mayor[1] < vector[i] or mayor[1] == 0:
            mayor[1] = vector[i]
            mayor[0] = i
    return mayor

def separar_str(cadena:str, separacion)->list:
    primer_tramo = False
    for i in range (len(cadena)):
        
        if ord(cadena[i]) == ord(separacion):

            primer_tramo = "" 
            for j in range(i):
                primer_tramo += cadena[j]

            segundo_tramo = ""
            for j in range(i + 1,len(cadena) ):
                segundo_tramo += cadena[j]
            break   

    if primer_tramo:
        lista = [primer_tramo,segundo_tramo]
    else: 
        lista = cadena + " no se pudo hacer split por busqueda inexistente"

    return lista

def mostrar_set(mi_set):

    for valor in mi_set:
        print(f"{valor}")


def desordenar_vector(vector:list) -> list:

    for i in range(len(vector)):

            posicion_aleatoria = random.randint(0,len(vector)-1)
            
            vector[i] , vector[posicion_aleatoria] = vector[posicion_aleatoria], vector[i]

    return vector

def comprobar_elementos_en_lista(lista:list, elemento:any):
    
    bandera = False
    if elemento in lista:

        bandera = True

    return bandera

def perder_vida(vidas: int, mostrar = True):
    vidas -=1

    if mostrar ==True:
        mostrar_vidas(vidas)
    
    return vidas

def reinicio_nivel(reinicio: int, vidas :int):

    reinicio -=1
    
    if reinicio == 0:
        print("No te quedan reinicios")
    else:
        print(f'Reiniciando Nivel, Te quedan {reinicio} reinicios')
        vidas = 3
        print(f"Nivel Restaurado, Vidas Restantes {vidas}")
        

    return reinicio, vidas

def verificar_vidas(vida: int):
    estado = False
    
    if vida > 0:
        estado = True

    return estado

def verificar_reinicio(reinicio: int):
    estado = False
    
    if reinicio > 0:
        estado = True

    return estado 

def mostrar_vidas(vidas:int):
    
    if vidas >=1:
        print(f"Perdiste una vida, te quedan {vidas} vidas")
    else:
        print(f'Te quedas sin vidas. Reinicio Nivel')