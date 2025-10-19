import numpy as np
import pygame
pygame.init()


def draw_pixel(window,pos,clr):
    pygame.draw.rect(window,pygame.Color(clr),(pos[0],pos[1],50,50),0)
    pygame.display.flip()

# mathrix :  C M Y K
#        C   * * * *
#        M   * * * *
#        Y   * * * *
#        K   * * * *
M = np.array([
     [0.2,0.2,0.30,0.1],
     [0.2,0.3,0.05,0.2],
     [0.4,0.0,0.50,0.0],
     [0.2,0.5,0.15,0.7]
])

clr_0 = (50,14,28,0)

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Markov Pixel Art")

draw_pixel(window,(0,0),clr_0)

running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()