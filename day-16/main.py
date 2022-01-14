# from turtle import Turtle, Screen
#
# tammy = Turtle()
# tammy.shape("turtle")
# tammy.color("red")
# tammy.forward(300)
# tammy.back(600)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
