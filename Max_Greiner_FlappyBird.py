from Tkinter import *
import random





def timerFired():
    delay = 80
    canvas.after(delay,timerFired)
    canvas.data.counter+=1
    redrawAll()
    ## if jumping then no more falling
    if canvas.data.jump==False:
        gravity()
    canvas.data.jump = False
    ## you died
    if canvas.data.birdy>canvas.data.screenHeight:
        canvas.data.score=0
        

     
    if canvas.data.brickx<0:
        canvas.data.whiteBricky=random.randint(0,canvas.data.screenHeight-canvas.data.whiteBrickSize)
        canvas.data.brickx=canvas.data.screenWidth
        ##if bird is in between bricks or detection area
    if canvas.data.birdx>=canvas.data.brickx and canvas.data.birdx<=canvas.data.brickx+canvas.data.brickWidth:
        
        if canvas.data.birdy >= canvas.data.whiteBricky and canvas.data.birdy<=canvas.data.whiteBricky+canvas.data.whiteBrickSize:

                
                canvas.data.score+=1
           

        else:
             canvas.data.score = 0
            

         
        
        

def blocks():
    canvas.create_rectangle(0)

def redrawAll():
    canvas.delete(ALL)
    ###BACKGROUNG
    canvas.create_rectangle(0,0,canvas.data.screenWidth,canvas.data.screenHeight/2,fill="light blue")   
    canvas.create_rectangle(0,canvas.data.screenHeight/2,canvas.data.screenWidth,canvas.data.screenHeight, fill = "dark green",width = 0)
        ##score
    canvas.create_text(10,10,text = canvas.data.score/3, fill = "black")
##############################BRICK CODE######################################
    ####green block
    canvas.create_rectangle(canvas.data.brickx,0,canvas.data.brickx+canvas.data.brickWidth,canvas.data.screenHeight, fill = "green",width=0)
    #####white block
    canvas.create_rectangle(canvas.data.brickx,canvas.data.whiteBricky,canvas.data.brickx+canvas.data.brickWidth,canvas.data.whiteBricky+canvas.data.whiteBrickSize,fill="white",width = 0)
    canvas.data.brickx-=canvas.data.brickSpeed
     ####BIRD
    canvas.create_oval(canvas.data.birdx+canvas.data.size,canvas.data.birdy+canvas.data.size,canvas.data.birdx+canvas.data.size-5,canvas.data.birdy+canvas.data.size-5,fill = "yellow",width=0)
    canvas.create_oval(canvas.data.birdx,canvas.data.birdy,canvas.data.birdx+canvas.data.size,canvas.data.birdy+canvas.data.size,fill = "yellow",width=0)
#####STARS 

    
        

def keyPressed(event):
    if event.keysym == "space":
        hop()
    if event.keysym == "g " and canvas.data.toogle == True:
        canvas.data.fall == False
        canvas.dara.toogle=False
    if event.keysym == "g " and canvas.data.toogle == False:
        canvas.data.fall == True
        canvas.dara.toogle=True
    if event.keysym == "s":
        canvas.data.brickSpeed = 15
        canvas.data.fall = True
    elif event.keysym == "Right":
        canvas.data.brickSpeed += 2
        print "speed up"
    elif event.keysym =="Left":
        canvas.data.brickSpeed -= 2
        print "slow down"
def gravity():
    if canvas.data.fall == True:
        canvas.data.birdy+=canvas.data.jumpHeight

def hop():
    canvas.data.birdy-=canvas.data.jumpHeight*4 
    redrawAll()
def init():
    canvas.data.toogle = False
    canvas.data.fall = False
    canvas.data.scored=True
    canvas.data.score = 0
    canvas.data.color = "light blue"
    canvas.data.brickWidth = 50
    canvas.data.brickSpeed = 0 # 15 is default
    canvas.data.whiteBrickSize = 150
    canvas.data.counter=0
    canvas.data.createStars = 10
    canvas.data.screenWidth=500
    canvas.data.screenHeight=500
    canvas.data.whiteBricky=random.randint(25,canvas.data.screenHeight-canvas.data.whiteBrickSize)
    canvas.data.brickx = canvas.data.screenWidth
    canvas.data.birdx=200
    canvas.data.birdy=300
    canvas.data.size=30
    canvas.data.jumpHeight = 15
    canvas.data.jump=False
    

def run():
     print "run"
     global canvas  
     root=Tk()
     canvas=Canvas(width=500,height=500)
     canvas.pack()
     class Struct: pass
     canvas.data = Struct()
     init()
     redrawAll()
     timerFired()
     root.bind("<Key>", keyPressed)
     root.mainloop()
     canvas.pack()
print "flappy bird:    ", "Press G to start:", "INSTRUCTIONS: press  'space' to jump and move to the white areas. Missing the white squares resets the score to zero"
run()
