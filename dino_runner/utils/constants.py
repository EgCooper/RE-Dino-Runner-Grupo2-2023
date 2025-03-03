import pygame
import os

# Global Constants
TITLE = "Game Dino Runner"
#ALTURA
SCREEN_HEIGHT = 600
#ANCHURA
SCREEN_WIDTH = 1100
FPS = 30
pygame.mixer.init()


IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "icodino.jpg"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
DINO_ICO =[pygame.image.load(os.path.join(IMG_DIR, "Dino/Dino.png"))]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

#AGREAMOS SHIELDTYPE
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HAMMER_Y = 340

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"



#CONSTANTES DE LA UBICACION DEL DINOSAURIO

POSITION_X = 80
POSITION_Y = 330

#UBICACION DE LOS OBSTACULOS EN Y
BIRD_POSITIONS_Y = (320,250,200,150,100,290)

CACTUS_SMALL_Y = 340

CACTUS_LARGE_Y = 320

#CONSTANTE PARA DETERMINAR LA VELOCIDAD DE SALTO DEL DINOSAURIO

JUMP_VEL = 8.5

#CONSTANTE PARA POSICIONAR AL DINO DUCK

DUCK_Y = 370

#DELAY FOR EXIT GAME
DELAY_QUIT = 300

#DEFINIMOS EL GAME SPEED DEL JUEGO
GAME_SPEED = 20

#ESTABLECEMOS LA PISTA EN PANTALLA X AND Y

SET_PIST_x = 0
SET_PIST_Y = 400

#CLOUD POSITION
CLOUD_Y = 100

#COLORS

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

#FONTS
FONT_STYLE = 'freesansbold.ttf'

#SOUNDS
DEATH_SOUND = pygame.mixer.Sound("lose.wav")
GAME_SOUND = pygame.mixer.Sound("backGround.wav")
JUMP_SOUND = pygame.mixer.Sound("jump.wav")
UPGRADE_SOUND = pygame.mixer.Sound("ImpactF.wav")
SCORE_SOUND = pygame.mixer.Sound("100pts.wav")

