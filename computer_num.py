#!/usr/bin/python3 
import random

def randomunm():
    rannum = random.randint(1, 101)
    user = 0
    user = int(input("Guess my number between 1 - 100 \n"))
    while user is not rannum:
        if user < rannum:
            print(f"Your number is less than mine")
        elif user > rannum:
            print(f"Your number is greater than mine")
        user = int(input("Guess again \n"))
ans = 'y'
while ans == 'y':
    randomunm();
    print("Your guess was correct")
    ans = input("Would you like to play again y/n")
