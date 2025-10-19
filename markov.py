import numpy as np
import pygame
pygame.init()

def init_clr():
    c,m,y,k = -1,-1,-1,-1
    try:
        c,m,y,k = input("Enter four values (between 0 and 100) separated by a comma : respectively cyan, magenta, yellow and black :").split(",")
    except ValueError:
        print("Please enter FOUR values")
        init_clr()
    else:
        try:
            c,m,y,k = int(c),int(m),int(y),int(k)
            if not(0<=c<=100 and 0<=m<=100 and 0<=y<=100 and 0<=k<=100):
                raise ValueError
            return (c,m,y,k)
        except ValueError:
            print("Please enter an integer between 0 and 100")
            init_clr()
        except Exception:
            print("Something goes wrong... Please retry\n")
            init_clr()

def convert_to_RGB(clr):
    c,m,y,k = clr
    c/=100
    m/=100
    y/=100
    k/=100
    return (255*(1-c)*(1-k),255*(1-m)*(1-k),255*(1-y)*(1-k))


def draw_pixel(window,pos,clr):
    clr = convert_to_RGB(clr)
    clr = [abs(clr[i]) for i in range(3)]
    pygame.draw.rect(window,pygame.Color(clr),(pos[0],pos[1],50,50),0)
    pygame.display.flip()

def change_color(clr,M):
    new_clr = np.dot(M,np.array(list(clr)))
    return new_clr

def break_stationary():
    N = np.array([[np.random.uniform(0.0,0.33) for j in range(4)] for i in range(3)])
    stocha = np.array([1-np.sum(N[:,j]) for j in range(4)])
    print(np.shape(stocha))
    # redimension for concatenation 
    stocha = np.reshape(stocha,(1,4))
    return np.concatenate((N,stocha))

# mathrix :  C M Y K
#        C   * * * *
#        M   * * * *
#        Y   * * * *
#        K   * * * *
M = break_stationary()
print(M)

clr = init_clr()
i,j = 0,0

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Markov Pixel Art")

running = True
while running:
    if j!=500:
        draw_pixel(window,(i,j),clr)
        pygame.time.delay(1000)
        i+=50
        clr = change_color(clr,M)
        if i%250==0:
            M = break_stationary()
            print(M,'\n')
        if i==500:
            i=0
            j+=50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()