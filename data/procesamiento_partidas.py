import csv
def separar_str(cadena:str, separacion: str)->list:
    """recibe una cadena de texto y lo separa en dos partes utilizando codigo ascii
    Args:
        cadena (str): cadena de texto a analizar
        separacion (int): utilizada en el codigo ascii que indica un nuevo string

    Returns:
        list: Devuelve las cadenas separadas en una lista.
    """
    primer_tramo = False
    for i in range (len(cadena)):
        
        if ord(cadena[i]) == ord(separacion[0]):

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

def cargar_elementos(path)->dict:
    lista_diccionarios = []
    print(path)

    with open(path, "r") as archivo:

        for linea in archivo:
            
            nombre = separar_str(linea, ",")

            elemento1 = separar_str(nombre[1], ",")
            elemento2 = separar_str(elemento1[1], ",")
            elemento3 = separar_str(elemento2[1], ",")
            elemento4 = separar_str(elemento3[1], ",")

            elemento4 = separar_str(elemento4, "\n")

            diccionario = {
                "titulo":nombre[0],
                "elementos":[elemento1[0],elemento2[0],elemento3[0],elemento4[0]]
            }
            lista_diccionarios += [diccionario]

    return lista_diccionarios
