"""
ROSHAMBO PROGRAM
----------------
Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record
"""
import random
win = 0
lose = 0
tied = 0
games = 0
quit = False
while not quit == True:
    number = random.randint(1, 3)
    roshambo = int(input("put 1 for rock, 2 for paper, 3 for scissors or 4 for quit"))
    if number == 1:
        play = "rock"
    elif number == 2:
        play = "paper"
    elif number == 3:
        play = "scissors"
    if roshambo == number:
        print("you tied")
        print("the computer chose", play)
        tied += 1
    elif number == 1 and roshambo == 2:
        print("The computer chose rock")
        print("you win")
        win += 1
        games += 1
    elif number == 2 and roshambo == 3:
        print("The computer chose paper")
        print("you win")
        win += 1
        games += 1
    elif number == 3 and roshambo == 1:
        print("you win")
        print("The computer chose scissors")
        win += 1
        games += 1
    elif roshambo == 1 and number == 2:
        print("you lose")
        print("The computer chose rock")
    elif roshambo == 2 and number == 3:
        print("You Lose")
        print("The computer chose paper")
    elif roshambo == 3 and number == 1:
        print("you lose")
        print("the computer chose scissors")
    elif roshambo == 4:
        quit = True
    else:
        print("That is not a number you can choose try again")


print("you won", win, "times")
print("you lost", lose, "times")
print("you tied", tied, "times")
print("you played", games, "times")