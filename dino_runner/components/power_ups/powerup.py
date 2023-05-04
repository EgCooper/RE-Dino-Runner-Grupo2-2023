from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
import random
class PowerUp():
    def __init__(self,image,type):
        self.image = image
        self.rect = self.image.get_rect()
        self.type = type
        #PONEMOS LA IMAGEN FUERA DE LA PANTALLA Y USAMOS EL RANDOM PARA QUE EL OBJETO VARIE SU APARICION
        self.rect.x = SCREEN_WIDTH + random.randint(800,1000)
        self.rect.y = random.randint(100,150)
        #DETERMINAMOS EL PERIODO DEL TIEMPO PARA QUITAR EL POWER UP AL DINOSAURIO
        self.start_time = 0
        self.width = self.image.get_width()

    #METODO PARA RECORRER EL POWERUP Y UNA VEZ QUE SEA MENOR A LAS MEDIDAS DE LA PANTALLA ELIMINAR EL POWERUP
    def update(self,game_speed,powerups):
        self.rect.x -= game_speed
        if self.rect.x < self.rect.width:
            powerups.pop()
    def draw(self,screen):
        screen.blit(self.image, self.rect)