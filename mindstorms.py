import turtle
    
def draw_shapes():
    window= turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(4)
    
    for i in range(4):
            brad.forward(100)
            brad.right(90)

    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.speed(4)
    angie.circle(100)

    colon=turtle.Turtle()
    colon.shape("turtle")
    colon.color("blue")
    colon.speed(4)
    colon.right(180)
    colon.forward(100)
    colon.left(120)
    colon.forward(100)
    colon.left(120)
    colon.forward(100)
    window.exitonclick()
    
draw_shapes()



