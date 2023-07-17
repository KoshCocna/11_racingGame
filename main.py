import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
tim = []
yy = -100

for color in colors:
    timmy = Turtle(shape="turtle")
    timmy.color(color)
    timmy.penup()
    timmy.goto(x=-230, y=yy)
    tim.append(timmy)
    yy += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in tim:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
