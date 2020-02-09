# Based on tutorial from freeCodeCamp.org : https://www.youtube.com/watch?v=C6jJg9Zan7w
# Sounds downloaded from freesound.org

# import turtle module
import turtle

# intreracts with MacOS and Linux
import os
# for Windows: import winsound  

# create a drawing canvas
canvas = turtle.Screen()
canvas.title("Classic Pong")
canvas.bgcolor("black")
canvas.setup(width=800, height=600)
canvas.tracer(0)

# Score
score_a = 0
score_b = 0

# Gamer A
gamer_a = turtle.Turtle()
# animation speed, not the game speed 
gamer_a.speed(0)
gamer_a.shape("square")
gamer_a.color("white")
gamer_a.shapesize(stretch_wid=5, stretch_len=1)
gamer_a.penup()
gamer_a.goto(-350, 0)

# Gamer B
gamer_b = turtle.Turtle()
gamer_b.speed(0)
gamer_b.shape("square")
gamer_b.color("white")
gamer_b.shapesize(stretch_wid=5, stretch_len=1)
gamer_b.penup()
gamer_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Score table, Pen turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
#penup is not to drawn a line from center to upper canvas
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gamer A: 0  Gamer B: 0", align="center", font=("Courier", 24, "normal"))

# Ball moviment into coordinate X in pixels
# adequate speed to your computer processor
ball.changex = 1.5 
ball.changey = -1.5

# Ball moviment into coordinate Y in pixels

# Function
def gamer_a_up():
    y = gamer_a.ycor()
    y += 20
    gamer_a.sety(y)

def gamer_a_down():
    y = gamer_a.ycor()
    y -= 20
    gamer_a.sety(y)

def gamer_b_up():
    y = gamer_b.ycor()
    y += 20
    gamer_b.sety(y)

def gamer_b_down():
    y = gamer_b.ycor()
    y -= 20
    gamer_b.sety(y)

# Keyboard binding
canvas.listen()
canvas.onkeypress(gamer_a_up, "q")
canvas.onkeypress(gamer_a_down, "z")
canvas.onkeypress(gamer_b_up, "Up")
canvas.onkeypress(gamer_b_down, "Down")

# Main game loop
while True:
    # Every time the loop runs, it updates the screen
    canvas.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.changex)
    ball.sety(ball.ycor() + ball.changey)

    # Border checking on Y coordinate
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.changey *= -1
        os.system("afplay pong_a.wav&")
        # for Windows: windsound.PlaySound("music.wav", winsound.SND_ASYNC)
        # for Linux: os.system("aplay music.wav&")
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.changey *= -1
        os.system("afplay pong_b.wav&")
        # for Windows: windsound.PlaySound("music.wav", winsound.SND_ASYNC)
        # for Linux: os.system("aplay music.wav&")
    
    # Border checking on X coordinate
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.changex *= -1
        score_a += 1
        pen.clear()
        pen.write("Gamer A: {}  Gamer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay scored_pong.wav&")
        # for Windows: windsound.PlaySound("music.wav", winsound.SND_ASYNC)
        # for Linux: os.system("aplay music.wav&")
    
    if ball.xcor() < - 390:
        ball.goto(0, 0)
        ball.changex *= -1
        score_b += 1
        pen.clear()
        pen.write("Gamer A: {}  Gamer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay scored_pong.wav&")
        # for Windows: windsound.PlaySound("music.wav", winsound.SND_ASYNC)
        # for Linux: os.system("aplay music.wav&")
    
    # Gamer and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < gamer_b.ycor() + 40 and ball.ycor() > gamer_b.ycor() -40):
        ball.setx(340)
        ball.changex *= -1
        os.system("afplay pong_a.wav&")
        # for Windows: windsound.PlaySound("music.wav", winsound.SND_ASYNC)
        # for Linux: os.system("aplay music.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < gamer_a.ycor() + 40 and ball.ycor() > gamer_a.ycor() -40):
        ball.setx(-340)
        ball.changex *= -1
        os.system("afplay pong_b.wav&")
        # for Windows: windsound.PlaySound("music.wav", winsound.SND_ASYNC)
        # for Linux: os.system("aplay music.wav&")