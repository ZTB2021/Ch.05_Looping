#Sign your name:Zachary Blum
import random
'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    num = int(input("Enter a number: "))
    total += num
print("The total is:", total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2, 101, 2):
    print(i)
print("Done")

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
count=10
while count>=0:
    print(count)
    count-=1
print("Blast off")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

num = random.randint(1, 11)
print("the integer is", num)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
totals = 0
pos = 0
neg = 0
zero = 0
for i in range(7):
    number = float(input("What is your number"))
    totals += number

    if number >0:
        print("positive")
        pos+=1

    if number <0:
        print("negative")
        neg+=1
    else:
        print("it is zero")
        zero+=1

print("the total sum is", total)
