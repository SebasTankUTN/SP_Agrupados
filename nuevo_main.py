import sys
import pygame
import pygames.events as event
import pygames.core as core

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
    "objetos_a_mostrar": []
}


core.generator(juego)


while juego["seguir"]:

    event.reader(juego)
    
    juego["screen"].fill((0, 0, 15))

    core.drawer(juego)

    pygame.display.update()
    juego["clock"].tick(30)


pygame.quit()
sys.exit()