import pygame
from models import (Balon,Ghost)
pygame.init()

FONDOVENTANA=pygame.image.load("./assets/football-pitch.png")

colores=(0,0,0)
RESOLUCION=(800,1000)

ventana=pygame.display.set_mode(RESOLUCION,pygame.RESIZABLE)

pygame.display.set_caption("JumpThor")

ICON=pygame.image.load("./assets/SoccerBall.png")
pygame.display.set_icon(ICON)
ESTADO_JUGANDO=True
# Musica inicializacion


class Musica:
    def __init__(self) -> None:
        pygame.mixer.init() 
        pygame.mixer.music.load("./sounds/chickenSoup.mp3")  
        self.reproducir()
        
    def reproducir(self) -> None:
        pygame.mixer.music.play(-1)  


musica = Musica()


#SOUNDS
# PROXIMA FUNCION IMPLEMENTADA
SONIDO_COLISION=pygame.mixer.Sound("./sounds/8.ogg")


# Class Objeto Balon



velocidad=[5,5]    







# CLASE DEL EMOJI PARA SIMPLICAR LAS COSAS
# DEBERIA AÑADIR UNA VARIABLE QUE SE LE PASE A LA POSICION DE ESTA MANEJA ME HABRIA SIMPLIFICADO CREAR DOS CLASES PARA CADA PLAYER
class Emoji(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/sun.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,1)
        self.draw() 
        
    def movimientos(self) -> None:
        self.botones =pygame.key.get_pressed()
        if self.botones[pygame.K_a]:  
            self.rect = self.rect.move(-3, 0)
        if self.botones[pygame.K_d]:
            self.rect=self.rect.move(3,0)
    
    def draw(self)->None:
        ventana.blit(self.image,self.rect)


#INSTANCIAS
player1=Ghost()
player2=Emoji()
balon=Balon(velocidad=velocidad)


# Collisiones de los personajes y pelotas
def Collisiones():        
    if player1.rect.colliderect(balon.react):
        balon.velocidad[1]= -balon.velocidad[1]
        SONIDO_COLISION.play()
        print(puntos)
    if player2.rect.colliderect(balon.react):
        balon.velocidad[1]= - balon.velocidad[1]
        SONIDO_COLISION.play()
# Movimientos de los personajes       
def movimientosPersonajes():
    player2.movimientos()
    player1.movimientos()



puntos=0





while ESTADO_JUGANDO:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ESTADO_JUGANDO=False
    
    movimientosPersonajes()
    Collisiones()
    balon.actualizar()
    
    if balon.react.left < 0 or balon.react.right > ventana.get_width():
        balon.velocidad[0]=-balon.velocidad[0]
    if balon.react.top < 0 or balon.react.bottom > ventana.get_height():
        balon.velocidad[1] = -balon.velocidad[1]
        
    
    # print(ventana.get_height(),ventana.get_width())
    ventana.fill(color=colores)
    ventana.blit(FONDOVENTANA,(0,2))
    
    balon.draw(ventana=ventana)
    player1.draw(ventana=ventana)
    player2.draw()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()    
