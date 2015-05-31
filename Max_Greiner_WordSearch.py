from Tkinter import *
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l = []
size = 0
def redrawAll():
    cellWidth = canvas.data.width / canvas.data.cols 
    cellHeight = canvas.data.height / canvas.data.rows
    canvas.data.cellWidth = cellWidth
    canvas.data.cellHeight = cellHeight


    canvas.delete(ALL)
    #draw the background
    canvas.create_rectangle(0, 0, canvas.data.width, canvas.data.height, fill = "black")
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
                canvas.create_rectangle(col * cellWidth,
                                        row * cellHeight,
                                        (col + 1) * cellWidth,
                                        (row + 1) * cellHeight,
                                        fill = "white")
                x1 = col * cellWidth
                x2 = (col + 1) * cellWidth
                y1 = row * cellHeight
                y2 = (row + 1) * cellHeight
                x3 = (x1+x2)/2
                y3 = (y1+y2)/2
                canvas.create_text(x3,y3 , text = canvas.data.board[col][row])

def addWords():
    for words in l:
        way = random.randint(1,1)
        if (way == 1):
            y= random.randint(0,len(words))
            x = random.randint(0,size-1)
            print y
            for letter in words:#goes through ever letter in the world
                canvas.data.board[x][y] = letter
                y+=1
                
         
            
            

def init():
    canvas.data.width = 600
    canvas.data.height = 600
    canvas.data.rows = size
    canvas.data.cols = size

    canvas.data.board = []
    
    for row in xrange(canvas.data.rows):
        next_row=[]
        for col in xrange(canvas.data.cols):
            next_row.append(alphabet[random.randint(0,len(alphabet) - 1)])
        canvas.data.board.append(next_row)
    addWords()
    

def run():
     print "run"
     global canvas  
     root=Tk()
     canvas=Canvas(width=600,height=600)
     canvas.pack()
     class Struct: pass
     canvas.data = Struct()
     init()
     redrawAll()
     root.mainloop()
     canvas.pack()


for x in xrange(20):
    words = (str(raw_input("What words would you like to enter in this word search: ")))
    if words == 'break':
        break
    else:
        l.append(words)
print l
sums = 0
for x in l:
    for y in x:
        sums+=1
while True:
    size = int(raw_input("What size would you like the word search to be: |||" + "minimum + " + str(sums) + ": " ))
    size1 = 0
    for words in l:
        for letters in words:
            size1+=1
    if size1<size**2:
        break
    else:
        print "there are to many words in this word search"
    

run()



