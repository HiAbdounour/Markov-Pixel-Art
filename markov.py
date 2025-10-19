import numpy as np
import pygame
pygame.init()

def convert_to_RGB(clr):
    c,m,y,k = clr
    c//=100
    m//=100
    y//=100
    k//=100
    return (255*(1-c)*(1-k),255*(1-m)*(1-k),255*(1-y)*(1-k))


def draw_pixel(window,pos,clr):
    clr = convert_to_RGB(clr)
    pygame.draw.rect(window,pygame.Color(clr),(pos[0],pos[1],50,50),0)
    pygame.display.flip()

def change_color(clr,M):
    new_clr = np.dot(M,np.array(list(clr)))
    return new_clr

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


window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Markov Pixel Art")

clr = (50,14,28,0)
i,j = 0,0

running = True
while running:
    if j!=500:
        draw_pixel(window,(i,j),clr)
        pygame.time.delay(1000)
        i+=50
        clr = change_color(clr,M)
        if i==500:
            i=0
            j+=50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()