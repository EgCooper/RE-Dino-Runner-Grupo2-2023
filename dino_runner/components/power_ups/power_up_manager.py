import random
import pygame
from dino_runner.components.obstacles.cactus import Small_Cactus,LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import RUNNING_SHIELD, SMALL_CACTUS,DELAY_QUIT,LARGE_CACTUS,BIRD, UPGRADE_SOUND
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

#CREAMOS LA CLASE 
class Power_Up_Manager:
    #AGREGAMOS SU METODO CONSTRUCTOR
    def __init__(self):
        #CREAMOS UNA VARIABLE DONDE ALMACENAREMOS LOS POWERUPS  U OBJETOS
        self.power_ups = []
        #VARIABLE PARA SAABER CUANDO AGREGAR EL POWERUP
        self.when_appers = 0
        self.points = 0


    #METODO PARA VERIFICAR SI HAY OBSTACULOS EN PANTALLA O NO 
    def update(self, points,game_speed,player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            ####    
            power_up.update(game_speed, self.power_ups) 
            #USAMOS EL METODO COLLIDERECT PARA SABER SI HUBO UN CHOQUE ENTRE EL JUGADOR Y OBSTACULOS
            if player.dino_rect.colliderect(power_up.rect):
                UPGRADE_SOUND.play()
                power_up.start_time = pygame.time.get_ticks()

                player.shield = True
                player.show_text = True
                player.type = power_up.type
                                
                

                time_random = random.randrange(5,8)
                player.shield_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)

            


    #DIBUJAMOS LOS OBSTACULOS
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    #RESETAMOS LOS POWERUPS
    def reset_power_ups(self, points):
        self.power_ups =  []
        self.points = points
        self.when_appers = self.points + random.randint(50,100)

    def generate_power_ups(self,points):
        self.points = points
        if len(self.power_ups ) == 0 :
            
            if self.when_appers == self.points:
                self.power_ups.append(Shield())
                self.when_appers = random.randint(self.when_appers+200,self.when_appers+400)
        elif len(self.power_ups) == 0:
            if self.when_appers == self.points:
                self.power_ups.append(Hammer())
                self.when_appers = random.randint(self.when_appers+100,self.when_appers+200)

        return self.power_ups