import pygame
import math
import numpy as np

FPC = 30
W = 700
H = 700

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Life')

def putpixel(x,y,m,w=700,h=700):
    pygame.draw.rect(sc, (255,255,255), (round(x*m)+round(w/2),round(y*m)+round(h/2),1,1))
if __name__ == "__main__":
    while True:    
        clock.tick(FPC)
        for j in [1000,800,600,400,200,100,90,80,70,60,50,40,30,20,10,8,6,4,2,1]:
            pygame.draw.rect(sc, (0, 0, 0), (0, 0, W, H))
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
            for i in range(100000):
                x = i * math.cos(i)
                y = i * math.sin(i)
                putpixel(x,y,j/100)
            pygame.display.update()
            # pygame.time.delay(500)
        pygame.display.update()