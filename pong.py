#simple pong in python 3 for beginners

#part 1: getting started


import turtle #lets you do basic graphics, great for games for beginners (pyGame is also an option)

#create windows
wn = turtle.Screen()
wn.title("Pong by Allen Loyola")
wn.bgcolor("black")
wn.setup(width=800, height = 600)
wn.tracer(0) #stops window from updating, lets us speed up game faster

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle() #class name
paddle_a.speed(0) # speed of animation, sets it to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle() #class name
paddle_b.speed(0) # speed of animation, sets it to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle() #class name
ball.speed(0) # speed of animation, sets it to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15  #d means delta
ball.dy = 0.15  #this means that every time the ball moves(ie window updates), the ball moves 2 pixels in x or y


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions
# functions for moving paddle A
def paddle_a_up():
    y = paddle_a.ycor() #.ycor() is from the turtle module, returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #.ycor() is from the turtle module, returns the y coordinate
    y -= 20
    paddle_a.sety(y)

# functions for moving paddle B
def paddle_b_up():
    y = paddle_b.ycor() #.ycor() is from the turtle module, returns the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #.ycor() is from the turtle module, returns the y coordinate
    y -= 20
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#every game needs a main game loop:
#Main game loop
while True:
    wn.update() #this means every time the loop runs, the windows updates

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border
        #the goal here is to compare the ball's coordinate to the window size
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #this reverses the ball direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #this reverses the ball direction

    #Remember this tells us that the ball has gone past the paddle, ie the game should reset
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    #comparing position of ball with the paddles

    #paddle b coordinates vs ball coor
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    #paddle a coor vs ball coor
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1