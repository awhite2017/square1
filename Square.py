#first line
from Myro import *
init("sim") #only if sim is not open
def movesquare(): #move for the square
    turnBy(180)
    forward(1,1)
    turnBy(90)
    forward(2,1)
    turnBy(90)
    penDown()
    forward(4,1)
    forward(4,.6)
    penUp()
    turnBy(90)#move the second part of the square
    penDown()
    forward(4,1)
    forward(4,.6)
    penUp()
    turnBy(90) #move the third part of the square
    penDown()
    forward(4,1)
    forward(4,.6)
    penUp()
    turnBy(90) #last move for the square
    penDown()
    forward(4,1)
    forward(4,.6)
    penUp()
    turnBy(90) #square complete
movesquare()
def pentagon(): #writes a hexagon 
    forward(.5,1)
    turnBy(90)
    forward(3.5,1)
    turnBy(308)
    penDown()
    forward(3,1)
    penUp()
    turnBy(288)
    penDown()
    forward(3,1)
    penUp()
    turnBy(288)
    penDown()
    forward(3,1)
    penUp()
    turnBy(288)
    penDown()
    forward(3,1)
    penUp()
    turnBy(288)
    penDown()
    forward(3,1)
pentagon()
def triangle(): #create triangle
    penUp()
    turnBy(253)
    forward(1,1)
    penDown()
    forward(2,1)
    penUp()
    turnBy(240)
    penDown()
    forward(2,1)
    penUp()
    turnBy(240)
    penDown()
    forward(2,1)
    penUp()
triangle()

    


