from Tkinter import *






def timerFired():
    delay = 150 - canvas.data.updgradeAmounts[1]*10 
    canvas.data.counter +=1
    redrawAll()

    
    canvas.after(delay,timerFired)
    
    amount = 15 - canvas.data.updgradeAmounts[2]
    
    if canvas.data.counter%amount == 0:
        canvas.data.cookies+=canvas.data.updgradeAmounts[2]
   ## print canvas.data.updgradeAmounts
    
def mousePressed(event):
    if event.x>200 and event.x<300 and event.y>200 and event.y<300:
        canvas.data.cookies += canvas.data.updgradeAmounts[0]
    if event.x>450 and event.x<500 and event.y>450 and event.y<500:
        canvas.data.menu = not canvas.data.menu
    if event.x > 200 and event.x < 350 and event.y > 350 and event.y < 400 and canvas.data.menu == True and canvas.data.cookies > canvas.data.updgradeAmounts[0] * canvas.data.upgradeCost[0]:
        canvas.data.cookies -=  canvas.data.updgradeAmounts[0] * canvas.data.upgradeCost[0]
        canvas.data.updgradeAmounts[0] += 1
    if event.x > 200 and event.x < 350 and event.y > 400 and event.y < 450 and canvas.data.menu == True and canvas.data.cookies > canvas.data.updgradeAmounts[1] * canvas.data.upgradeCost[1]:
           canvas.data.cookies -=  canvas.data.updgradeAmounts[1] * canvas.data.upgradeCost[1]
           canvas.data.updgradeAmounts[1] += 1
    if event.x > 200 and event.x < 350 and event.y > 450 and event.y < 500 and canvas.data.menu == True and canvas.data.cookies > canvas.data.updgradeAmounts[2] * canvas.data.upgradeCost[2]:
        canvas.data.cookies -=  canvas.data.updgradeAmounts[2] * canvas.data.upgradeCost[2]
        canvas.data.updgradeAmounts[2] += 1
    if event.x > 0 and event.x < 50 and event.y>450 and event.y<500:
        canvas.data.updgradeAmounts = [1,0,1]
        
   

 
def redrawAll():
    canvas.delete(ALL)
    canvas.create_oval(200,200,300,300,fill = "black")
    canvas.create_text(200,19,text = "Cookies: ")
    
    canvas.create_text(250,20,text = canvas.data.cookies)

    offset = 50
    l = ["cliking production","steady rate","increasing amount"]
    if canvas.data.menu == True: ## set menu active
        canvas.create_rectangle(0,350,500,500, fill = "blue", outline = "white")
###UPGRADES
        xpos = 200
        y = 350
    
        
        for x in xrange(3):
            canvas.create_rectangle(xpos, y+(offset*x) , xpos + 150, y+(offset*x) + 50)
            canvas.create_text(xpos+75, y+(offset*x) + 25, text = l[x])
            
    
    canvas.create_rectangle(450,450,500,500,fill = "blue",outline = "white")
    canvas.create_text(475,475,text = "menu", fill = "white")
    y = 150
    for x in xrange(3):
        canvas.create_text(150,y+(offset*x), text = canvas.data.updgradeAmounts[x])
        canvas.create_text(80,y+(offset*x), text = l[x])
##cost
        canvas.create_text(440,y+(offset*x), text = "cost ")
        canvas.create_text(365,y+(offset*x), text = l[x])
        canvas.create_text(480,y+(offset*x), text = canvas.data.upgradeCost[x] *  canvas.data.updgradeAmounts[x])
        
    
    canvas.create_rectangle(0,450,50,500,fill = "blue",outline = "white")
    canvas.create_text(26,475,text = "reset", fill = "white")




def init():
    canvas.data.cookies = 1

    canvas.data.counter = 0
    canvas.data.menu = False

    canvas.data.autoclikingRate = 0
    canvas.data.updgradeAmounts = [0,0,0]
    canvas.data.upgradeCost = [32,31,37]
  
        


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
     root.bind('<Button-1>', mousePressed)
     root.mainloop()
     canvas.pack()
run()
