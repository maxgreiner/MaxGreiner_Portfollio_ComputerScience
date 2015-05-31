from Tkinter import *
import random, time

def keyPressed(event):
    if canvas.data.bools == True:
        
        if event.keysym == "1":
            canvas.data.vsPlayer = True
            canvas.data.start = True
        elif event.keysym == "2":
            canvas.data.vsPlayer = False
            canvas.data.start = True
        canvas.data.bools = False
        time.sleep(3)
    if event.keysym == "Up":
        canvas.data.enemyy -= canvas.data.enemyspeed
    elif event.keysym == "Down":
        canvas.data.enemyy += canvas.data.enemyspeed
#    elif event.keysym == "p" and canvas.data.boools == True:
#        pause()
 #   elif event.keysym == "p" and canvas.data.boools == False:
#        unpause()
    elif event.keysym == "q" and canvas.data.vsPlayer == False:
        canvas.data.playery -= canvas.data.playerspeed
    elif event.keysym == "a" and canvas.data.vsPlayer == False:
        canvas.data.playery += canvas.data.playerspeed
    elif event.keysym == "space":
        reset()
    elif event.keysym == "r":
        init()
 
##def pause():
##    canvas.data.ballspeed = 0
##    canvas.data.enemyspeed = 0
##    canvas.data.playerspeed = 0
##    canvas.data.boools = False
##def unpause():
##    canvas.data.ballspeed = canvas.data.origianlballspeed
##    canvas.data.enemyspeed = canvas.data.origianlenemyspeed
##    canvas.data.playerspeed = canvas.data.origianlplayerspeed
##    canvas.data.boools = True
def redrawALL():
    width = 700
    height = 500
    
    canvas.delete(ALL)

    ###########INTRO
    string = "Enter which setting you would like to play in: (VS Computer (press 1)) || (VS Player (press 2)) )"
    if canvas.data.endgame == True:
        winner = "the winner is: "
        if canvas.data.enemyscore >= 10:
            winner += "player"
        elif canvas.data.playerscore >= 10:
            winner += "enemy"
        canvas.create_rectangle(0,0,width,height, fill = "black")
        canvas.create_text(width/2,height/2,text = winner, fill = "white" , font=("Helvetica", 32))
#        time.sleep(2)
        canvas.data.g2 = True
    elif canvas.data.g2 == True:
        resetGame()
    elif canvas.data.bools == True:
        canvas.create_rectangle(0,0,width,height, fill = "black")
        canvas.create_text(width/2 ,height/2,text = string, fill = "white", font=("Helvetica", 16))
    else:

        

        ##Backrgoundcanvas.data.lastpowerup
      
        canvas.create_rectangle(0,0,width,height, fill = "black")
        canvas.create_line(width/2 - 5, 0,width/2 + 5, height, fill = "white" )
        ##TEXT
        canvas.create_text(width/2,30,text = canvas.data.lastpowerup, fill = "white")
        
        ##Paddle
        canvas.create_rectangle(canvas.data.playerx,canvas.data.playery,canvas.data.playerx + 20,canvas.data.playery + canvas.data.playersize, fill = "white")
        ##Enemy Paddle
        canvas.create_rectangle(canvas.data.enemyx,canvas.data.enemyy,canvas.data.enemyx + 20,canvas.data.enemyy + canvas.data.enemysize, fill = "white")
         ##Ball
        canvas.create_oval(canvas.data.ballx,canvas.data.bally,canvas.data.ballx+canvas.data.ballsize,canvas.data.bally+canvas.data.ballsize, fill = "white", outline = "white")
        ##SCore
        canvas.create_text(width/2 - 150, 10, text = canvas.data.playerscore, fill = "white")

        canvas.create_text(width/2 + 150, 10, text = canvas.data.enemyscore, fill = "white")

        if canvas.data.powerbeingused == False:
            canvas.create_rectangle(canvas.data.randomx,canvas.data.randomy,canvas.data.randomx+canvas.data.randomsize,canvas.data.randomy+canvas.data.randomsize,fill = "red")
def move():
    canvas.data.ballx += (abs((canvas.data.ballspeed**2) - (canvas.data.incline**2) )**.5) * canvas.data.direction
    canvas.data.bally += canvas.data.incline 
    
def checkCollision():
    ##check player paddle
    
    if canvas.data.bally + canvas.data.ballsize > canvas.data.playery and canvas.data.bally < canvas.data.playery + canvas.data.playersize and canvas.data.ballx<canvas.data.playerx + 20 and canvas.data.ballx>canvas.data.playerx: 
        canvas.data.direction *= -1
        resetRandom()#for ball
    ##check enemy paddle
    if canvas.data.bally + canvas.data.ballsize > canvas.data.enemyy and canvas.data.bally < canvas.data.enemyy + canvas.data.enemysize and canvas.data.ballx + canvas.data.ballsize<canvas.data.enemyx + 20 and canvas.data.ballx+canvas.data.ballsize>canvas.data.enemyx:
        canvas.data.direction *= -1
        resetRandom()#for ball
## check outline
    ##check top
    if canvas.data.bally<0:
      canvas.data.incline *= -1
    ##check right
    elif canvas.data.ballx>700:
        scoreBoard(0)
    ##check bottom
    elif canvas.data.bally+canvas.data.ballsize>500:
      canvas.data.incline *= -1
    ##check left
    elif canvas.data.ballx + canvas.data.ballsize<0:
        scoreBoard(1)
    ##Check if hit random
    if canvas.data.bally + canvas.data.ballsize > canvas.data.randomy and canvas.data.bally < canvas.data.randomy + canvas.data.randomsize  and ((canvas.data.ballx > canvas.data.randomx and canvas.data.ballx < canvas.data.randomx + canvas.data.randomsize) or (canvas.data.ballx+canvas.data.ballsize > canvas.data.randomx and canvas.data.ballx+canvas.data.ballsize < canvas.data.randomx + canvas.data.randomsize)): # and canvas.data.powerUpinplay == True:
        canvas.data.powerUpinplay = False
        hitPowerUp()

def ballsizechange(player):
    changesize = 15
    canvas.data.ballsize += changesize
    canvas.data.lastpowerup = "ball enlarged"
    
def ballspeedchange(player):
    changespeed = 5
    canvas.data.ballspeed += changespeed
    
    canvas.data.playerspeed += changespeed * 2
    canvas.data.enemyspeed += changespeed * 2

    canvas.data.playersize += changespeed * 2
    canvas.data.enemysize += changespeed * 2
    canvas.data.lastpowerup = "ball speed up"
    
def PaddleEnlarge(player):
    changesize = 65
    if player == 0:
        canvas.data.playersize += changesize
        canvas.data.lastpowerup = "enemy enlarged"
    else:
        canvas.data.enemysize += changesize
        canvas.data.lastpowerup = "player enlarged"
    
def PaddleSpeedChange(player):
    changespeed = 55
 #   padlesspeed = [canvas.data.playerspeed, canvas.data.enemyspeed]
#    padlesspeed[player] += changespeed
    if player == 0:
        canvas.data.playerspeed += changespeed
        canvas.data.lastpowerup = "enemy paddle speed up"
    else:
        canvas.data.enemyspeed += changespeed
        canvas.data.lastpowerup = "player paddle speed up"
    
def hitPowerUp():
    ##Power Up Changed Variables
    ballincreasedspeed = 10
    poweruplist = [ballsizechange,ballspeedchange,PaddleEnlarge,PaddleSpeedChange] ## all names of powers ups must be functions
    randomness = random.randint(0,len(poweruplist)-1)
    player = 0
    if canvas.data.direction == 1: ##Player
          pass
    elif canvas.data.direction == -1:
        player = 1
    if canvas.data.powerbeingused == False:
        poweruplist[randomness](player)
    canvas.data.powerbeingused = True ##Enemy
        
    
def scoreBoard(x):
    if x == 0 and canvas.data.start == True:
        canvas.data.playerscore += 1
    elif x == 1 and canvas.data.start == True:
        canvas.data.enemyscore += 1
    if canvas.data.enemyscore >= 10 or canvas.data.playerscore >= 10:
        canvas.data.endgame = True
    restartRound()
    reset()
    
    
def moveAI():
        width = 700
        height = 500
        deadzone = 150
        if (abs(canvas.data.bally - canvas.data.playery)) < canvas.data.ballsize and canvas.data.ballx < width / 2: ## if ball is in position to hit(to avoid constant up and down)
            pass
        elif canvas.data.bally + (canvas.data.ballsize/2) > canvas.data.playery + (canvas.data.playersize/2) and canvas.data.ballx < width / 2 :
            canvas.data.playery += canvas.data.playerspeed - (canvas.data.playerspeed - canvas.data.difficulty )
        elif canvas.data.bally + (canvas.data.ballsize/2) < canvas.data.playery + (canvas.data.playersize/2) and canvas.data.ballx < width/ 2:
               canvas.data.playery -= canvas.data.playerspeed - (canvas.data.playerspeed - canvas.data.difficulty )
        elif canvas.data.ballx>width/2 and canvas.data.playery > deadzone:
            canvas.data.playery -= canvas.data.playerspeed - (canvas.data.playerspeed - canvas.data.difficulty )
        elif canvas.data.ballx>width/2 and canvas.data.playery < height - deadzone  :
            canvas.data.playery += canvas.data.playerspeed - (canvas.data.playerspeed - canvas.data.difficulty )
                          
        ## if ball is on other side and the y of the paddle if in the corners of the screen that go to the center
def increaseSpeeds():
    print "increase speeds"
    increasespeed = 1
    canvas.data.ballspeed += increasespeed
    
    canvas.data.playerspeed += increasespeed  * 5
    canvas.data.enemyspeed += increasespeed * 5

    canvas.data.playersize += increasespeed * 5
    canvas.data.enemysize += increasespeed * 5
    


def restartRound():
    width = 700
    height = 500

    canvas.data.incline = 0
    
    canvas.data.playerx = 10
    canvas.data.playery = height/2
    canvas.data.playersize = canvas.data.originalplayersize
    canvas.data.playerspeed = canvas.data.originalplayerspeed

    canvas.data.enemyy = height/2
    canvas.data.enemyx = width - 27
    canvas.data.enemysize = canvas.data.originalenemysize
    canvas.data.enemyspeed = canvas.data.originalenemyspeed

    canvas.data.ballx = width/2
    canvas.data.bally = height/2
    canvas.data.ballsize = canvas.data.originalballsize
    canvas.data.ballspeed = canvas.data.origianlballspeed 


def resetValues():
    canvas.data.playersize = canvas.data.originalplayersize
    canvas.data.playerspeed = canvas.data.originalplayerspeed
    
    canvas.data.enemysize = canvas.data.originalenemysize
    canvas.data.enemyspeed = canvas.data.originalenemyspeed

    canvas.data.ballsize = canvas.data.originalballsize
    canvas.data.ballspeed = canvas.data.origianlballspeed 

def resetGame():
    resetValues()
    canvas.data.playerscore = 0
    canvas.data.enemyscore = 0
    canvas.data.endgame = False
    
def setRandom():
    width = 700
    height = 500
    randomy = random.randint((height/2) - 150, (height/2) + 150)
    randomx = random.randint((width/2) - 150, (width/2) + 150)
    #####
    canvas.data.randomx = randomx
    canvas.data.randomy = randomy
    canvas.data.powerUpinplay = True
        
def timerFired():
    redrawALL()
    canvas.after(5, timerFired)
    canvas.data.counter+=1
    checkCollision()
    move()
    if canvas.data.counter%1000 == 0 and canvas.data.start==True:
        canvas.data.counter = 0
        increaseSpeeds()
    if random.randint(0,100) >= 85 and canvas.data.powerUpinplay == False:
        setRandom()
        
    if canvas.data.vsPlayer == True:
        moveAI()
    if canvas.data.powerbeingused == True:
        canvas.data.counter += 1
    if canvas.data.counter > canvas.data.poweruptime and canvas.data.powerbeingused == True:
        canvas.data.counter = 0
        canvas.data.powerbeingused = False
        resetValues()
        canvas.data.lastpowerup = "None"

def reset():
     width = 700
     height = 500
     canvas.data.ballx = width/2
     canvas.data.bally = height/2
     canvas.data.direction *= -1
    
        
def resetRandom():
    canvas.data.incline = random.randint(-(canvas.data.ballspeed - 1),canvas.data.ballspeed - 1)

def init():
    width = 700
    height = 500
    ##original values
    canvas.data.originalplayersize = 85
    canvas.data.originalplayerspeed = 30
    
    canvas.data.originalenemysize = 85
    canvas.data.originalenemyspeed = 30
    
    canvas.data.origianlballspeed = 7
    canvas.data.originalballsize = 25
    
    ##player
    canvas.data.playerx = 10
    canvas.data.playery = height/2
    canvas.data.playersize = canvas.data.originalplayersize
    canvas.data.playerspeed = canvas.data.originalplayerspeed
    
    ##enemy
    canvas.data.enemyy = height/2
    canvas.data.enemyx = width - 27
    canvas.data.enemysize = canvas.data.originalenemysize
    canvas.data.enemyspeed = canvas.data.originalenemyspeed

    ##Ball
    canvas.data.ballx = width/2
    canvas.data.bally = height/2
    canvas.data.ballsize = canvas.data.originalballsize
    canvas.data.ballspeed = canvas.data.origianlballspeed 
    canvas.data.direction = -1 

    ##random
    resetRandom()
    ##Score
    canvas.data.enemyscore = 0
    canvas.data.playerscore = 0

    canvas.data.bools = True
    canvas.data.buttonPressed = False
    ##AI
    canvas.data.vsPlayer = False
    canvas.data.difficulty = 5
    
    ##FOR Power UPS TO WORK
    canvas.data.powerUpinplay = False
    canvas.data.randomx = -100
    canvas.data.randomy = - 100
    canvas.data.randomsize = 25
    canvas.data.powerbeingused = False
    canvas.data.counter = 0
    canvas.data.poweruptime = 600
    canvas.data.lastpowerup = ""

    ##end and restart
    canvas.data.endgame = False
    canvas.data.g2 = False
    canvas.data.boools = True
    ##START
    canvas.data.start = False
    canvas.data.counter = 0
    

def main():
    global root
    root = Tk()
    global canvas
    canvas = Canvas(root, width = 700, height = 500)
    canvas.pack()
    class Struct(): pass
    canvas.data = Struct()
    init()
    timerFired()
    root.bind("<Key>",keyPressed)
    root.mainloop()


main()
