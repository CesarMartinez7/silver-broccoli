import pygame


# El balon no tiene movimiento

class Balon(pygame.sprite.Sprite):
    def __init__(self, velocidad: list[int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("./assets/SoccerBall.png")
        self.react=self.image.get_rect()
        self.move_ip=self.react.move_ip(0,0)
        self.velocidad=velocidad
        self.movimiento=self.react.move(velocidad)
    
    def actualizar(self) -> None:
        self.react = self.react.move(self.velocidad)  
    
    def draw(self,ventana) -> None:
        self.ventanaSurface=ventana
        self.ventanaSurface.blit(self.image,self.react)


# Clase con atributos del FANTASMA

class Ghost(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("./assets/ghost1.png")
        self.rect=self.image.get_rect()
        self.rect.move_ip(400,800)
        
    
    def movimientos(self) -> None:
        self.botones=pygame.key.get_pressed()
        if self.botones[pygame.K_LEFT]:
            self.rect=self.rect.move(-3,0)
        if self.botones[pygame.K_RIGHT]:
            self.rect=self.rect.move(3,0)
    
    def draw(self,ventana)->None:
        self.ventanaSurface=ventana
        self.ventanaSurface.blit(self.image,self.rect)