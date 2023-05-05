from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import HAMMER_TYPE,HAMMER,HAMMER_Y

class Hammer(PowerUp):
    def __init__(self):
        #CREAMOS UNA VARIABLE DONDE ALMACENAREMOS LA IMAGEN DEL POWERUP QUE QUERAMOS AGREGAR
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rect.y = HAMMER_Y

        super().__init__(self.image,self.type)
