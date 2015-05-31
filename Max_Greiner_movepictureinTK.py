from Tkinter import *
import random

def checkCollision():
    width = 700
    height = 500
    size = 20
    for c in xrange(canvas.data.amountofspawn):
        ##bottom use y
        if canvas.data.variabley[c] > height - size :
            canvas.data.direction[c] = 1
        ##right use x
        if canvas.data.variablex[c] > width - size:
            canvas.data.direction[c] = 4
        ##top use y
        if canvas.data.variabley[c] < 0:
            canvas.data.direction[c] = 3
        ##left use x
        if canvas.data.variablex[c] < 0:
            canvas.data.direction[c] = 2


def changeVar():
    speed = 15
    for x in xrange(canvas.data.amountofspawn):
        if canvas.data.direction[x] == 1: ##up
            canvas.data.variabley[x] -= speed
        elif canvas.data.direction[x] == 2: ##right
            canvas.data.variablex[x] += speed
        elif canvas.data.direction[x] == 3: ##down
            canvas.data.variabley[x] += speed
        elif canvas.data.direction[x] == 4: ##left
            canvas.data.variablex[x] -= speed


def changeDir():
    for x in xrange(canvas.data.amountofspawn):
        canvas.data.direction[x] = random.randint(1,4)
      
    
    
def timerFired():
   
################## DONE ################
    redrawAll()
    canvas.data.delay = 150 # milliseconds
    canvas.after(canvas.data.delay, timerFired)# pause, then call timerFired again
    if canvas.data.haventHitblock == False:
        canvas.data.counter += 1
        changeVar()
        checkCollision()
    if random.randint(0,100) > 75 and canvas.data.haventHitblock == False:
        changeDir()


        
        
  

def keyPressed(event):
    speed = 30
    if event.keysym == "Up" :#and canvas.data.starty > 7:
        canvas.data.starty-= speed
    elif event.keysym == "Down" :#and canvas.data.starty < 493:
        canvas.data.starty+= speed
    elif event.keysym == "Left" :#and canvas.data.startx > 7:
        canvas.data.startx-= speed
    elif event.keysym == "Right" :#and canvas.data.startx < 703:
        canvas.data.startx+= speed


    startx = canvas.data.startx
    starty = canvas.data.starty

    triggerx = canvas.data.trigerx
    triggery = canvas.data.trigery
    
    if startx + canvas.data.startsize < triggerx + canvas.data.trigersize and startx > triggerx and starty + canvas.data.startsize < triggery + canvas.data.trigersize and starty > triggery:
        canvas.data.haventHitblock = False


def redrawAll():
    canvas.delete(ALL)
 #   canvas.create_rectangle(0,0,700,500, fill = "blue")
    
    if canvas.data.haventHitblock == True:
            canvas.create_rectangle(canvas.data.trigerx, canvas.data.trigery, canvas.data.trigerx + canvas.data.trigersize, canvas.data.trigery+canvas.data.trigersize, fill = "red")

           
            canvas.create_image(canvas.data.startx,canvas.data.starty, image=canvas.data.img)
            ##canvas.create_rectangle(canvas.data.startx,canvas.data.starty,canvas.data.startx + canvas.data.startsize, canvas.data.starty + canvas.data.startsize, fill = "black")
    elif canvas.data.haventHitblock == False:
        varix = canvas.data.variablex
        variy = canvas.data.variabley
        size = 10 
        for x in xrange(canvas.data.amountofspawn):
            canvas.create_rectangle(varix[x], variy[x], varix[x] + size, variy[x] + size, fill = canvas.data.color[x])

        
                        
    
def init():
    width = 700
    height = 500
    canvas.data.startx = 350
    canvas.data.starty = 250
    canvas.data.startsize = 30

    canvas.data.trigersize = 100
    canvas.data.trigerx = width-20-canvas.data.trigersize
    canvas.data.trigery = height-20-canvas.data.trigersize


    canvas.data.haventHitblock = True

    canvas.data.amountofspawn = 1000
    canvas.data.variablex = []
    canvas.data.variabley = []
    canvas.data.direction = []
    canvas.data.colorchoice = ["red", "black", "purple", "pink", "brown"]
    canvas.data.color = []
    for x in xrange(canvas.data.amountofspawn):
        canvas.data.color.append(canvas.data.colorchoice[random.randint(0,len(canvas.data.colorchoice)-1)])
        canvas.data.direction.append(random.randint(1,4))

    canvas.data.counter = 0


    canvas.data.img = PhotoImage(file="head.gif")
    
    for x in xrange(canvas.data.amountofspawn):
        canvas.data.variablex.append(350 )
        canvas.data.variabley.append(250 )
        

 

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=700, height=500)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()


