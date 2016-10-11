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



#importing Myro robot commands and opening simulator
from Myro import *
init("sim") #if sim is not already running

def sqside1(): #moving robot in big square
    penDown()
    wait(.5)
    forward(1,8)
    penUp()
    turnBy(270)
    
def sqside2(): #smaller middle square
    penDown()
    wait(.5)
    forward(1,5.4)
    penUp()
    turnBy(270)
    
def sqside3(): #smallest square
    penDown()
    wait(.5)
    forward(1,3)
    penUp()
    turnBy(270)
    
def triside1(): #side of triangle 
    wait(1)
    penDown()
    wait(.5)
    forward(1,3)
    penUp()
    turnBy(120)
    
def hexside1(): #side of hexagon
    penDown()
    wait(.5)
    forward(1,3)
    penUp()
    turnBy(60)


#moving to corner of first, biggest square
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

#drawing big square
sqside1()
sqside1()
sqside1()
sqside1()

#moving to corner of middle square
turnBy(-45)
forward(1,2)
turnBy(45)

#drawing small square
sqside2()
sqside2()
sqside2()
sqside2()

#moving to corner of smallest square
turnBy(-45)
forward(1,2)
turnBy(45)

#drawing smallest square
sqside3()
sqside3()
sqside3()
sqside3()

#clearing and restarting simulator
init("sim")

#drawing trianle
triside1()
triside1()
triside1()
    
#setting up and then drawing hexagon
turnBy(-100)
forward(1,1.2)
turnBy(100)
hexside1()
hexside1()
hexside1()
hexside1()
hexside1()
hexside1()
