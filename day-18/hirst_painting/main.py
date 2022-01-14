import turtle as turtle_module
import random

turtle_module.colormode(255)
tam = turtle_module.Turtle()
number_of_dots = 100

colors_list = [(246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61),
               (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
               (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
               (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
               (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
               (65, 66, 56)]

tam.setheading(230)
tam.penup()
tam.hideturtle()
tam.forward(300)
tam.setheading(0)
tam.speed("fastest")


for dots_count in range(1, number_of_dots+1):
    tam.dot(15, random.choice(colors_list))
    tam.forward(50)

    if dots_count % 10 == 0:
        tam.setheading(90)
        tam.forward(50)
        tam.setheading(180)
        tam.forward(500)
        tam.setheading(0)

my_screen = turtle_module.Screen()
my_screen.exitonclick()


