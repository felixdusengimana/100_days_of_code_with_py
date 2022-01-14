# import random
# import turtle as t
#
# t.colormode(255)
# leonardo = t.Turtle()
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand_color = (r, g, b)
#     return rand_color
#
#
# directions = [0, 90, 180, 270]
# leonardo.pensize(15)
# leonardo.speed("fastest")
# for _ in range(200):
#     leonardo.color(random_color())
#     leonardo.forward(30)
#     leonardo.setheading(random.choice(directions))
#
# my_screen = t.Screen()
# my_screen.exitonclick()
