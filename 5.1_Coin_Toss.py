import random
'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
heads = 0
tails = 0
for i in range(50):
    coin_side = random.randint(0, 1)
    if coin_side == 0:
        print("You got heads")
        heads += 1
    else:
        print("you got tails")
        tails += 1
print("you got", tails, "amount of tails")
print("you got", heads, "amount of heads")







