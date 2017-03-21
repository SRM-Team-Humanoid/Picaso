#Plotting Pixel Values on Screen
import pygame
import time
import sys
from copy import deepcopy


f = open('G.txt','r')
g = [int(float(x)) for x in f.readline().split()]
f.close()	


f = open('X.txt','r')
x = [int(float(x)*3) for x in f.readline().split()]
f.close()	



f = open('Y.txt','r')
y = [int(float(y)*3) for y in f.readline().split()]
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
i = 0
for point in points:	
	#if g[i] == 1:
	print point
	pygame.draw.circle(screen,black,point,0)
	pygame.display.update()
	#i+=1
z = raw_input()
pygame.quit()
sys.exit()
