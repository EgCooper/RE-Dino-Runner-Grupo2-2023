#IMPRTAMOOS LA CLASE OBSTACLE
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CACTUS_LARGE_Y,CACTUS_SMALL_Y
import random

#CREAMOS LA CLASE CACTUS Y HEREDAMOS A LA CLASE OSBTACLE
class Small_Cactus(Obstacle):
    def __init__(self, image):
        #EL TIPO DE IMAGEN LA SACAREMOS DE UNA LISTA QUE CONTIENE 3 IMAGENES (CACTUS)
        #USAREMOS LA FUNCION RANDINT DE LA LIBRERIA RANDOM PARA PDOER ESCOGER UN NUMERO ALEATORIO ENTRE LOS LIMITES PUESTO (0-1-2) 
        self.type = random.randint(0,2)
        #LLAMAMOS A LOS METODOS DE LA CLASE PADRE (OSBTACLE)
        super().__init__(image,self.type)
        #DETERMINAMOS SU POSICION DEL CACTUS
        self.rect.y = CACTUS_SMALL_Y


#CREAMOS LA CLASE LARGECACTUS Y REUTILIZAMOS EL CODIGO DEL CACTUS PEQUEÑO A DIFERENCIA QUE ESTE ESTARA UBICADO EN OTRA POSICION 
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = CACTUS_LARGE_Y


