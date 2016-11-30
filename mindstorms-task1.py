import turtle


def draw_square(some_turtle):
        for i in range(4):
            some_turtle.forward(100)
            some_turtle.right(90)
def draw_shapes():
    window= turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    
    for i in range(36):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()
    
draw_shapes()



