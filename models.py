


import pygame


#  Clase balon que tiene movimiento optimizado 

class Balon(pygame.sprite.Sprite):
    def __init__(self, velocidad: list[int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("./assets/SoccerBall.png")
        self.react=self.image.get_rect()
        self.move_ip=self.react.move_ip(0,0)
        self.velocidad=velocidad
        self.movimiento=self.react.move(velocidad)

    #La actualizacion que hace que el balon se mueva
    def actualizar(self) -> None:
        self.react = self.react.move(self.velocidad)  
    
    def draw(self,ventanaGame) -> None:
        self.ventanaSurface=ventanaGame
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
        if self.botones[pygame.K_UP]:
            print("Arriba")
            self.rect=self.rect.move(0,-3)
        if self.botones[pygame.K_DOWN]:
            self.rect=self.rect.move(0,3)
            print("Abajo")
    
    def draw(self,ventanaGame) -> None:
        self.ventanaSurface=ventanaGame
        self.ventanaSurface.blit(self.image,self.rect)


# Clase con atributos de Emoji

class Emoji(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/sun.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,1)

        
    def movimientos(self) -> None:
        self.botones =pygame.key.get_pressed()
        if self.botones[pygame.K_a]:  
            self.rect = self.rect.move(-3, 0)
        if self.botones[pygame.K_d]:
            self.rect=self.rect.move(3,0)
        if self.botones[pygame.K_w]:
            self.rect=self.rect.move(0,-3)
        if self.botones[pygame.K_s]:
            self.rect=self.rect.move(0,3)
    
    def draw(self,ventanaGame) -> None:
        self.ventanaSurface=ventanaGame
        self.ventanaSurface.blit(self.image,self.rect)

# Clase para la musica de de fondo o para otras cosas

class Musica():
    def __init__(self,cancion) -> None:
        self.cancion=cancion
        pygame.mixer.init() 
        pygame.mixer.music.load(cancion)  
        self.reproducir()
        
    def reproducir(self) -> None:
        pygame.mixer.music.play(-1) 
        

# Sonidos class (PRINCIPALMENTE PARA COLLISIONES O DISPAROS)

class Sonidos():
    def __init__(self):
        pygame.mixer.init()

    def reproducir(self,sound):
        self.sonido=pygame.mixer.Sound(sound)
        self.sonido.play()