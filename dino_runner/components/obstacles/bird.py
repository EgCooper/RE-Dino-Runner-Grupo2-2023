from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD_POSITIONS_Y
import random
#CREAMOS LA CLASE PAJARO Y REUTILIZAMOS EL CODIGO DE LOS OBSTACULOS ANTERIORES Y MODIFICACMOS LA POSICION EN Y

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = random.choice(BIRD_POSITIONS_Y)
        #DEFINIMOS UNA VARIABLE QUE DETERMINARA LOS AVANCES DEL PAJARO Y LO ESTABLECEMOS EN 0 PARA
        #POSTERIORMENTE MODIFICARLO CON UNA CONDICIONAL
        self.index = 0

    def draw(self,screen):
        #CONDICIONAL PRA CAMBIAR DE IMAGEN CONTANDO LOS PASOS
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index +=1