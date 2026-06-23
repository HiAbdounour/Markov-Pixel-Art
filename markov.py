import numpy as np
from random import random as rdm,uniform as unif,randint as rdt
import pygame
pygame.init()

def init_clr():
    r,g,b = -1,-1,-1
    try:
        r = int(input("Choose your initial value of red (between 0 and 255) : "))
        g = int(input("Choose your initial value of green (between 0 and 255) : "))
        b = int(input("Choose your initial value of blue (between 0 and 255) : "))
        RANGE = list(range(0,256))
        if r not in RANGE or g not in RANGE or b not in RANGE:
            raise ValueError
    except ValueError:
        print("Please enter values between 0 and 255\n")
        init_clr()
    except Exception:
        print("Something goes wrong... Please retry\n")
        init_clr()
    return np.array([r,g,b])

def draw_pixel(window,pos,clr):
    clrx = clr.tolist()
    clrx = [min(abs(elem),255) for elem in clrx]
    pygame.draw.rect(window,pygame.Color(clrx),(pos[0],pos[1],50,50),0)
    pygame.display.flip()

def change_color(clr,M):
    new_clr = np.dot(M,clr)
    return new_clr

def break_stationary():
    x = [rdm() for _ in range(3)]
    y = [unif(0,x[i]) for i in range(3)]
    z = [1-x[i]-y[i] for i in range(3)]

    Nx = [x,y,z]
    Nsh = np.array(Nx.pop(rdt(0,2)),dtype=float)
    Nsh = np.concatenate((Nsh,np.array(Nx.pop(rdt(0,1)),dtype=float)))
    N = np.concatenate((Nsh,np.array(Nx.pop(),dtype=float)))
    return N.reshape(3,3)

# mathrix :  R G B
#        R   * * *
#        G   * * *
#        B   * * *
M = break_stationary()

clr = init_clr()
i,j = 0,0

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Markov Pixel Art")

running = True
while running:
    if j!=500:
        draw_pixel(window,(i,j),clr)
        pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    M = break_stationary()

        i+=50
        clr = change_color(clr,M)
        if i==500:
            i=0
            j+=50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()