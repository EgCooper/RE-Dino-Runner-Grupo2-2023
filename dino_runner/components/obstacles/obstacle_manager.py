import random
import pygame
from dino_runner.components.obstacles.cactus import Small_Cactus,LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS,DELAY_QUIT,LARGE_CACTUS,BIRD

#CREAMOS LA CLASE 
class ObstacleManager:
    #AGREGAMOS SU METODO CONSTRUCTOR
    def __init__(self):
        #CREAMOS UNA VARIABLE DONDE ALMACENAREMOS LOS OBSTACULOS  U OBJETOS
        self.obstacles = []


    #METODO PARA VERIFICAR SI HAY OBSTACULOS EN PANTALLA O NO 
    def update(self, game):
        #CREAMOS UNA CONDICIONAL QUE USARA EL METODO LEN PARA CONTAR LA LISTA  VER SI HAY O NO OBSTACULOS
        #Y POSTERIORMENTE AGREGAR 1 X 1
        if len(self.obstacles) == 0:
            options_obstacles = random.randint(0,2)
            #CREAMOS OTRA CONDICIONAL PARA AGREGAR LOS DISTINTOS OBSTACULOS QUE TENEMOS
            #USAMOOS APPEND PARA AGREGAR EL OBSTACULO NUMERO 1 QUE SERIA EL CACTUS PEQUEÑO
            if options_obstacles == 0:
                self.obstacles.append(Small_Cactus(SMALL_CACTUS))
            #USAMOOS APPEND PARA AGREGAR EL OBSTACULO NUMERO 2 QUE SERIA EL CACTUS GRANDE
            elif options_obstacles == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            #AGREGAMOS EL ULTIMO OBJETO CON OTRA CONDICIONAL  obstaculo numero 3
            elif options_obstacles == 2:
                self.obstacles.append(Bird(BIRD))   
        #CREAMOS UN BUCLE PARA VER SI EL JUGADOR (DINOSAURIO CHOCA CON UN OBSTACULO)
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles) 
            #USAMOS EL METODO COLLIDERECT PARA SABER SI HUBO UN CHOQUE ENTRE EL JUGADOR Y OBSTACULOS
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
            #AGREGAMOS DELAY CON LA FUNCION TIMDELAY
                    pygame.time.delay(DELAY_QUIT)
                    game.playing = False
                    break
                #CUANDO EL JUGADOR MUERA EL CONTADOR DE MUERTES AUMENTARA
                    game.death_count+=1
                else:
                    self.obstacles.remove(obstacle)
            
                

        
    #DIBUJAMOS LOS OBSTACULOS
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []