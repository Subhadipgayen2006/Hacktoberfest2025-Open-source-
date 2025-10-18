import pygame, sys
pygame.init()

W, H = 800, 400
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("🏃 Gravity Runner")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)
GROUND = 300

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(midbottom=(100, GROUND))
        self.vel_y = 0
        self.jump_power = -15
        self.gravity = 0.8

    def update(self, keys):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.vel_y = 0
        if keys[pygame.K_SPACE] and self.rect.bottom == GROUND:
            self.vel_y = self.jump_power

player = Player()
all_sprites = pygame.sprite.Group(player)

while True:
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update(keys)

    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, (0, GROUND, W, H-GROUND))
    all_sprites.draw(win)
    pygame.display.flip()
    clock.tick(60)
