import json
import random

def cargar_archivo_json(path, modo):
    
    with open(path, modo) as archivo:
        datos = json.load(archivo)

    return datos


def guardar_json(path,datos):
    with open(path,"w") as archivo:
        json.dump(datos, archivo, indent = 4)


def get_string(mensaje:str, mensaje_error, funcion):

    cadena = input(mensaje)
    while funcion(cadena) != True:
        print(mensaje_error)
        cadena = input(mensaje)

    return cadena

def generar_id():

    id_usuario = random.randint(10000,99999)

    return id_usuario

def validar_json(lista):
    
    datos = cargar_archivo_json("data/archivos_usuarios.json","r")
    lista_Archivos = datos[lista]

    estado = False
    if lista_Archivos !=[]:
        estado = True
    
    return estado

def validacion_string(cadena: str)-> bool:

    estado = True
    
    if len(cadena) > 15 or len(cadena) == 0:
        estado = False
    
    return estado