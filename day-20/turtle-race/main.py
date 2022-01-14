import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race. Enter color: ")
colors = ['red', 'orange', 'green', 'yellow', 'blue', 'purple', 'black']
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0, 7):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor();
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The winning turtle is {winning_color}")
            else:
                print(f"You've lost! The winning turtle is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
