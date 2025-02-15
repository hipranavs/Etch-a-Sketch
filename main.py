from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.back(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def pen_up():
    tim.penup()
def pen_down():
    tim.pendown()
def clear_drawing():
    tim.home()
    tim.clear()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="u", fun=pen_up)
screen.onkey(key="z", fun=pen_down)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
