import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge the Falling Blocks!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = -50
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(0, WIDTH - 50)

all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(5):
    block = Block()
    all_sprites.add(block)
    blocks.add(block)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.spritecollide(player, blocks, True):
        print("Game Over!")
        running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
