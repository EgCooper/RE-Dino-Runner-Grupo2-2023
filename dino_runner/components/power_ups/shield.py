from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import SHIELD,SHIELD_TYPE

class Shield(PowerUp):
    def __init__(self):
        #CREAMOS UNA VARIABLE DONDE ALMACENAREMOS LA IMAGEN DEL POWERUP QUE QUERAMOS AGREGAR
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image,self.type)
