import pygame
import src.core.engine as engine
import src.data.processor as processor

def drawer(juego):

    for objeto in juego["objetos_a_mostrar"]:

        if objeto["tipo"]=="texto":
            juego["screen"].blit(objeto["objeto"], objeto["posicion"])

        if objeto["tipo"]=="boton":
            pygame.draw.rect(juego["screen"], objeto["color"], objeto["objeto"])
            


def generator(juego,game):

    juego["objetos_a_mostrar"]=[]

    if juego["pantalla_inicio"]:

        fondo = crear_boton("fondo",275,25,(66, 173, 145),200,400)
        iniciar_sesion = crear_texto("iniciar sesion",300,50,(250,250,250),36,"iniciar_sesion")
        jugar = crear_texto("jugar",300,100,(250,250,250),36,"jugar")
        estadisticas = crear_texto("estadisticas",300,150,(250,250,250),36,"estadisticas")
        boton_jugar = crear_boton("boton_jugar",300,85,(150,150,150),120,30)

        juego["objetos_a_mostrar"]=[fondo,iniciar_sesion,boton_jugar,jugar,estadisticas]


    if juego["pantalla_juego"]:
        texto_vidas = crear_texto(f"vidas restantes: {game["vidas"]}",520,300,(250,250,250),36,"vidas")
        texto_reinicios = crear_texto(f"reinicios restantes: {game["reinicios"]}",520,350,(250,250,250),36,"reinicios")
        texto_puntuacion = crear_texto(f"puntuacion: {game["puntuacion"]}",520,400,(250,250,250),36,"puntuacion")
        texto_stage = crear_texto(f"stage: {game["stage"]}",25,25,(250,250,250),36,"stage")
        texto_nivel = crear_texto(f"nivel: {game["nivel"]}",150,25,(250,250,250),36,"nivel")

        boton_comodin1 = crear_boton("boton_comodin1",600,100,(250,250,250),45,45)
        boton_comodin2 = crear_boton("boton_comodin2",600,150,(250,250,250),45,45)
        boton_comodin3 = crear_boton("boton_comodin3",600,200,(250,250,250),45,45)

        texto_nombre_grupo = crear_texto(f"nombre grupos",25,50,(250,250,250),25,"nombre_grupos")

        juego["objetos_a_mostrar"] = crear_matriz(game) + [texto_vidas,boton_comodin1, boton_comodin2, boton_comodin3, texto_reinicios, texto_puntuacion, texto_stage, texto_nivel, texto_nombre_grupo]
    
    if juego["pantalla_perder"]:
        texto_perdiste = crear_texto("PERDISTE WACHIN",100,300,(250,250,250),88,"perder")
        juego["objetos_a_mostrar"] = [texto_perdiste]

    if juego["pantalla_ganar"]:
        texto_ganaste = crear_texto("GANASTE WACHIN",100,300,(250,250,250),88,"ganar")
        juego["objetos_a_mostrar"] = [texto_ganaste]
    pass


def crear_boton(nombre: str,x: int, y: int, color: tuple, ancho: int, alto: int):

    boton = {
            "nombre":nombre,
            "tipo":"boton",
            "objeto":pygame.Rect(x, y, ancho, alto),
            "color":(color)
        }
    return boton
    

def crear_texto(texto: str, x: int, y: int, color: tuple, tamaño_fuente: int,nombre:str):
    font = pygame.font.SysFont(None, tamaño_fuente)

    text = {
        "nombre":nombre,
        "tipo":"texto",
        "posicion":(x,y),
        "color":color,
        "objeto":font.render(texto, True, color),
        "texto":texto,
        "fuente":pygame.font.SysFont(None, tamaño_fuente)
        }
    return text
def crear_imagen(x: int,y: int,path: str,ancho: int,alto: int,nombre: str):
    objeto = pygame.image.load(path)
    objeto = pygame.transform.scale(objeto,(ancho,alto))
    img = {
        "nombre":nombre,
        "objeto":objeto,
        "posicion":(x,y)

    }

    return img
    

def crear_matriz(game):
    vector_botones = []
    vector_textos = []
    numero_de_elemento = 0
    x = 75
    y = 125

    for i in range (4):
        x = 75
        for j in range (4):
            vector_textos += [crear_texto(game["matriz_a_jugar"][i][j],x,y,(0,0,0),26,f"texto_matriz{numero_de_elemento}")]



            boton = crear_boton(f"boton_matriz{numero_de_elemento}",x,y,(224, 224, 105),85,85)
            estados_adicionales = {"valor":game["matriz_a_jugar"][i][j],"ordenado":False}
            boton.update(estados_adicionales)
            vector_botones += [boton]
            numero_de_elemento += 1
            x += 105
        pass
        y += 105
    
    return vector_botones + vector_textos



        
    