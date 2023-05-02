#IMPORTAMOS SPRITE DE LA LIBRERIA PYGAME
from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

#CREAMOS LA CLASE OBSTACLE  DEFINIMOOS LOS ATRIBUTOS
class Obstacle(Sprite):
    #INSERTAMS EL METODO CONSTRUCTOR CON LOS ATRIBUTOS QUE DEFINEN UN OBSTACULO 
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        

    def update(self,game_speed,obstacles):
        #RECORREMOS EL OBJETO EN X (HORIZONTAL)
        self.rect.x -= game_speed
        #SI EL VALOR DE X LLEGA A SER MENOR DEL ANCHO DE LA PANTALLA (1100) ELIMINAMOS EL OBJETO
        if self.rect.x < -self.rect.width:
            #METODO PARA SACAR EL PRIMER ELEMNTO DE LA LISTAS
            obstacles.pop()
    def draw(self,screen):
        #DIBUJAR EL OBSTACULO EN PANTALLA CON EL METODO BLIT QUE NOOS PEDIRA LA IMAGEN Y SU POSICION
        screen.blit(self.image[self.type],self.rect)