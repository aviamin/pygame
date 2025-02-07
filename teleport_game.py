import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game loop
clock = pygame.time.Clock()
running = True

x = 200
y= 200
jump = False
m = 1
v = 10


inventory = {
    "s_potion": 0
    }
inventory_y= 525


bg = pygame.image.load('sprites/background2.jpg')

def image_load(path, size):
    return pygame.transform.scale(pygame.image.load('sprites/'+path).convert_alpha(),size)


char = image_load('char.jpg',(48,48))
berube = image_load('berube.png',(48,60))
sprite = image_load('realsprite.png',(48,48))

character = [char,berube,sprite]
char_iteration = 0

while running:
    screen.fill(BLACK)
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x-=3
    if keys[pygame.K_d]:
        x+=3

        print(char_iteration)
        if char_iteration >= 9:
            char_iteration = 0
        screen.blit(character[char_iteration//3],(x,y))
        char_iteration+=1
    if jump == False:
        if keys[pygame.K_SPACE]:
            jump = True

    if jump == True:
            k = 0.5 * m * v**2  
            y -= k  
            v -= 1
            if v < 0:
                m = -1 
            if v == -11:
                m = 1 
                v = 10
                jump = False  

    pygame.draw.rect(screen,BLUE,(x,y,25,25))    

    #inventory
    pygame.draw.rect(screen, BLACK, (275, inventory_y, 50, 50), 6)
    pygame.draw.rect(screen, BLACK, (325, inventory_y, 50, 50), 6) 
    pygame.draw.rect(screen, BLACK, (375, inventory_y, 50, 50), 6) 
    pygame.draw.rect(screen, BLACK, (425, inventory_y, 50, 50), 6) 
    pygame.draw.rect(screen, BLACK, (475, inventory_y, 50, 50), 6) 

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()        
