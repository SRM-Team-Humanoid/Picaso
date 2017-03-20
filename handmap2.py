#Controlling Drawing Arm with mouse
import math
import pypot.dynamixel
import time
import itertools
import math
import pygame
import sys
pygame.init()

size = width, height = 1365,767
screen = pygame.display.set_mode(size)
i=0
flag = False

ports = pypot.dynamixel.get_available_ports()

if not ports:
    raise IOError('no port found!')

print('ports found', ports)

print('connecting on the first available port:', ports[0])
dxl_io = pypot.dynamixel.DxlIO(ports[0])
ids = dxl_io.scan(range(1,5))
print(ids)

print(dxl_io.get_present_speed(ids))

def calc(x,y,z):
	l1 = 0.1065
	l2 = 0.08303+0.13482
	t = (x/math.sqrt(y**2+x**2))
	#print (t)
	b = x**2 + y**2 - (l1)**2 - (l2)**2
	c = x**2 + y**2 + (l1)**2 - (l2)**2
	d = 2*l1*math.sqrt(y**2+x**2)
	#e = ((x**2 + y**2 + (l1)**2 - (l2)**2 - (l3)**2)/2*l2*l3)
	#print(c/d)
	theta1 = ((180/math.pi)*(math.acos(t)-math.acos(c/d))-90)
	theta2 = -(180/math.pi)*(math.acos(b/(2*l1*l2)))
	#print("Theta1 = " + str(theta1) + " Theta2 = " + str(theta2)) 
	return theta1,theta2,0,z

dxl_io.set_moving_speed(dict(zip(ids, itertools.repeat(100))))

'''x = list(dxl_io.get_present_position(ids)) 
x[3] = -50
dxl_io.set_goal_position(dict(zip(ids, x)))
time.sleep(1)'''


def map(OldValuex,OldValuey):
	NewValuex = (((OldValuex) * (0.1638)) / (1365))
	NewValuey = (((767 - OldValuey) * (0.27204-0.15)) / (767)) + 0.15
	print(str(NewValuex) + ',' +str(NewValuey))
	return NewValuex,NewValuey

#n = raw_input()	
screen.fill((255,255,255))
pygame.display.update()
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag = True
		if event.type == pygame.MOUSEBUTTONUP:
			flag = False
			print "Stahp!"
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
			run == False
			pygame.quit()
			sys.exit()
			

	if flag:
		print "sup" 		
		Old = list(pygame.mouse.get_pos())
		pygame.draw.circle(screen,(0,0,0),(Old[0],Old[1]),3)
		new = map(Old[0],Old[1])
		#print (Old)
		#print (new)
		x = new[0]
		g = float("{0:.5f}".format(x))
		y = new[1]
		h = float("{0:.5f}".format(y))
		print(str(g) + ' ' + str(h))
	
		angles = calc(g,h,-23)
		print(angles)

		dxl_io.set_goal_position(dict(zip(ids, angles)))
		time.sleep(0.01)
	else:
		print "sdwn"		
		Old = list(pygame.mouse.get_pos())
		new = map(Old[0],Old[1])
		#print (Old)
		#print (new)
		x = new[0]
		g = float("{0:.5f}".format(x))
		y = new[1]
		h = float("{0:.5f}".format(y))
		print(str(g) + ' ' + str(h))
	
		angles = calc(g,h,-50)
		print(angles)

		dxl_io.set_goal_position(dict(zip(ids, angles)))
		time.sleep(0.01)
	pygame.display.update()
pygame.display.flip()

