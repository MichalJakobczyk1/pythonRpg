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


class HealthBar():
    def __init__(self, x, y ,hp ,max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp/self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, ratio * 150, 20))


# game window
bottom_panel = 150
screen_width = 700
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')
clock = pygame.time.Clock()
fps = 60

# defining units
knight = Fighter(200, 260, "Knight", 60, 12, 3)
bandit1 = Fighter(550, 270, "Bandit", 30, 7, 1)
bandit2 = Fighter(650, 270, "Bandit", 30, 7, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(450, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(450, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)

pygame.init()

# define fonts
font = pygame.font.SysFont('Times New Roman', 26)

# define colors
red = (255, 0, 0)
green = (0, 255, 0)

# load images
# background
backgroound_image = pygame.image.load('img/background/forest.jfif').convert_alpha()

# panel image
panel_image = pygame.image.load('img/background/panel.png').convert_alpha()


# create function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing background
def draw_bg():
    screen.blit(backgroound_image, (0, 0))
    screen.blit(panel_image, (-50, screen_height - bottom_panel))


def draw_panels():
    # knight stats
    draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height - bottom_panel + 10)
    for count, i in enumerate(bandit_list):
        # show name and hp
        draw_text(f'{i.name} HP: {i.hp}', font, red, 450, (screen_height - bottom_panel + 10) + count * 60)


# draw units
def draw_units():
    knight.update()
    knight.draw()

    for b in bandit_list:
        b.update()
        b.draw()


# run game constantly
run = True
while run:

    clock.tick(fps)

    # draw functions
    draw_bg()
    draw_units()
    draw_panels()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

print(pygame.font.get_fonts())
