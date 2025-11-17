from data.elements import *
import src.core.engine as engine
import src.data.show as show
import src.data.loader as datos

game = datos.init_game_values()

salir=True
while salir:


    game = engine.jugar_agrupados(game, grupos_de_elementos)


    condicional=input("salir: a, sino apreta enter: ")
    if condicional == "a":
        salir = False