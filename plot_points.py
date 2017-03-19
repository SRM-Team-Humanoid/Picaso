#Plotting Pixel Values on Screen
import pygame
import time
import sys
from copy import deepcopy

f = open('xf.txt','r')
x = [int(x) for x in f.readline().split()]
f.close()


f = open('yf.txt','r')
y = [int(y) for y in f.readline().split()]
f.close()

white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill(white)
pygame.display.update()
points = zip(x,y)
'''
thresh = (max(point[1] for point in points)+min(point[1] for point in points))/2
thresh = int(thresh)
print thresh

points2 = deepcopy(points)

points = [point for point in points if point[1]<thresh]
points = sorted(points, key=lambda e: (e[0]))

points2 = [point for point in points2 if point[1]>thresh]
points2 = sorted(points2, key=lambda e: (e[0]))

points.extend(points2[::-1])
'''
for point in points:
	pygame.draw.circle(screen,black,point,1)
	pygame.display.update()

z = raw_input()
pygame.quit()
sys.exit()
