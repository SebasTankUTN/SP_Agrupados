import sys
import pygame
import pygames.events as event
import pygames.core as core
from data.procesamiento_partidas import *
import src.core.engine as engine
import src.data.show as show
import src.data.loader as datos
import data.src.processor_usuarios as load
import data.engine_user as up
import data.src.loader_usuarios as down

pygame.init()
pygame.display.set_caption("AGRUPADOS")

juego = {
    "seguir": True,
    "screen": pygame.display.set_mode((800, 600)),
    "clock": pygame.time.Clock(),
    "pantalla_inicio": True,
    "pantalla_iniciar_sesion": False,
    "pantalla_registro": False,
    "pantalla_juego": False,
    "pantalla_estadisticas": False,
    "pantalla_perder": False,
    "pantalla_ganar": False,
    "objetos_a_mostrar": []
}

game = datos.init_game_values()
grupos_de_elementos = cargar_elementos('data/archivo_partidas.csv')
core.generator(juego,game)



while juego["seguir"]:

    event.reader(juego,game,grupos_de_elementos)
    
    juego["screen"].fill((0, 0, 15))

    core.drawer(juego)

    pygame.display.update()
    juego["clock"].tick(30)


pygame.quit()
sys.exit()