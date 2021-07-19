
import turtle
import random
wn=turtle.Screen()  #creating a turtle window screen
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6,stretch_len=1)  #mutiplies default width by 5 and length by 1
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6,stretch_len=1)  #mutiplies default width by 5 and length by 1
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx=0.7
ball.dy=-0.7

#Score pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=("Arial",25,"normal"))

#score
scorea,scoreb=0,0


#function
#moving paddle

def paddle_a_up():
    y=paddle_a.ycor()   #returns y coordinate and assigns to y
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()   #returns y coordinate and assigns to y
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"o")
wn.onkeypress(paddle_b_down,"k")

#main game loop
while 1:
    wn.update()

    #moving ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(random.randint(-50,50),random.randint(-50,50))
        ball.dx *= -1
        scorea+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(scorea,scoreb), align="center", font=("Arial", 25, "normal"))

    if ball.xcor() < -390:
        ball.goto(random.randint(-50,50),random.randint(-50,50))
        ball.dx *= -1
        scoreb+=1
        pen.clear()  #avoiding overwriting
        pen.write("Player A:{}  Player B:{}".format(scorea, scoreb), align="center", font=("Arial", 25, "normal"))

    #paddle and ball collision
    if ball.xcor()<-340 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50:
        ball.dx*=-1
    elif ball.xcor()>340 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50:
        ball.dx*=-1






