import math
from operator import truediv
import os
from re import T
import time
from turtle import forward, width
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def clearconsole():
    clear = "\n" * 100
    print (clear)

def writetxt(index , text, y):
    z = 0
    while z<len(text):
        y[index+z] = text[z]
        z = z+1

def makescreen(width, height):
    s = 0
    x = []
    y = []
    while s<width:
        if s %2 == 0:
            x.append("-")
        else:
            x.append('_')
        s = s+1
    i = 0
    while i<height:
        s = 0
        while s<width:
            if s == 0:
                if i == 0:
                    y.append('-_')
                else:
                    y.append('\n-_')
            elif s== width-3:
                y.append('_-')
            elif s < width-3:
                y.append(' ')

            s = s +1
        i = i +1
    return [x,y]
p = [116,105 ,109,101]    
def drawscreen(x,y,z):
	print(''.join(x))
	print(''.join(y))
	print(''.join(z))

def tocol(y,width,height):
	c =[]
	i=0
	k=0
	while i<height-2:
		c.append([])
		j=0
		while j<width-2:
			c[i].append(y[k])
			j += 1
			k += 1
		i += 1
		
	return c

def tononcol(y):
			nc=[]
			i = 0
			while i<len(y):
				j = 0
				while j<len(y[i]):
					nc.append(y[i][j])
					j += 1
				i += 1
			return nc

def obj(xo,yo,width,height,f,d):
    i =0
    k = 0

    if xo+1+i > width-5:
        f = False
    elif xo+1+i < 3:
        f = True
    if yo+k > height-4:
        d = False
    elif yo+k < 1:
        d = True
    if f:
        i +=1
    else:
        i -= 2
    if d:
        k +=1
    else:
        k -= 1
        
    return [yo+k,xo+1+i,f,d]
    

def sinx(xo,yo,width,height):
    j = makescreen(100,40)
    x = j[0]
    y = j[1]
    o1 = [0,0,True,True]
    o2 = [0,0,True,True]
    o3 = [0,0,True,True]
    o4 = [0,0,True,True]
    o5 = [0,0,True,True]
    o6 = [0,0,True,True]
    o7 = [0,0,True,True]


    y = tocol(y,100,40)
    i = 1
    k = 1
    f = True
    d = True

    r = 0
    while True:
        if r == 0:
            o1 = obj(42,3, width, height,f,d)
            o2 = obj(23,8, width, height,f,d)
            o3 = obj(86,17, width, height,f,d)
            o4 = obj(92,29, width, height,f,d)
            o5 = obj(64,34, width, height,f,d)
            o6 = obj(42,37, width, height,f,d)
            o7 = obj(7,11, width, height,f,d)

            r += 1
        else:
            o1 = obj(o1[1],o1[0], width, height,o1[2],o1[3])
            o2 = obj(o2[1],o2[0], width, height,o2[2],o2[3])
            o3 = obj(o3[1],o3[0], width, height,o3[2],o3[3])
            o4 = obj(o4[1],o4[0], width, height,o4[2],o4[3])
            o5 = obj(o5[1],o5[0], width, height,o5[2],o5[3])
            o6 = obj(o6[1],o6[0], width, height,o6[2],o6[3])
            o7 = obj(o7[1],o7[0], width, height,o7[2],o7[3])
        y[o1[0]][o1[1]] = 'V'
        y[o2[0]][o2[1]] = 'S'
        y[o3[0]][o3[1]] = 'A'
        y[o4[0]][o4[1]] = 'M'
        y[o5[0]][o5[1]] = 'B'
        y[o6[0]][o6[1]] = 'H'
        y[o7[0]][o7[1]] = 'A'
        y = tononcol(y)
        # time.sleep(0.01)
        cls()
        drawscreen(x,y,x) 
        y = j[1] 
        y = tocol(y,100,40)
        
       
     # r= width/c
    # i = 0
    # while i<100-xo: #y[Y-yo][X-xo]
    #     if y[]

    # math.sin()
    y = tononcol(y)
    time.sleep(0.05)
    cls()
    drawscreen(x,y,x)
    

sinx(0,20,100,40)