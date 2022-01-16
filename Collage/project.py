import os
import random
import time
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
	
def changeani(height,x,y,z):
	i =1
	while i < height/3 + 2:
		cls()
		del y[0:303]
		x.insert(0,'\n')
		z.insert(0,'\b')
		drawscreen(x,y,z)
		i += 1
	cls()
def changeani2(width,height,x,y,z):
    i = 0
    y = tocol(y,width,height)
    while i<width/2:
        cls()
        x[i+1] = x[i]
        x[i] = ' '
        x[-2-i] = x[-1-i]
        x[-1-i] = ' '
        j=0
        while j<len(y):
            if i == 0:
                y[j][i] = '-_'
            y[j][i+1] = y[j][i]
            y[j][i] = ' '
            y[j][-2-i] = y[j][-1-i]
            y[j][-1-i] = ' '
            j += 1
        z[i+1] = z[i]
        z[i] = ' '
        z[-2-i] = z[-1-i]
        z[-1-i] = ' '
        print(''.join(x))
        j = 0
        while j<len(y):
            print(''.join(y[j]))
            j += 1
        print(''.join(z))
        i += 1

def changeani3(width,height,x,y,z):
    i = 0
    tx = []
    ty = []
    tz = []
    y = tocol(y,width,height)
    while i<width-1:
        tx.append(' ')
        tz.append(' ')
        i +=1
    
    i = 0
    while i<height-2:
        ty.append([])
        j = 0
        while j<width:
            ty[i].append(' ')
            j +=1
        i += 1
    tty = ty
    i = 0
    while i<max(width,height)-1:
        cls()
        print(''.join(tx))
        j = 0
        while j<len(ty):
            print(''.join(ty[j]))
            j += 1 
        print(''.join(tz))
        ty = tty
        tx[i] = x[i]
        tz[-1-i] = z[-1-i]
        k = 0
        while k<j:
            li = random.randint(0,height-3)
            el = random.randint(0,width-7)

            if y[li][el] == '\n-_':
                ty[li][0] = '-_'
                break
            ty[li][el] = y[li][el]
            if i<len(y):
                ty[i][0] = '-_'
                ty[-1-i][-1] = '_-'
            k += 1
        i += 1
    cls()
    y=tononcol(y)
    drawscreen(x,y,z)


def checkpass(user):
	j= makescreen(101,18)
	x = j[0]
	y = j[1]
	writetxt(137,title,y)
	writetxt(437,moto,y)
	if user !=''.join(chr(i)for i in p):
		writetxt(1026,'Incorrect Password Try Again',y)
		drawscreen(x,y,x)
		u = input()
		changeani(18,x,y,x)
		checkpass(u)
	else:
		writetxt(1033,'Welcome Back!',y)
		drawscreen(x,y,x)
		i = 0
		while i<30080000:
			i += 1
		changeani2(101,18,x,y,x)
		main()
		
def main():
    cls()
    j = makescreen(101,31)
    x = j[0]
    y = j[1]

    writetxt(10, 'HOW CAN I HELP YOU?', y)
    changeani3(101,31,x,y,x)


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
			
title = 'S H A D O W  H O T E L'
moto = 'Hotel Management'
i = 0

j = makescreen(101,18)
x = j[0]
y = j[1]
writetxt(137, title, y)
writetxt(437, moto, y)
writetxt(1032,'Enter Password',y)
x1= x
drawscreen(x,y,x)

user = input()

changeani(48,x,y,x)

checkpass(user)
