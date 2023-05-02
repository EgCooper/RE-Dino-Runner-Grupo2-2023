from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,DELAY_QUIT
import pygame

#CREAMOS LA CLASE 
class ObstacleManager:
    #AGREGAMOS SU METODO CONSTRUCTOR
    def __init__(self):
        #CREAMOS UNA VARIABLE DONDE ALMACENAREMOS LOS OBSTACULOS  U OBJETOS
        self.obstacles = []
    #METODO PARA VERIFICAR SI HAY OBSTACULOS EN PANTALLA O NO 
    def update(self, game):
        #CREAMOS UNA CONDICIONAL QUE USARA EL METODO LEN PARA CONTAR LA LISTA  VER SI HAY O NO OBSTACULOS
        if len(self.obstacles) == 0:
            #USAMOOS APPEND PARA AGREGAR UN OBSTACULO EN CASO DE QUE NO EXISTA NINGUNO EN LA LISTA
            self.obstacles.append(Cactus(SMALL_CACTUS))
        #CREAMOS UN BUCLE PARA VER SI EL JUGADOR (DINOSAURIO CHOCA CON UN OBSTACULO)
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles) 
            
            #USAMOS EL METODO COLLIDERECT PARA SABER SI HUBO UN CHOQUE ENTRE EL JUGADOR Y OBSTACULOS
            
            if game.player.dino_rect.colliderect(obstacle.rect):
            #AGREGAMOS DELAY CON LA FUNCION TIMDELAY
                pygame.time.delay(DELAY_QUIT)
                game.playing = False
                break

        
    #DIBUJAMOS LOS OBSTACULOS
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)