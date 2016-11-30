import turtle

def draw_rhombus(some_turtle):
    for i in range(2):
        some_turtle.fd(100)    
        some_turtle.left(45)
        some_turtle.fd(100)
        some_turtle.left(135)
        
def draw_flower():
    window=turtle.Screen()
    window.bgcolor("black")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(15)
    draw_rhombus(brad)
    
    for i in range(36):
        draw_rhombus(brad)
        brad.right(10)

    line=turtle.Turtle()
    line.shape("arrow")
    line.color("white")
    line.right(90)
    line.fd(300)
    window.exitonclick()
    
draw_flower()
