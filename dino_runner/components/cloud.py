from dino_runner.utils.constants import GAME_SPEED, SCREEN_WIDTH,CLOUD,CLOUD_Y
import random
class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = CLOUD_Y
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= GAME_SPEED
        if self.x < self.width:
            self.x = SCREEN_WIDTH + random.randint(500,800)
            self.y = CLOUD_Y

    def draw(self,screen):
        screen.blit(self.image, (self.x , self.y))