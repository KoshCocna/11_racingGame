import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
stake = 5000
want_to_go_on = True
counter = 0
while want_to_go_on:
    is_race_on = False
    try:
        user_bet_info = screen.textinput(title="Make your bet",
                                         prompt=f"Which turtle will win the race? Enter a color and "
                                                f"your betting stake: \n"
                                                f"Pls remember your stake is {stake}$")
        user_bet_color, user_bet_stake = user_bet_info.split(",")
        if int(user_bet_stake) > stake:
            print(f"Not enough money, Your money is {stake}")
            continue
    except:
        if user_bet_info == 'q':
            want_to_go_on = False
            print(f"Your stake is {stake} now.")
            screen.clear()
            continue
        else:
            print("Pls enter a color and stake correctly!")
            counter += 1
            if counter > 2:
                print("We consider you don't want to play anymore. Goodbye!")
                want_to_go_on = False
                screen.clear()

            continue

    screen.clear()

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

    if user_bet_color:
        is_race_on = True

    while is_race_on:
        for turtle in tim:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet_color:
                    stake += int(user_bet_stake)
                    print(f"You've won! The {winning_color} turtle is the winner! Your money is now {stake}")
                else:
                    stake -= int(user_bet_stake)
                    print(f"You've lost! The {winning_color} turtle is the winner! Your money is now {stake}")
                    if stake <= 0:
                        want_to_go_on = False
                        print("Sorry, You lost all of your money. If you want to play, pls make a deposit")
                        screen.clear()

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
