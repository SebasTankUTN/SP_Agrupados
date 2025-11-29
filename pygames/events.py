import pygame
import sys
import pygames.core as core


def reader(juego):

    for event in pygame.event.get():
        for objeto in juego["objetos_a_mostrar"]:

            if event.type == pygame.QUIT:
                juego["seguir"] = False


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    juego["seguir"] = False

                elif event.key == pygame.K_DOWN:
                    if objeto["nombre"] == "jugar":
                        x,y = objeto["posicion"]
                        objeto["posicion"] = (x+10,y+20)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if objeto["nombre"] == "boton_jugar" and objeto["objeto"].collidepoint(event.pos):

                    juego["pantalla_juego"] = True
                    juego["pantalla_inicio"] = False
                    core.generator(juego)
                    print("me tocaaste")

                


                

