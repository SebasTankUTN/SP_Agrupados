import pygame

def drawer(juego):

    for objeto in juego["objetos_a_mostrar"]:

        if objeto["tipo"]=="texto":
            juego["screen"].blit(objeto["objeto"], objeto["posicion"])

        if objeto["tipo"]=="boton":
            pygame.draw.rect(juego["screen"], objeto["color"], objeto["objeto"])
            
        



def generator(juego):

    juego["objetos_a_mostrar"]=[]

    if juego["pantalla_inicio"]:

        fondo = crear_boton("fondo",275,25,(66, 173, 145),200,400)
        iniciar_sesion = crear_texto("iniciar sesion",300,50,(250,250,250),36,"iniciar_sesion")
        jugar = crear_texto("jugar",300,100,(250,250,250),36,"jugar")
        estadisticas = crear_texto("estadisticas",300,150,(250,250,250),36,"estadisticas")
        boton_jugar = crear_boton("boton_jugar",300,85,(150,150,150),120,30)

        juego["objetos_a_mostrar"]=[fondo,iniciar_sesion,boton_jugar,jugar,estadisticas]


    if juego["pantalla_juego"]:
        jugar = crear_texto("jugar",300,100,(250,250,250),36,"jugar")

        juego["objetos_a_mostrar"]=[jugar]
    

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
        "objeto":font.render(texto, True, color)
        }
    return text
    