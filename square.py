#importing Myro robot commands and opening simulator
from Myro import *
init("sim") # if sim is not already running
# that was just set up now starting movement commands

def sqside1(): #moving robot in big square
    penDown()
    wait(.5)
    forward(1,8)
    penUp()
    turnBy(270)
    
def sqside2(): #smaller square
    #smaller
    

penUp()
backward(1,1.5)
wait(1)
turnBy(90)
forward(1,1)
forward(1,1)
forward(1,1)
forward(1,1)
wait(1)
turnBy(270)

#about to draw big swuare
sqside1()
sqside1()
sqside1()
sqside1()

#about to draw small square
sqside2()
sqside2()
sqside2()
sqside2()


#
init("sim")
turnBy(225)
forward(1,1.8)
turnBy(45)
penDown("red")
forward(1,5.4)
penUp()
turnBy(270)
penDown("red")
forward(1,5.4)
penUp()
turnBy(270)
penDown("red")
forward(1,5.4)
penUp()
turnBy(270)
penDown("red")
forward(1,5.4)
penUp()
turnBy(270)
forward(1,2.7)
turnBy(300)
penDown()
forward(1,5)
turnBy(240)
forward(1,5)
turnBy(240)
forward(1,5)
