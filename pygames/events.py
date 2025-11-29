import pygame
import sys
import pygames.core as core
import src.core.engine as engine
import src.data.processor as processor
import src.core.comodines as comodines


def reader(juego,game,grupos_de_elementos):

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
                    game["matriz_a_jugar"] = engine.generar_nuevo_stage(grupos_de_elementos, game["elementos_jugados"])
                    core.generator(juego,game)
                    

                if objeto["nombre"] == "boton_comodin1" and objeto["objeto"].collidepoint(event.pos) and game["comodin1"]:
                    game["comodin1"] = False
                    respuesta_comodin = comodines.comodin_revelar_categoria(game)
                    engine.mostrar_comodin_1(respuesta_comodin, juego)
                if objeto["nombre"] == "boton_comodin2" and objeto["objeto"].collidepoint(event.pos)and game["comodin2"]:
                    game["comodin2"] = False
                    respuesta_comodin = comodines.comodin_revelar_dos_elementos(game)
                    engine.mostrar_comodines_2_y_3(respuesta_comodin, juego)
                if objeto["nombre"] == "boton_comodin3" and objeto["objeto"].collidepoint(event.pos)and game["comodin3"]:
                    game["comodin3"] = False
                    respuesta_comodin = comodines.comodin_revelar_dos_elementos(game,False)
                    engine.mostrar_comodines_2_y_3(respuesta_comodin, juego, True)
                    
                    

                if "boton_matriz" in objeto["nombre"] and objeto["objeto"].collidepoint(event.pos):
                    
                    if objeto["color"] == (42, 222, 40) and objeto["ordenado"] != True:
                        game["elecciones"].remove(objeto["valor"])
                        objeto["color"] = (224, 224, 105)
                    else:
                        game["elecciones"].append(objeto["valor"])
                        objeto["color"] = (42, 222, 40)

                    engine.manejar_elecciones(juego,game,grupos_de_elementos)
                            
                                
                                
                                            

                                

                        
            

                            

                


                

