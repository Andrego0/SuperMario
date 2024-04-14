from pygame import *
mixer.init()
font.init()
#створи вікно гри
TILESIZE = 30
MAP_WIDTH, MAP_HEIGHT = 35,20
WIDTH, HEIGHT = TILESIZE*MAP_WIDTH, TILESIZE*MAP_HEIGHT
FPS = 120
font1 = font.SysFont("ProtestRevolution-Regular.ttf", 40)
font2 = font.SysFont("ProtestRevolution-Regular.ttf", 55)

window = display.set_mode((WIDTH, HEIGHT)) #створюємо вікно 
display.set_caption("Mario")
clock = time.Clock() # Створюємо ігровий таймер

platform1_img= image.load("platform/platform_01.png")
platform2_img= image.load("platform/platform_02.png")
platform3_img= image.load("platform/platform_88.png")
point1_img = image.load ("point/point_01.png")




sprites = sprite.Group()

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, width, height, x, y):
        super().__init__()
        self.image = transform.scale(sprite_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        sprites.add(self)

    def draw(self, window):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, sprite_image, width, height, x, y):
        super().__init__(sprite_image, width, height, x, y)
       
        self.hp = 100
        self.damage = 20
        self.coins = 0
        self.speed = 3

    def update(self):
        global hp_text
        self.old_pos = self.rect.x, self.rect.y

        keys = key.get_pressed() #отримуємо список натиснутих клавіш
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        
           
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
           
        if keys[K_d] and self.rect.right < WIDTH    :
            self.rect.x += self.speed
           
platforms = sprite.Group()
enemys = sprite.Group()


class Platform(GameSprite):
    def __init__(self, platform_img, x, y):
        super().__init__(platform_img,TILESIZE, TILESIZE, x, y)
        platforms.add(self)

with open("Map.txt", "r") as file:
    x, y = TILESIZE/2, TILESIZE/2
    map = file.readlines()
    for row in map:
        for symbol in row:
            if symbol == 'W':
                Platform(platform2_img, x,y)
            elif symbol == 'D':
                Platform(platform1_img, x,y)
            elif symbol == 'S':
                Platform(platform3_img, x,y)
            elif symbol == 'P':
                GameSprite(point1_img, TILESIZE-5, TILESIZE-5, x,y)
            # elif symbol == 'P':
            #     player.rect.x = x
            #     player.rect.y = y
            #     player.start_x, player.start_y = x, y
            # elif symbol == 'T':
            #     treasure = GameSprite(point_img, TILESIZE, TILESIZE, x ,y)
            x += TILESIZE
        y+=TILESIZE
        x = TILESIZE/2


while True:
    #оброби подію «клік за кнопкою "Закрити вікно"
    for e in event.get():
        if e.type == QUIT:
            quit()
   
    window.fill((3, 73, 252))
    sprites.draw(window)
   
    display.update()
    clock.tick(FPS)