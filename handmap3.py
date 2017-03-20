#Reading Pixel Coordinates from file and writing to Drawing Arm
import math
import pypot.dynamixel
import time
import itertools
import math
import pygame
import sys

ob = open('xz.txt','r')
x = [int(x) for x in ob.readline().split()]
#x = x[:-45]
ob.close()
ob = open('yz.txt','r')
y = [int(y) for y in ob.readline().split()]
#y = y[:-45]
ob.close()
coord = list(zip(x,y))
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

#print(dxl_io.get_present_speed(ids))

def calc(x,y,z):
	l1 = 0.1085
	l2 = 0.08305+0.13482
	t = (x/math.sqrt(y**2+x**2))
	#print (t)
	b = x**2 + y**2 - (l1)**2 - (l2)**2
	c = x**2 + y**2 + (l1)**2 - (l2)**2
	d = 2*l1*math.sqrt(y**2+x**2)
	#e = ((x**2 + y**2 + (l1)**2 - (l2)**2 - (l3)**2)/2*l2*l3)
	print(c/d)
	theta1 = ((180/math.pi)*(math.acos(t)-math.acos(c/d))-90)
	theta2 = -(180/math.pi)*(math.acos(b/(2*l1*l2)))
	#print("Theta1 = " + str(theta1) + " Theta2 = " + str(theta2)) 
	return theta1,theta2,0,z

#dxl_io.set_moving_speed(dict(zip(ids, itertools.repeat(200))))

resx = float(input("x resolution: "))
resy = float(input("y resolution: "))
i = float(input("Magnificaion: "))

def map(OldValuex,OldValuey):
	global resx
	global resy
	global i
	NewValuex = (((OldValuex) * (resx/10000*i)) / (resx))
	NewValuey = (((resy - OldValuey) * (resy/10000*i)) / (resy)) + 0.15
	print(str(NewValuex) + ',' +str(NewValuey))
	return NewValuex,NewValuey



run = True
oldcord = [0,0]

x = list(dxl_io.get_present_position(ids)) 
x[3] = -35
dxl_io.set_goal_position(dict(zip(ids, x)))
time.sleep(0.5)
g,h = map(coord[0][0],coord[0][1])
angles = calc(g,h,-35)
print(angles)
dxl_io.set_goal_position(dict(zip(ids, angles)))
time.sleep(0.5)

for cord in coord:
		
	if cord[0]-oldcord[0]>30 or cord[1]-oldcord[1]>30:
		x = list(dxl_io.get_present_position(ids)) 
		x[3] = -35
		dxl_io.set_goal_position(dict(zip(ids, x)))
		time.sleep(0.5)	
	
		new = map(cord[0],cord[1])
		x = new[0]
		y = new[1]
		#h = float("{0:.5f}".format(y))
		print(str(x) + ' ' + str(y))
		
		angles = calc(x,y,-35)
		print(angles)
		
		dxl_io.set_goal_position(dict(zip(ids, angles)))
		time.sleep(1)
		
	new = map(cord[0],cord[1])
	x = new[0]
	g=x
	#g = float("{0:.5f}".format(x))
	y = new[1]
	h=y
	#h = float("{0:.5f}".format(y))
	print(str(g) + ' ' + str(h))
	
				
	angles = calc(g,h,-22)
	print(angles)
	dxl_io.set_goal_position(dict(zip(ids, angles)))
	time.sleep(0.01)
	
	oldcord = cord

