import random
import turtle as t

t.colormode(255)
leonardo = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


leonardo.speed("fastest")


def draw_circle(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        leonardo.color(random_color())
        leonardo.circle(100)
        current_heading = leonardo.heading()
        leonardo.setheading(current_heading+size_of_graph)


draw_circle(5)

my_screen = t.Screen()
my_screen.exitonclick()
