import pygame


from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAME_SPEED, SET_PIST_Y, SET_PIST_x,RED,WHITE
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components import text_utils
from dino_runner.components.cloud import Cloud
#LLAMAMOS A LA CLASE DINOSAUR

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = GAME_SPEED
        self.x_pos_bg = SET_PIST_x
        #DEFINIMOS LA ALTURA A LA QUE ESTARA LA PISTA
        self.y_pos_bg = SET_PIST_Y
        #AGREGAMOS EL PLAYER (PLAYER)
        self.player = Dinosaur()
        #AGREGAMOS EL OBSTACLEMANAGER PARA AGREGAR LOS OBJETOS
        self.obstacle_manager = ObstacleManager()
        #AGREGAMOS LA NUBE AL GAME
        self.cloud = Cloud()
        #VARIABLE PARA CONTAR LOS PUNTOS
        self.points = 0 

        self.running = True

        self.death_count = 0

    #METODO QUE CONTENDRA UN BUCLE QUE CORRERA EN ORDEN EL JUEGO (EVENTS,UPDATES,DRAW)
    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
    

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()


    def show_menu(self):
        self.running = True
        self.screen.fill(WHITE)
        self.print_menu_elements()
        pygame.display.update()
    

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            text,text_rect = text_utils.get_centered_message('Press Any Key to Start. ')
            self.screen.blit(text, text_rect)
 

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.run()


    #METODO PARA SALIR DEL JUEGO
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    #METODO PARA ACTUALIZAR
    def update(self):
        #CAPTURA LA TECLA QUE EL USUARIO ESTA PRESIONANDO
        user_input = pygame.key.get_pressed()
        #DINOSAURIO
        self.player.update(user_input)
        #OBSTACULO
        self.obstacle_manager.update(self)
        #NUBE 
        self.cloud.update()

    #METODO PARA INSERTAR LAS IMAGENES
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(RED)
        self.draw_background()
        #DINOSAURIO OBSTACULO
        self.player.draw(self.screen)
        #OBSTACULO DIBUJO
        self.obstacle_manager.draw(self.screen)
        #NUBES
        self.cloud.draw(self.screen)
        #FUNCIONES PARA ACTUALIZAR LA PANTALLA
        pygame.display.update()
        pygame.display.flip()

    #METODO PARA AGREGAR
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
