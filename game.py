import pygame


class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        # 0:idle 1:attack 2:hurt 3:dead
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # load images
        # load idle
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # load attack
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # load hurt
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f'img/{self.name}/Hurt/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # load dead
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'img/{self.name}/Dead/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self):
        screen.blit(self.image, self.rect)


# defining units
knight = Fighter(200, 260, "Knight", 60, 12, 3)
bandit1 = Fighter(550, 270, "Bandit", 30, 7, 1)
bandit2 = Fighter(650, 270, "Bandit", 30, 7, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 700
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

# load images
# background
backgroound_image = pygame.image.load('img/background/forest.jfif').convert_alpha()

# panel image
panel_image = pygame.image.load('img/background/panel.png').convert_alpha()


# create function for drawing text


# function for drawing background
def draw_bg():
    screen.blit(backgroound_image, (0, 0))
    screen.blit(panel_image, (-50, screen_height - bottom_panel))

    # draw units
    knight.update()
    knight.draw()

    for b in bandit_list:
        b.update()
        b.draw()


# run game constantly
run = True
while run:

    clock.tick(fps)

    # draw background
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
