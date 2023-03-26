from pygame import *
from time import time as time_count
from random import *

mixer.init()
window = display.set_mode((700, 600))
display.set_caption("Shooter")
background = transform.scale(image.load("maxresdefault-2-6.jpg"), (700, 600))
window.blit(background, (0, 0))
mixer.music.load("rick-136788.mp3")
# mixer.music.play()
clock = time.Clock

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size, player_speed=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


shot_time = time_count()
class Player(GameSprite):

    def update(self):
        pressed_keys = key.get_pressed()  # Отримати клавіші, які натиснуті
        if pressed_keys[K_a]:
            self.rect.x -= self.speed  # переміститися вгору
        if pressed_keys[K_d]:
            self.rect.x += self.speed
        if pressed_keys[K_SPACE]:
            bullets.add(Bullet)
            global shot_time
            if time_count() = shot_time >= 1:

            new_bullet = Bullet('', self.rect.x, self.rect.y, (10, 20), 7)
            bullets.append(bullet)
            shot_time = time_count()


class Bullet(GameSprite):

    def update(self):
        self.rect.y -= self.speed

class Enemie(GameSprite):

    def move(self):
        self.rect.y += self.speed

rocket = Player('', 250, 500, (60, 100), 5)
bullet = Bullet('',250, 480, (10, 20), 7)
game = True

bullet = sprite.Group()
 
enemie = sprite.Group()
enemie.add(Enemie(0, 0, (50, 50), 5))
counter = 1
while game:
    if len(enimes_group) < 7:
        new_enemy = Enemy('', randit(0,600), -100, (80, 50), 1)
        enemies_group.add(new_enemy6)

    if counter % 6 == 0:
        counter = 1
    else:
        counter += 1
    for e in event.get():
        if e.type == QUIT:
            game = False
    

    sprite.spritecollide()
    window.blit(background, (0, 0))
    rocket.update(bullets)
    rocket.draw_sprite()
    for bullet in bullets:
        bulet.move()
        bulet.draw

    enemie.update(bullets)
    for bullet in bullets:
        bullet.move()
        bullet.draw_sprite()
    rocket.draw_sprite()
    display.update()
    clock.tick(60)
