import turtle
import random

pencere = turtle.Screen()
pencere.screensize(600,600)
pencere.title("Kaplumbağaları Yakala")
pencere.bgcolor('blue')

oyuncu = turtle.Turtle()
oyuncu.color('white')
oyuncu.shape('triangle')
oyuncu.shapesize(3)
oyuncu.penup()

speed = 2

def solaDon():
    oyuncu.left(30)
    
def sagaDon():
    oyuncu.right(30)
    
def hiziArtir():
    global speed
    speed = speed + 1

def hiziAzalt():
    global speed
    speed = speed - 1
pencere.listen()
pencere.onkey(solaDon,'Left')
pencere.onkey(sagaDon,'Right')
pencere.onkey(hiziArtir,'Up')
pencere.onkey(hiziAzalt,'Down')

maxHedef = 5
hedefler = []
for i in range(maxHedef):
    hedefler.append = turtle.Turtle()
    hedefler[i].penup()
    hedefler[i].color("yellow")
    hedefler[i].shape('turtle')
    hedefler[i].speed(0)
    hedefler[i].setposition(random.randint(-300,300),random.randint(-300,300))
while True:
    oyuncu.forward(speed)
    

    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)
    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)
        
        for i in range(maxHedef):
            hedefler[i].forward(1)

    if oyuncu.distance(hedefler) < 40:
        hedefler.setposition(random.randint(-300,300),random.randint(-300,300))
            