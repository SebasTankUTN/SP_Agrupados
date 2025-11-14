import random




def get_int (mensaje:str,minimo:int,maximo:int):
    """Solicitar al usuario una cadena numerica, verificar si es valida, lo parcea a
    numero entero y controla que se encuentre dentro del rango permitido.

    Args:
        mensaje (str): Texto que se le muestra al usuario para solicitar informacion
        minimo (int): valor minimo permitido para la validacion
        maximo (int): valor maximo permitido para la validacion

    Returns:
        _int_: Numero entero ingresado por el usuario cumpliendo las condiciones establecidas.
    """
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
    """Verifica si la matriz esta cargada con algun valor que no sea 0

    Args:
        matriz (list): Matriz(lista de listas) a analizar

    Returns:
        _bool_: devuelve false si se encuentra 0.
                devuelve True si no encontro 0.
     """         
    bandera = False
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] !=0:
                bandera = True
                break
    
    return bandera


#toma un float
def get_float (mensaje: str):
    """Le solicitar al usuario un valor flotante

    Args:
        mensaje (_str_): Texto que se le muestra al usuario para solicitar informacion  

    Returns:
        _float_: Numero flotante ingresado por el usuario cumpliendo las condiciones establecidas.
    """
    numero_float = float(input(mensaje))
    
    return numero_float

#toma un dato y lo manda a validar 
def get_string (mensaje: str, lista: list):
    """Solicitar al usuario una cadena de texto y lo valida segun los valores permitidos.

    Args:
        mensaje (_str_): Texto que se le muestra al usuario para solicitar la entrada.
        lista (list): vector utilizado para la validacion

    Returns:
        _str_: devuelve la cadena de texto ingresada por el usuario cumpliendo con las condiciones establecidas.
    """
    ingreso_cadena = input(mensaje)
    while validacion_string(lista, ingreso_cadena) !=True:
        ingreso_cadena = input(mensaje)
    return ingreso_cadena

#agarra un valor y lo compara con el minimo y el maximo
def validacion_entero (minimo:int,maximo:int,numero:int):
    """Verificar si un numero entero cumple con las condiciones minima y maximas establecidas.

    Args:
        minimo (int): Valor minimo permitido para validacion
        maximo (int): Valor maximo permitido para validacion
        numero (int): Valor entero que se desea validar.

    Returns:
        _bool_: Si es true, El valor ingresado cumple entre el minimo y maximo.
                Si es False, el valor ingresado no cumple entre el minimo y maximo.
    """
    respuesta = False

    if numero >= minimo and numero <= maximo:
        respuesta = True
        
    return respuesta

#valida que un dato este dentro de la lista de cadenas aceptadas
def validacion_string (lista: list, dato: str):
    """Valida si la cadena de texto se encuentra dentro de la lista de valores.

    Args:
        lista (list): Lista de valores utilizados para la validacion.
        dato (str): Cadena de texto utilizada en la busqueda.

    Returns:
        _bool_: Si es True, el valor se encuentra en la lista de valores.
                Si es False, el valor no se encuentra en la lista de valores.
    """
    respuesta = False
    for i in range(len(lista)):
        if lista[i].lower() == dato.lower():
            respuesta = True
            break
    
    return respuesta

#busca un dato dentro de una lista y devuelve la posicion
def obtener_posicion_lista(lista:list, dato:str):
    """Buscar si la cadena de texto se encuentra en la lista y devuelve la posicion

    Args:
        lista (list): Lista de valores utilizados para la validacion
        dato (str): Cadena de texto utilizada en la busqueda.

    Returns:
        _int_: Devuelve La posicion en donde se encontro el valor en la lista.
    """
    for i in range(len(lista)):
        if lista[i].lower() == dato.lower():
            respuesta = i
            break
    
    return respuesta

#revisa que una cadena de texto tenga todos sus valores dentro de los ascii de numeros
def es_numero(numero:str):
    """Validar si la cadena de texto es una cadena unicamente de numeros con el codigo ascii

    Args:
        numero (str): Cadena texto utilizada para la validacion

    Returns:
        _bool_: Si es true es una cadena numerica.
                Si es false no es una cadena numerica.
    """         
    bandera=True
    
    for i in range(len(numero)):
        if ord(numero[i]) > 57 or ord(numero[i]) < 48:
            bandera = False
            break
    
    return bandera

#crea un vector con las posiciones ingresadas y las inicializa
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

#recorre un vector y lo muestra, si ingresa 2 los muestra juntos
def mostrar_vector(vector:list,vector2:list=False, muestreo_doble:bool=False):
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

#recorre la matriz y muestra cada valor, los muestra por fila y separa las columnas con |
def mostrar_matriz (matriz:list):
    """recorrer la matriz y muestra cada valor de la misma.

    Args:
        matriz (list): Lista a mostrar al usuario.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}",end=' | ')
        print()

#crea una matriz con un valor iniciado y columnas por la cantidad de filas
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

#recorre un vector, suma todos sus valores y devuelve el acumulado
def acumulador_de_vector(vector:list):
    """Recorre un vector, Suma todos sus valores y lo guarda.

    Args:
        vector (list): Lista de valores para la sumatoria.

    Returns:
        _int_: Devuelve el resultado de la suma todos los valores que tendra la lista de valores.
    """
    acumulador=0
    
    for i in range(len(vector)):
        acumulador+=vector[i]
    
    return acumulador

#recorre un vector y guarda el mayor valor que encontro y su posicion, devuelve otro vector con esos datos

def encontrar_mayor_en_vector(vector:list):
    """Recorre un vector y encuentra el valor mas alto
    Args:
        vector (list): Utilizada para buscar los valores del vector

    Returns:
        _list_: devuelva un vector con el valor mas alto y su posicion del vector utilizado
    """
    mayor=crear_vector(2,0)
    for i in range(len(vector)):
        if mayor[1] < vector[i] or mayor[1] == 0:
            mayor[1] = vector[i]
            mayor[0] = i
    return mayor

def separar_str(cadena:str, separacion: int)->list:
    """recibe una cadena de texto y lo separa en dos partes utilizando codigo ascii
    Args:
        cadena (str): cadena de texto a analizar
        separacion (int): utilizada en el codigo ascii que indica un nuevo string

    Returns:
        list: Devuelve las cadenas separadas en una lista.
    """
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
    """Muestra los valores de una coleccion

    Args:
        mi_set (_type_): utilizada para mostrar los valores
    """
    for valor in mi_set:
        print(f"{valor}")


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

def tomar_valores(cantidad_valores):
    
    lista_valores = crear_vector(cantidad_valores,any)

    for i in range(len(lista_valores)):
        lista_valores[i] = input('Ingrese su eleccion: ')

    return lista_valores     

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

def reinicio_nivel(reinicio: int, vidas :int):
    """descuenta el valor de reinicios y actualizar el valor de vidas a 3.

    Args:
        reinicio (int): valor a descontar
        vidas (int): Valor a actualizar

    Returns:
        _int_: devuelve dos valores enteros cumpliendo con sus condiciones establecidas.
    """
    reinicio -=1
    
    if reinicio == 0:
        print("No te quedan reinicios")
    else:
        print(f'Te quedan {reinicio} reinicios')
        vidas = 3
        print(f"Nivel Restaurado, Vidas Restantes 3/{vidas}")
        

    return reinicio, vidas

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

def mostrar_vidas(vidas:int):
    """Muestrar los valores de un valor

    Args:
        vidas (int): Valor a mostrar
    """
    if vidas >=1:
        print(f"Perdiste una vida, 3/{vidas} vidas")
    else:
        print(f'Te quedaste sin vidas.')

def sumar_puntuacion(nivel: int, vidas: int, reinicios: int)-> int:
    
    suma_puntuacion = 0

    match nivel:
        case 1:
            match reinicios:
                case 3:
                    if vidas == 3:
                        suma_puntuacion = 30
                    else:
                        suma_puntuacion = 15
                case 2:
                    if vidas == 3:
                        suma_puntuacion =22
                    else:
                        suma_puntuacion =8
        case 2:
            match reinicios:
                case 3:
                    if vidas == 3:
                        suma_puntuacion = 50
                    else:
                        suma_puntuacion = 25
                case 2,1:
                    if vidas == 3:
                        suma_puntuacion = 35
                    else:
                        suma_puntuacion = 15
        case 3:
            match reinicios:
                case 3:
                    if vidas == 3:
                        suma_puntuacion = 75
                    else:
                        suma_puntuacion = 35
                case 2,1:
                    if vidas == 3:
                        suma_puntuacion =50
                    else:
                        suma_puntuacion =21
        case 4:
            match reinicios:
                case 3:
                    if vidas == 3:
                        suma_puntuacion = 100
                    else:
                        suma_puntuacion = 80
                case 2,1:
                    if vidas == 3:
                        suma_puntuacion =85
                    else:
                        suma_puntuacion =40
        case 5:
            match reinicios:
                case 3:
                    if vidas == 3:
                        suma_puntuacion = 150
                    else:
                        suma_puntuacion = 100
                case 2,1:
                    if vidas == 3:
                        suma_puntuacion =120
                    else:
                        suma_puntuacion =75

    return suma_puntuacion

def perder_puntuacion(puntuacion: int, nivel: int, reinicios: int, vidas: int)-> int:
    resta_puntuacion = 0

    if puntuacion !=0:
        match nivel:
            case 1:
                match reinicios:
                    case 3:
                        if vidas == 3:
                            resta_puntuacion = 16
                        else:
                            resta_puntuacion = 20
                    case 2:
                        if vidas == 3:
                            resta_puntuacion = 14
                        else:
                            resta_puntuacion = 18
                    case 1:
                        if vidas == 3:
                            resta_puntuacion = 14
                        else:
                            resta_puntuacion = 18
            case 2:
                match reinicios:
                    case 3:
                        if vidas == 3:
                            resta_puntuacion = 14
                        else:
                            resta_puntuacion = 18
                    case 2:
                        if vidas == 3:
                            resta_puntuacion = 12
                        else:
                            resta_puntuacion = 16
                    case 1:
                        if vidas == 3:
                            resta_puntuacion = 12
                        else:
                            resta_puntuacion = 16
            case 3:
                match reinicios:
                    case 3:
                        if vidas == 3:
                            resta_puntuacion = 10
                        else:
                            resta_puntuacion = 14
                    case 2:
                        if vidas == 3:
                            resta_puntuacion = 8
                        else:
                            resta_puntuacion = 12
                    case 1:
                        if vidas == 3:
                            resta_puntuacion = 8
                        else:
                            resta_puntuacion = 12
            case 4:
                match reinicios:
                    case 3:
                        if vidas == 3:
                            resta_puntuacion = 7
                        else:
                            resta_puntuacion = 11
                    case 2:
                        if vidas == 3:
                            resta_puntuacion = 6
                        else:
                            resta_puntuacion = 10
                    case 1:
                        if vidas == 3:
                            resta_puntuacion = 6
                        else:
                            resta_puntuacion = 10
            case 5:
                match reinicios:
                    case 3:
                        if vidas == 3:
                            resta_puntuacion = 4
                        else:
                            resta_puntuacion = 8
                    case 2:
                        if vidas == 3:
                            resta_puntuacion = 3
                        else:
                            resta_puntuacion = 5
                    case 1:
                        if vidas == 3:
                            resta_puntuacion = 3
                        else:
                            resta_puntuacion = 5
    else:
        resta_puntuacion = 0

    return resta_puntuacion