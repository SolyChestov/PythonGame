from pygame import *
from map import make_map
mixer.init()
window = display.set_mode((700, 600))
display.set_caption("Лабіринт")
background = transform.scale(image.load("resources/background.jpg"), (700, 600))
window.blit(background, (0, 0))
mixer.music.load("resources/jungles.ogg")
# mixer.music.play()
kick = mixer.Sound("resources/kick.ogg")  # Sound - окремий звук
money = mixer.Sound("resources/money.ogg")
clock = time.Clock()
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):

    def update(self):
        pressed_keys = key.get_pressed()  # Отримати клавіші, які натиснуті
        if pressed_keys[K_w]:
            self.rect.y -= self.speed  # переміститися вгору
        if pressed_keys[K_s]:
            self.rect.y += self.speed
        if pressed_keys[K_a]:
            self.rect.x -= self.speed  # переміститися вгору
        if pressed_keys[K_d]:
            self.rect.x += self.speed

    def touch(self, sprite):
        # colliderect - функція, що перевіряє зіткенння ректів (прямокутників)
        return self.rect.colliderect(sprite.rect)


class Enemy(GameSprite):

    def update(self, x1, x2):
        # Якщо кіборг підходить до граничних точок
        if self.rect.x <= x1 or self.rect.x + self.rect.width >= x2:
            # Змінити його напрямок
            self.speed *= -1
        self.rect.x += self.speed


hero = Player('resources/hero.png', 0, 0, 5)
hero.draw_sprite()
cyborg = Enemy('resources/cyborg.png', 470, 300, 2)
cyborg.draw_sprite()
treasure = GameSprite('resources/treasure.png', 580, 480)
treasure.draw_sprite()

game_map = make_map()  # створюю карту make_map повертає список прямокутників, в яких вже є розмір і кординати

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    # Рух
    hero.update()
    cyborg.update(450, 650)
    # Взаємодія
    # Малювання графіки
    if hero.touch(cyborg):                                  #
        hero.rect.x = 0
        hero.rect.y = 0
        kick.play()
    window.blit(background, (0, 0))  # фон
    for block in game_map:
        # якщо хітбокс героя торкнувся стінки
        if hero.rect.colliderect(block):                    #
            hero.rect.x = 0
            hero.rect.y = 0
        draw.rect(window, (255, 255, 0), block)
    hero.draw_sprite()
    cyborg.draw_sprite()
    treasure.draw_sprite()
    display.update()
    clock.tick(60)