"""
Programmer: Giovanni Vecchione
Date: 11/28/23
Subject: Exam 2
Description: 

1.Write code to calculate the probability of getting the same number on the rolling of 5
standard six-sided dice.

2.Write code to calculate the probability of getting the same number on the rolling of 5 standard six-sided dice 
if you get to re-roll any of the dice you choose a second time.

3.Write code to simulate the following scenario. There are three doors. A grand prize is placed behind one of the doors. 
A contestant chooses a door. A different door is opened revealing that the grand prize is not behind that door.
The contestant is allowed to change their choice if they desire. What should they do and why? 
Explore the scenario where they ALWAYS choose to switch doors and the scenario where they NEVER choose to switch doors. 
Determine what their optimal strategy should be to win as often as possible. 
"""
import math
import random

import sys

sys.setrecursionlimit(15000)  # Be cautious with this

prob_value_NR = 0
match_count_NR = 0
total_cases_NR = 10000

def prob_dice_NO_reroll(n , prob_value, count, total_cases):

    if n == 1: 

        print("Count: ")
        print(count)

        print("total_cases: ")
        print (total_cases)

        prob_value = count / total_cases

        print("prob_value: ")
        print(prob_value)

        return 1

    else:
        random_number_1 = random.randint(1,6)
        random_number_2 = random.randint(1,6)
        random_number_3 = random.randint(1,6)
        random_number_4 = random.randint(1,6)
        random_number_5 = random.randint(1,6)
        random_number_6 = random.randint(1,6)

        if random_number_1 == random_number_2 == random_number_3 == random_number_4 == random_number_5 == random_number_6:
            print("Values Match")
            count += 1
        
            print(count)

        return n * prob_dice_NO_reroll(n - 1, prob_value, count, total_cases) #recursive call



print ("Probability of dice W/O Reroll: ")
prob_dice_NO_reroll(10001, prob_value_NR, match_count_NR, total_cases_NR)

"""
Test 1:
depth: 11
total_cases: 10
matches: 1

probability: .1

note: most cases this will result in a 0 probability
however went with the one with an actual match.

Test 2: 
Depth: 101
total_cases: 100
matches: 1

probability: .01


"""



#print (f"Probability of dice W Reroll: {prob_dice_Reroll()}")
#print (f"Probability of 3 Doors scenerio: {prob_three_doors()}")