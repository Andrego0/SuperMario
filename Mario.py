from pygame import *
mixer.init()
font.init()
#створи вікно гри
TILESIZE = 35
MAP_WIDTH, MAP_HEIGHT = 35,20
WIDTH, HEIGHT = TILESIZE*MAP_WIDTH, TILESIZE*MAP_HEIGHT
FPS = 120
bg_color= (3, 73, 252)
font1 = font.SysFont("ProtestRevolution-Regular.ttf", 40)
font2 = font.SysFont("ProtestRevolution-Regular.ttf", 55)

window = display.set_mode((WIDTH, HEIGHT)) #створюємо вікно 
display.set_caption("Mario")
clock = time.Clock() # Створюємо ігровий таймер
player1_img = image.load("player/player_01.png")
platform1_img= image.load("platform/platform_01.png")
platform2_img= image.load("platform/platform_02.png")
platform3_img= image.load("platform/platform_88.png")
platform4_img= image.load("platform/platform_11.png")
platform5_img= image.load("platform/platform_57.png")
platform6_img= image.load("platform/platform_56.png")
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
        self.speed_x = 3
        self.speed_y = 0
        self.on_ground = True
        self.jump_height = 70
    

    def update(self):
        global hp_text
        self.old_pos = self.rect.x, self.rect.y

        keys = key.get_pressed() #отримуємо список натиснутих клавіш
        if keys[K_SPACE] and self.rect.y > 0 and self.on_ground: 
            self.rect.y -= self.jump_height
            self.on_ground = False
            self.speed_y = 0
            
           
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speed_x
           
        if keys[K_d] and self.rect.right < WIDTH    :
            self.rect.x += self.speed_x
           
        if not self.on_ground:
            self.speed_y += 0.25
            self.rect.y += self.speed_y

        collide_list = sprite.spritecollide(self, platforms, False)
        for platform in collide_list: 
            self.on_ground = True
            # self.rect.bottom = platform.rect.top
        if len(collide_list) == 0:
            self.on_ground = False

platforms = sprite.Group()
enemys = sprite.Group()
player = Player(player1_img,TILESIZE+20, TILESIZE, 0,0)

class Platform(GameSprite):
    def __init__(self, platform_img, x, y):
        super().__init__(platform_img,TILESIZE, TILESIZE, x, y)
        platforms.add(self)

map = 1
with open(f"Map{map}.txt", "r") as file:
    if map == 2:
        bg_color = (7, 36, 82)
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
            elif symbol == 'K':
                Platform(platform4_img, x,y)
            elif symbol == 'M':
                Platform(platform5_img, x,y)
            elif symbol == 'N':
                Platform(platform6_img, x,y)
            elif symbol == 'C':
                GameSprite(point1_img, TILESIZE-5, TILESIZE-5, x,y)
                
            elif symbol == 'P':
                player.rect.centerx = x
                player.rect.centery = y
                player.start_x, player.start_y = x, y
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
    
    window.fill(bg_color)
    sprites.draw(window)
    sprites.update()
    display.update()
    clock.tick(FPS)