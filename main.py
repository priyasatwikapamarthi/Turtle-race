from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

colours = ["red","purple","blue","orange","yellow","green"]

ypos = [-150,-90,-30,30,90,150]

all_turtles = []

for key in range(0,6) :
    tim = Turtle(shape="turtle")
    tim.color(colours[key])
    tim.penup()
    tim.goto(x = -230,y = ypos[key])
    all_turtles.append(tim)

user_guess = screen.textinput(title='Guess a colour',prompt='Bet on a colour you chose to win')

if user_guess :
    game = True

while game :
    for turtle in all_turtles :
        if turtle.xcor()>230 :
            game = False
            winner = turtle.pencolor()
            if winner == user_guess :
                print(f"You've won.The winner is {winner}")
            else :
                print(f"You've lost.The winner is {winner}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
