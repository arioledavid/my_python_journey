#!/usr/bin/python3
import os
import random
def user_num():
    print("Pick a number between 1 - 100, I will try to guess it")
    print("Indicate if number is higher or lower by 'h' or 'l' and 'c' if the number is correct")
    
    rannum = random.randint(1, 100)
    choice = ''
    low = 1
    high =100
    lives = 7
    input("Press Enter to Start")

    while choice != 'c' and lives != 0:
        lives -= 1
        print(f"is {rannum} your number", end=',')
        print(f"( {lives} tries left)")
        choice = str(input().lower())
        if choice == 'h':
            high = rannum - 1
            rannum = random.randint(low, high)
        elif choice == 'l':
            low = rannum + 1
            rannum = random.randint(low, high)
    print("Yay I got the answer correctly")
user_num()
