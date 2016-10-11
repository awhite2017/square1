#first line
from Myro import *
init("sim") #only if sim is not open

turnBy(180)
forward(1,1)
turnBy(90)
forward(2,1)
turnBy(90)
def movesquare(): #move for the square    
    penDown()
    forward(4,1)
    forward(4,.6)
    penUp()
    turnBy(90)#move the second part of the square
     
def pentagon(): #writes a hexagon  
    penDown()
    forward(3,1)
    penUp()
    turnBy(288)
    
def triangle(): #create triangle
    penUp()
    turnBy(253)
    forward(1,1)
    penDown()
    forward(2,1)
    
movesquare() #moves square
movesquare()
movesquare()
movesquare()

forward(.5,1) #get ready for pentagon
turnBy(90)
forward(3.5,1)
turnBy(308)

pentagon() #move pentagon
pentagon()
pentagon()
pentagon()
penDown()
forward(3,1)
triangle()
triangle()
triangle()
penUp()

    


