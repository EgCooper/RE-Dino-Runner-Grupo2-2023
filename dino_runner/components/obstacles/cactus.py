#IMPRTAMOOS LA CLASE OBSTACLE
from dino_runner.components.obstacles.obstacle import Obstacle
import random

#CREAMOS LA CLASE CACTUS Y HEREDAMOS A LA CLASE OSBTACLE
class Cactus(Obstacle):
    def __init__(self, image):
        #EL TIPO DE IMAGEN LA SACAREMOS DE UNA LISTA QUE CONTIENE 3 IMAGENES (CACTUS)
        #USAREMOS LA FUNCION RANDINT DE LA LIBRERIA RANDOM PARA PDOER ESCOGER UN NUMERO ALEATORIO ENTRE LOS LIMITES PUESTO (0-1-2) 
        self.type = random.randint(0,2)
        #LLAMAMOS A LOS METODOS DE LA CLASE PADRE (OSBTACLE)
        super().__init__(image,self.type)
        #DETERMINAMOS SU POSICION DEL CACTUS
        self.rect.y = 340
