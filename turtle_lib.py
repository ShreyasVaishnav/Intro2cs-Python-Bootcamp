import turtle
rectangle_ = turtle.Turtle()

def rectangle():
    rectangle_.forward(100)
    rectangle_.right(90)
    rectangle_.forward(100)
    rectangle_.right(90)
    rectangle_.forward(100)
    rectangle_.right(90)
    rectangle_.forward(100)

rectangle()

turtle.circle(10)
turtle.circle(40)

turtle.penup()
turtle.forward(100)
turtle.pendown()

turtle.circle(10)
turtle.circle(40)

turtle.penup()
turtle.backward(30)
turtle.goto(20, -40)
turtle.pendown()

turtle.circle(10)

turtle.penup()
turtle.backward(30)
turtle.goto(80, -40)
turtle.pendown()

turtle.circle(10)

turtle.penup()
turtle.goto(45, -55)
turtle.pendown()

def triangle(edge=10):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.left(300)

triangle()

turtle.penup()
turtle.goto(45, -82)
turtle.pendown()

turtle.circle(10,180)

turtle.Screen().exitonclick()
