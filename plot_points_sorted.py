#Plotting In Sequence
import pygame
import time
import math
import sys

f = open('X.txt','r')
x = [int(float(x)*5) for x in f.readline().split()]
f.close()

f = open('G.txt','r')
g = [int(float(x)) for x in f.readline().split()]
f.close()


f = open('Y.txt','r')
y = [int(float(y)*5) for y in f.readline().split()]
f.close()

white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill(white)
pygame.display.update()
points = zip(x,y)

def euc(a,b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def near(z,points):
	points.remove(z)
	mind = 30000000000
	minp = 0
	for point in points:
		k = euc(z,point)
		if k<mind:
			mind = k
			minp = point
	return minp

point = points[0]
scale = 0
while len(points)!=1:
	pygame.draw.circle(screen,black,(point[0],point[1]+scale),1)
	pygame.display.update()
	point = near(point,points)
	#print scale	
	#scale *= 1	
	for event in pygame.event.get():
		if event == pygame.KEYDOWN:
			pygame.quit()
			sys.exit()

point = points[0]
print point
pygame.draw.circle(screen,black,point,1)
pygame.display.update()

z = raw_input()
pygame.quit()
sys.exit()
