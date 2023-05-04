#La clase sprite es un clase que nos ayudara con el movimiento de imagenes
#basicamente son rectangulos que pueden ser objetos(personajes,obstaculos)
from pygame.sprite import Sprite
import pygame


#IMPORTAMOS LA CONSTANTE ESPECIFICA DE RUNNING
from dino_runner.utils.constants import DEFAULT_TYPE, FONT_STYLE, RUNNING,POSITION_Y,POSITION_X,JUMP_VEL,JUMPING,DUCKING,DUCK_Y


#CREAMOS LA CLASE DINOSAURIO Y LA UBICAMOS EN LA VENTANA
class Dinosaur:
  
    #INICIAMOS TODOS EL METODO CONSTRUCTOR QUE CONTENDRA TODAS LAS VARIABLES QUE UTILIZAREMOS
    def __init__(self):
        #LLAMAMOS A LA PRIMER IMAGEN Y LA ALMACENAMOS EN UNA VARIABLE
        self.image = RUNNING[0]
        #CREAMOS UNA VARIABLE QUE RECIBIRA LA UBICACION DEL DINOSAURIO
        self.dino_rect = self.image.get_rect()
        #VARIABLES QUE RECIBIRAN LA UBICACION TANTO EN X AND Y DEL DINOSARIO
        self.dino_rect.x = POSITION_X
        self.dino_rect.y = POSITION_Y
        #VARIABLE QUE CONTARA EL AVANCE DEL DINOSARIO PARA PODER CAMBIAR DE PIE (IMAGEN)
        self.step_index = 0
        #CREAMOS LOS ESTADOS EN LOS QUE PUEDE ENCONTRARSE EL DINOSAURIO
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.type = DEFAULT_TYPE
        self.setup_state_booleans()

    def update(self,user_input):
        #ACTUALIZAMOS LOS ESTADOS Y LUEGO EJECUTAMOS LAS FUNCIONES
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        #SI EL USUARIO PRESIONA LA TECLA ABAJO EL DINOSARIO DEBERA AGACHARSE, SIEMPRE Y CUANDO NO ESTE SALTANDO
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
       #SI EL USUARIO PRESIONA LA TECLA HACIA ARRIBA EL DINOSAURIO DEBE DE SALTAR, SIEMPRE Y CUANDO NO ESTE SALTANDO
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        #Y SI NO ESTA SALTANDO ENTONCES ESTA CORRIENDO
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0
    #INSERTAR AL DINOSAURIO EN LA PISTA DEL JUEGO
    def draw(self,screen):
        #DIBUJAMOS EN PANTALLA E INTRODUCIMOS LA IMAGEN Y LA UBICACION
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
    
    #INTERCALAR 2 SPRITES(IMAGENES) PARA PODER CREAR UNA VISTA DE QUE EL DINOSAURIO ESTE CORRIENDO
    def run(self):
        #RESETEAR DINOSARIO PARA QUE RETOME LA POSICION ORIGINAL, PARA CUANDO VUELVA A CORRER
        self.dino_rect.y = POSITION_Y

        #CONDICIONAL PRA CAMBIAR DE IMAGEN CONTANDO LOS PASOS
        if self.step_index < 5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]
        self.step_index +=1
    
    
    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y  -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < - JUMP_VEL:

            self.dino_rect.y = POSITION_Y
            self.dino_jump = False
            self.jump_vel = JUMP_VEL


    def duck(self):
        self.image = DUCKING [0]
        #POSICIONAMOS AL DINOSAURIO DUCK EN LA PANTALLA
        self.dino_rect.y = DUCK_Y
        if self.step_index < 5:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        self.step_index +=1

    def setup_state_booleans(self):
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
        self.has_powerup = False

    def check_invincibility(self,screen):
        if self.shield:
            #CON ESTO VEREMOS CUANTO TIEMPO DURAR EL ESCUDO 
            time_to_show = round ((self.shield_time_up - pygame.time.get_ticks())/100,2)
            if time_to_show >= 0:
                if self.show_text:
                    font = pygame.font.Font(FONT_STYLE,18)
                    text = font.render(f'Shield enable for{time_to_show}', True, (0,0,0))
                    textRect = text.get_rect()
                    textRect.center = (500,400)
                    screen.blit(text,textRect)
            else:
                self.shield = False