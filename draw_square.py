import turtle

"""def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angle=turtle.Turtle()
    angle.shape("arrow")
    angle.color("yellow")
    angle.circle(100)
   
    windoe.exitonclick()

draw_square()"""

"""def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    draw_square(brad)

    angle=turtle.Turtle()
    angle.shape("arrow")
    angle.color("yellow")
    angle.circle(100)
   
    windoe.exitonclick()

    

draw_art()"""

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

    

draw_art()
