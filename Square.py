#first line
from Myro import *
init("sim") #only if sim is not open
def move1(): #move the robot forward then right
    penDown()
    forward(4,1)
    penUp()
    turnBy(15)
    turnBy(15)
    turnBy(15)
    turnBy(15)
    turnBy(15)
    turnBy(15)
move1()