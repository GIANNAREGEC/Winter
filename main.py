import turtle

turtle.Turtle()
screen= turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("CornflowerBlue")


t=turtle.Turtle()
t.speed(0)

t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor('snow1')
t_ground.fillcolor('snow1')
t_ground.speed(0)


t_ground.begin_fill()
t_ground.goto(-1000, -100)
t_ground.pendown()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000, -100)
t_ground.end_fill()

#snowman
t_ground.penup()
t_ground. goto(0,-10)
t_ground.hideturtle()
t_ground.pencolor('black')
t_ground.fillcolor('snow1')
t_ground.pendown()
t_ground.begin_fill()
t_ground.circle(50)
t_ground.end_fill()


t_ground.penup()
t_ground. goto(0,80)
t_ground.showturtle()
t_ground.pencolor('black')
t_ground.fillcolor('snow1')
t_ground.pendown()
t_ground.begin_fill()
t_ground.circle(30)
t_ground.end_fill()

t_ground.penup()
t_ground. goto(0,-140)
t_ground.pencolor('black')
t_ground.fillcolor('snow1')
t_ground.pendown()
t_ground.begin_fill()
t_ground.circle(70)
t_ground.end_fill()
t_ground.pendown()

t_ground.penup()
t_ground.goto (50,400)
t_ground.circle(20)
t_ground.pendown()


t_ground.penup()
t_ground.goto(30, 400)
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.circle(4)
t_ground.end_fill
t_ground.pendown()

t_ground.penup()
t_ground.goto(60, 400)
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.circle(4)
t_ground.end_fill
t_ground.pendown()

t_ground.penup()
t_ground.goto(70, 400)
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.circle(4)
t_ground.end_fill
t_ground.pendown()

t_ground.pendown()
t_ground.goto(40, 400)
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.dot()
t_ground.end_fill()
t_ground.pendown()

t_ground.pendown()
t_ground.goto(60,400)
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.dot()
t_ground.end_fill()
t_ground.pendown()



#text
t_ground.pencolor('black')
t_ground.penup()
t_ground.goto(0,300)
t_ground.pendown()
t_ground.write("Happy Holidays", font=("arial", 30 , "bold"),align="center")
t_ground.penup()


t_ground.penup()
t_ground.goto(100, -150)
t_ground.pendown()
t_ground.pencolor('saddlebrown')

# t_ground.penup()
t_ground.pensize(10)

t_ground.pensize(4)
t_ground.forward(90)
t_ground.circle(20,100)

t_ground.pendown()
t_ground.pensize(1)

t.penup()
t.pensize(15)
t.pencolor('brown')
t.goto(-200,-150)
t.pendown()
t.goto(-200,-200)

t.pensize(1)
t.penup()
t.fillcolor('green')
t.pencolor('green')
t.goto(-250,-175)
t.pendown()
t.begin_fill()
t.goto(-200,100)
t.goto(-150,-175)
t.goto(-250,-175)
t.end_fill()

t.penup()
t.goto(-180,250)
t.fillcolor('yellow')
t.begin_fill()
t.circle(30)
t.end_fill()

candy = turtle.Turtle()

candy.pensize(5)
candy.hideturtle()
candy.color("red")
candy.penup()
candy.goto(80, -100)
candy.pendown()
candy.setheading(90)
candy.forward(50)
candy.right(90)
candy.forward(10)
candy.right(90)
candy.forward(10)
candy.penup()
candy.goto(0, -100)
candy.pendown()
candy.end_fill()

#present
t.penup()
t.goto(150,-300)
t.fillcolor('purple')
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.pendown()

t.penup()
t.setheading(270)
t.pendown()
t.forward(100)
t.pendown()

#snowflake

#this is the last line of code DO NOT change
turtle.done()