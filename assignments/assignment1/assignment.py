import turtle

screen = turtle.Screen()
screen.title("Drawing a square")
screen.bgcolor('red')

sq_turtle = turtle.Turtle()
sq_turtle.color("blue")
sq_turtle.pensize(3)
sq_turtle.speed(3)

for _ in range(4):
    sq_turtle.forward(100)
    sq_turtle.right(90)

screen.exitonclick()
        
