import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''
Done = False
canteen = 3
tiredness = 0
day = 7
thirst = 0
native = 20
Total = 200
miles_traveled = 0
print("\033[1;32;34m \n")
print("You start with 3 drinks from your canteen, your goal is to go 200 or more miles to win.")
print("When tiredness is 8 or higher you die, if the natives catch up to you you die and if you get 6 thirst or more you die")
print("you can type either the letter or the number position")
while not Done:
    print("\033[1;32;34m \n")
    print("A. Drink from your canteen. ")
    print("B. Ahead moderate speed. ")
    print("C. Ahead full speed. ")
    print("D. Stop for the night. ")
    print("E. Status check. ")
    print("or Q. Quit.")
    natives = 0
    user_input = input("- ")
    miles = 0
    oasis = random.randint(1, 20)
    natives -= random.randint(7, 12)
    miles_traveled = 0
    if (user_input.lower() == "a" or user_input) == "1" and canteen > 0:
        print("you drank from the canteen and it lessens your thirst")
        canteen -= 1
        thirst = 0

    elif (user_input.lower() == "a" or user_input.lower() == "drink form the canteen" or user_input == "1") and thirst <= 0:
        print("you now have more water then necessary")
        thirst = 0
    elif (user_input.lower() == "a" or user_input == "1") and thirst == 0:
        print("you are full on water")
    elif (user_input.lower() == "a" or user_input.lower() == "drink form the canteen" or user_input == "1") and canteen == 0:
        print("There is no water in the canteen")

    if user_input.lower() == "b" or user_input.lower() == "ahead at moderate speed" or user_input == "2":
        miles_traveled = random.randint(5, 12)
        Total -= miles_traveled
        native = natives + miles_traveled
        print("You moved", miles_traveled,  "miles")
        print("the natives moved", natives, "miles")
        print("The natives are", native, "miles behind you")
        print("you have", Total, "miles left")
        tiredness += 1
        thirst += 2
        day += 1

    if user_input.lower() == "c" or user_input.lower() == "full speed ahead" or user_input == "3":
        miles_traveled = random.randint(10, 20)
        native = natives + miles_traveled
        Total -= miles_traveled
        print("you have moved", miles_traveled, "miles")
        print("the natives moved", natives, "miles")
        print("The natives are", native, "miles behind you")
        print("you have", Total, "miles left")
        day += 1
        tiredness += 2
    if user_input.lower() == "d" or user_input.lower() == "Stop for the Night" or user_input == "4":
        tiredness = 0
        print("You have slept for the night")
        print("you are not tired")
        print("The natives are", native, "behind you")
        day += 1

    if tiredness >= 5:
        print("your camel is getting tired")
    if not Done and tiredness >= 8:
        print("your camel has died by tiredness")
        print("you had", miles_traveled, "miles left")
        Done = True

    if natives >= -15:
        print("The natives are getting closer")

    elif user_input.lower() == "e" or user_input == "Status Check" or user_input == "5":
        print("you have", tiredness, "tiredness")
        print("you have", canteen, "water in your canteen")
        print("you have", Total, "total miles left")
        print("The natives are", natives, "behind you")
        print("You have lived for", day, "days")

    if user_input.lower() == "q" or user_input.lower() == "quit" or user_input == "6":
        print("you had", miles_traveled, "miles left")
        Done = True

    if not Done and Total <= 0:
        print("You win the game")
        Done = True

    if not Done and native <= 0:
        print("The natives have caught you")
        Done = True

    if not Done and thirst >= 6:
        print("You have died of thirst")
        Done = True

    if not Done and thirst >= 4:
        print("You are thirsty")

    if not Done and oasis == 15:
        print("you found an oasis ")
        canteen = 3
        thirst = 0
        tiredness = 0

    else:
        print(" ")











