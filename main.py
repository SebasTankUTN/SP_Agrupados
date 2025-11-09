from elements import *
from agrupados import *
from funciones_generales import *
import random
elementos_jugados = []
nivel = 1
stage = 1
vidas = 3
reinicios = 3

salir=True
while salir:

    matriz_a_jugar = separar_grupos(elementos, elementos_jugados)
#    print()
#    mostrar_matriz(matriz_a_jugar)
    matriz_a_jugar = desordenar_grupos(matriz_a_jugar)

    while comprobar_stage(matriz_a_jugar,elementos) != True:
        print()
        mostrar_matriz(matriz_a_jugar)

        eleccion1=input("")
        eleccion2=input("")
        eleccion3=input("")
        eleccion4=input("")

        vector_eleccion = [eleccion1,eleccion2,eleccion3,eleccion4]

        while comprobar_grupo(vector_eleccion , elementos) == False:
            eleccion1=input("elegi")
            eleccion2=input("")
            eleccion3=input("")
            eleccion4=input("")

            vector_eleccion = [eleccion1,eleccion2,eleccion3,eleccion4]

        matriz_a_jugar = ordenar_grupo_en_linea(matriz_a_jugar, vector_eleccion, elementos)
    stage += 1
    if stage > 3 :
        stage = 1
        nivel += 1
        vidas = 3

    

    condicional=input("salir: a, sino apreta enter: ")
    if condicional == "a":
        salir = False

