from graphics import * 
import time
import random

def directionofbally(): #adds random movements on bounce to add difficulty
    global dy
    direction = random.randint(1,3)  
    if direction == 2:
        dy = -dy  

def directionofballx(): #adds random movements on bounce to add difficulty
    global dx
    direction = random.randint(1,3)
    if direction == 2:
        dx = -dx 

def savescore(score):
    f = open('scores.txt','a')
    f.write((str(score)+"\n"))  
    f.close

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    
def sortscores():
    sorts = []
    with open('scores.txt','r') as f:
        for line in f:
            sorts.append(int(line))
    sorts.sort(reverse=True)
    return sorts
        
def showscores(swin,sorts):
    num = 0
    tplace = 10
    
    p1 = Point(300,300)
    p2 = Point(400,400)
    button = Rectangle(p1,p2)
    button.setFill("green")
    button.draw(swin)
    bttext = Text(Point(350,350),"Return")
    bttext.draw(swin)
    
    for i in range(len(sorts)):
        if i < 5:
            num = num + 1
            tplace = tplace + 20
            temptxt = str(num) + "." + str(sorts[i])
            txt = Text(Point(150,tplace),temptxt)
            txt.draw(swin)
            
    exit = False
    while exit == False:
        mouse = swin.getMouse()
        x = mouse.getX()
        y = mouse.getY()
        if (p2.getX() > x > p1.getX()) and (p2.getY() > y > p1.getY()):
            exit = True
    clear(swin)
    titlescreen(swin)
        
def titlescreen(title):
    global restart 
    maintext = Text(Point(250,50),"Bounce the Ball")
    maintext.draw(title)
    p1 = Point(300,100)
    p2 = Point(400,200)
    p3 = Point(100,100)
    p4 = Point(200,200)
    p5 = Point(150,300)
    p6 = Point(350,400)
    
    button = Rectangle(p1,p2)
    button.setFill("green")
    button.draw(title)
    bttext = Text(Point(350,150),"Start Game")
    bttext.draw(title)
    
    buttone = Rectangle(p3,p4)
    buttone.setFill("red")
    buttone.draw(title)
    btetext = Text(Point(150,150),"Exit Game")
    btetext.draw(title)
    
    buttons = Rectangle(p5,p6)
    buttons.setFill("gold")
    buttons.draw(title)
    btstext = Text(Point(250,350),"Show High Scores")
    btstext.draw(title)
    
    start = False
    while start == False:
        mouse = title.getMouse()
        x = mouse.getX()
        y = mouse.getY()
        if (p2.getX() > x > p1.getX()) and (p2.getY() > y > p1.getY()):
            start = True
        elif (p4.getX() > x > p3.getX()) and (p4.getY() > y > p3.getY()):
            restart = False
            break
        elif (p6.getX() > x > p5.getX()) and (p6.getY() > y > p5.getY()):
            sortscores()
            sorts = sortscores()
            clear(title)
            showscores(title,sorts)
    if start == True: 
        clear(title)
        rungame(title)    
    
def rungame(win): 
    global dy
    global dx
    #win = GraphWin("Press s to begin", 500,500) #Creating window
    #Creating line 
    p = Point(250,100)
    p2 = Point(250,400)
    line = Line(p2,Point(350,400))
    line.setFill("blue")
    line.draw(win)
    #
    #Creating ball
    radius = 10 
    c = Circle(p,radius)
    c.setFill("blue")
    c.setOutline("blue")
    c.draw(win)
    #
    # Defines starting speed and direction of objects
    #mx = line speed dx/dy = ball speed
    dx = 1
    dy = 1
    score = 0
    directionofballx()
    directionofbally()
    mx = 2
    x  = 0.01
    #
    # While ball isn't touching the bottom, game should continue
    bottom = False
        
    while bottom == False:
        #Gets centre of each object then their edges
        c.move(dx,dy)
        cc = c.getCenter() #circle centre
        cx = cc.getX()
        cy = cc.getY()
        lc = line.getCenter() #line centre
        lx = lc.getX()
        ly = lc.getY()
        lleftedge = lx - 50 #lines left edge etc
        lrightedge = lx + 50
        leftedge = cx + radius #circles left edge etc
        rightedge = cx - radius
        topedge = cy - radius 
        bottomedge = cy + radius
        #
        #checks what direction the line should move
        k = win.checkKey()
        if k == 'Left':
            if (lleftedge > 0):
                if mx > 0:
                    mx = -mx
                    line.move(mx, 0)
        elif k == 'Right':
            if (lrightedge < 500):
                if mx < 0:
                    mx = -mx
                    line.move(mx, 0)
        else:
            if (lleftedge > 0) and (lrightedge < 500):
                line.move(mx,0)
        #checks if ball is on same y level as line, if so checks if its same x coords
        if (cy == 400):
            if ((lx - 50) <= cx <= (lx+50)):
                dy = -dy
                directionofballx()
                if dy >= 0:
                    if dy < 12:
                        dy = dy + 1
                elif dy <= 0:
                    if dy > -12:
                        dy = dy - 1
                score = score + 1
        #checks if ball is touching an edge, if so bounce random direction
        if (leftedge >= 500):
            dx = -dx
            directionofbally() 
        elif (rightedge <= 0):
            dx = -dx
            directionofbally()
        elif (topedge <= 0):
            dy = -dy
            directionofballx()
        elif (bottomedge > 500 ):
            bottom = True
        time.sleep(x)
    #prints score 
    scoretext = Text(Point(50,20), score)
    scoretext.draw(win)
    #Lets score display for short while, then restarts
    time.sleep(2.5)
    savescore(score)
    clear(win)
    titlescreen(win)

############### 
#Main code: Game restarts until user exits out of window
title = GraphWin("Bounce The Ball",500,500)
title.setBackground('pink')
restart = True
while restart == True:
    titlescreen(title)
title.close()
###############

