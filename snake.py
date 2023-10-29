#2023 LandinBT
import turtle
import time
import random

#Const
SLOW=0.13

#Window
wn=turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#--Snake--
#head
head=turtle.Turtle()
head.speed(0)
head.shape("square") #form
head.color("green")
head.penup() #erace trace
head.goto(0,0) #window pos
head.direction="stop"

#body
body=[] #init body

#--Food--
food=turtle.Turtle() #init head
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(200,100)

#--Score--
score=turtle.Turtle()
score.speed(0)

#Functions
def toUp():
    head.direction="up"

def toDown():
    head.direction="down"

def toRight():
    head.direction="right"

def toLeft():
    head.direction="left"

def mov():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

#Keyboard input
wn.listen()
wn.onkeypress(toUp, "Up")
wn.onkeypress(toDown, "Down")
wn.onkeypress(toRight, "Right")
wn.onkeypress(toLeft, "Left")

while True:
    wn.update()

    #Colisiones bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(0.5) #pause
        head.goto(0,0)
        head.direction="stop"
        #Reiniciar cuerpo
        for segment in body:
            #Eliminar segmentos
            #body.remove()
            #Limpiar lista de segmentos (body)
            body.clear()


    #Colisiones comida
    if head.distance(food)<20:
        #Cambiamos posicion de la comida
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        food.goto(x,y)

        #Crece la serpiente
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        body.append(new_body) #add body

        #Mover cuerpo de la serpiente
        body_length=len(body)
        for cord in range(body_length -1, 0, -1):
            x=body[cord - 1].xcor()
            y=body[cord - 1].ycor()
            body[cord].goto(x,y)

        if body_length > 0:
            x=head.xcor()
            y=head.ycor()
            body[0].goto(x,y)

    mov()
    time.sleep(SLOW)
