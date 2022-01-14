import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.listen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(10)


def move_right():
    tim.left(10)


def move_left():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_right, 'd')
screen.onkey(move_left, 'a')
screen.onkey(clear,'c')

screen.exitonclick()
