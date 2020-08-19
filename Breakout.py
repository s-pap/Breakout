#Breakout

#Setup
import turtle
import time
import random
import decimal
wn = turtle.Screen()
wn.title("Breakout by Sarah")
turtle.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score = 0
lives = 3
    
#startpen
start_pen=turtle.Turtle()
start_pen.speed(0)
start_pen.color("red")
start_pen.penup()
start_pen.setpos(0, 50)
start_pen.write("BREAKOUT", False, align= "center", font=("Courier", 100, "normal"))
start_pen.hideturtle()
time.sleep(3)
start_pen.clear()

 
#Paddle
paddle=turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=7)
paddle.penup()
paddle.goto (0,-250)


#ball
ball = turtle.Turtle()
ball.dx=5
ball.dy=5
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,-250)



#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setpos(-350, 270)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align= "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Draw the lives

lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("white")
lives_pen.penup()
lives_pen.setpos(350, 270)
livesstring = "Lives: {}".format(lives)
lives_pen.write(livesstring, False, align= "right", font=("Arial", 14, "normal"))
lives_pen.hideturtle()




#add color
colors=["red", "yellow", "green", "blue"]

brick_start_x = -300
brick_start_y = 250
brick_number = 0

#choose number of bricks
number_of_bricks = 24
#create an empty list of bricks
bricks=[]

#Add bricks to the list
for i in range (number_of_bricks):
    #create the brick
    bricks.append(turtle.Turtle())

for brick in bricks:
    brick.speed(0)
    brick.shape("square")
    color=colors[0]
    brick.color(color)
    brick.shapesize(stretch_wid=1, stretch_len=5)
    brick.penup()
    x = brick_start_x +(120*brick_number)
    y = brick_start_y
    brick.setpos(x,y)
                    
    brick_number += 1
    if brick_number ==6:
        colors = [colors[(i + 1) % len(colors)] 
            for i, z in enumerate(colors)]
        brick_start_y -=50
        brick_number = 0


#Function
def paddle_left():
    x=paddle.xcor()
    x-=20
    paddle.setx(x)
def paddle_right():
    x=paddle.xcor()
    x+=20
    paddle.setx(x)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

   


#Main game loop
while True :
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    #paddle limits
    if paddle.xcor()>360:
        x=paddle.xcor()
        x=370
        paddle.setx(x)
    if paddle.xcor()<-360:
        x=paddle.xcor()
        x=-370
        paddle.setx(x)
            

    #Border checking
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-360:
        time.sleep(1)
        ball.goto(0,-150)
        ball.dy *= -1
        lives_pen.clear()
        lives -= 1
        livesstring = "Lives: {}".format(lives)
        lives_pen.write(livesstring, False, align= "right", font=("Arial", 14, "normal"))

            #paddle and ball colisions
    if(ball.ycor()>-255 and ball.ycor()<-240) and (ball.xcor()<paddle.xcor() +100 and ball.xcor() > paddle.xcor() -100):
        ball.sety(-240)
        rand_dy=float(decimal.Decimal(random.randrange(90, 110))/-100)
                
                
        ball.dy *= rand_dy

    #brick and ball collision
    for brick in bricks:
        if brick.distance(ball)<50:
            ball.dy *= -1
            brick.goto(1000,1000)
            score_pen.clear()
            score+=10
            scorestring = "Score: {}".format(score)
            score_pen.write(scorestring, False, align= "left", font=("Arial", 14, "normal"))
    #end the game
    for brick in bricks:
        if lives == 0 or score ==240:   
            brick.goto(1000,1000)
            
    if lives == 0 or score ==240:
        ball.goto(1000,1000)
        paddle.goto(1000,1000)
        time.sleep(1)
        lives_pen.clear()
        score_pen.clear()
        end_pen=turtle.Turtle()
        end_pen.speed(0)
        end_pen.color("red")
        end_pen.penup()
        score_pen.setpos(0, 100)
        end_pen.write("GAME OVER", False, align= "center", font=("Courier", 60, "normal"))
        end_pen.hideturtle()
        scorestring = "Final Score: {}".format(score)
        score_pen.goto(0,-100)
        score_pen.write(scorestring, False, align= "center", font=("Courier", 40, "normal"))
                        

        
    

        

           
