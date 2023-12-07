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

sys.setrecursionlimit(15000)  # Extends the recursion limit implaced by default

#Variables for the dice w/o reroll scenario function
prob_value_NR = 0           #holds probability value
match_count_NR = 0          #if there is a match this tracks the count
total_cases_NR = 10000      #Number of runs (cases)

#Function for  Dice w/o reroll scenario
def prob_dice_NO_reroll(n , prob_value, count, total_cases):

    #calculates the probability once recursion is done
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
        #Random numbers are the dice, set to 1-6 randomly
        random_number_1 = random.randint(1,6)
        random_number_2 = random.randint(1,6)
        random_number_3 = random.randint(1,6)
        random_number_4 = random.randint(1,6)
        random_number_5 = random.randint(1,6)
        random_number_6 = random.randint(1,6)

        #if they all match it counts it
        if random_number_1 == random_number_2 == random_number_3 == random_number_4 == random_number_5 == random_number_6:
            print("Values Match")
            count += 1

        return n * prob_dice_NO_reroll(n - 1, prob_value, count, total_cases) #recursive call


#Calls dice w/o reroll function
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

Test 3: 
Depth: 1001
total_cases: 1000
matches: 3

probability: .0003

Test 3.1:
Test 3: 
Depth: 1001
total_cases: 1000
matches: 1

probability: .0001

note: Test 3 was raised to 1000 cases. There seems to be an increase in probability when there are larger cases.

Test 4: 
Depth: 100001
total_cases: 100000
matches: 10

probability: .0001

note: Test 4 was raised to 100,000 cases. Probability seems to stabilize around the .0001 mark.

Test 5: 
Depth: 1000001
total_cases: 1000000
matches: 106

probability: .000115

note: Test 5 was raised to 1,000,000 cases. Probability seems to stabilize around the .0001 mark even at 1,000,000 cases.

"""
#Variables for the dice w/ reroll scenario function
prob_value_R = 0        #probability value
match_count_R = 0       #tracks when dice match
total_cases_R = 10000  #number of runs (cases)

#Function for  Dice w/ reroll scenario
def prob_dice_reroll(n , prob_value, count, total_cases):

    #calculates the probability once recursion is done
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
        #variables simulates dice
        random_number_1 = random.randint(1,6)
        random_number_2 = random.randint(1,6)
        random_number_3 = random.randint(1,6)
        random_number_4 = random.randint(1,6)
        random_number_5 = random.randint(1,6)
        random_number_6 = random.randint(1,6)

        #checks if reroll is needed (false means it hasnt rerolled yet)
        unique_value_found = False

        #Basic format: 
        # 1. Checks if a reroll has occured, if not continues
        # 2. If the number does not match then it rerolls
        # 3. Otherwise it moves on and marks true if reroll occurs

        if unique_value_found != True:
            if all(x != random_number_1 for x in [random_number_2, random_number_3, random_number_4, random_number_5, random_number_6]):

                random_number_1 = random.randint(1,6)

                unique_value_found = True

        if unique_value_found != True:
            if all(x != random_number_2 for x in [random_number_1, random_number_3, random_number_4, random_number_5, random_number_6]):

                random_number_2 = random.randint(1,6)

                unique_value_found = True

        if unique_value_found != True:
            if all(x != random_number_3 for x in [random_number_1, random_number_2, random_number_4, random_number_5, random_number_6]):                
                random_number_3 = random.randint(1,6)

                unique_value_found = True

        if unique_value_found != True:
            if all(x != random_number_4 for x in [random_number_1, random_number_2, random_number_3, random_number_5, random_number_6]):
                random_number_4 = random.randint(1,6)

                unique_value_found = True

        if unique_value_found != True:
            if all(x != random_number_5 for x in [random_number_1, random_number_2, random_number_3, random_number_4, random_number_6]):
                random_number_5 = random.randint(1,6)

                unique_value_found = True

        if unique_value_found != True:
            if all(x != random_number_6 for x in [random_number_1, random_number_2, random_number_3, random_number_4, random_number_5]):
                random_number_6 = random.randint(1,6)

                unique_value_found = True
        #checks if all values match
        if random_number_1 == random_number_2 == random_number_3 == random_number_4 == random_number_5 == random_number_6:
            print("Values Match")
            count += 1

        return n * prob_dice_reroll(n - 1, prob_value, count, total_cases) #recursive call



print ("Probability of dice W/ Reroll: ")
prob_dice_reroll(10001, prob_value_R, match_count_R, total_cases_R)



"""
TEST 1: 
Depth: 101
total_cases: 100
matches: 1

probability: .01

TEST 2:
Depth: 1001
total_cases: 1000
matches: 2

probability: .002

TEST 3:
Depth: 10001
total_cases: 10000
matches: 8

probability: .0008

TEST 3.1:
Depth: 10001
total_cases: 10000
matches: 11

probability: .0011

TEST 4:
Depth: 100001
total_cases: 100000
matches: 82

probability: .00082

note: probability does improve with a reroll. 

"""

def prob_three_doors(switch_doors, num_trials=100000):
    wins = 0

    for _ in range(num_trials):
    # Randomly place the prize and have the contestant choose a door
        prize_door = random.randint(1, 3)
        contestant_choice = random.randint(1, 3)

        # Host opens a door that is not the prize door and not the contestant's choice
        available_doors = [door for door in [1, 2, 3] if door != contestant_choice and door != prize_door]
        door_opened = random.choice(available_doors)

        # If the contestant switches, change their choice to the remaining door
        if switch_doors:
            remaining_doors = [door for door in [1, 2, 3] if door != contestant_choice and door != door_opened]
            contestant_choice = remaining_doors[0]

        # Check if the contestant's final choice is the prize door
        if contestant_choice == prize_door:
            wins += 1

    return wins / num_trials


# Simulate both scenarios
switching_wins = prob_three_doors(True)
staying_wins = prob_three_doors(False)

print(f"Winning probability when always switching: {switching_wins}")
print(f"Winning probability when never switching: {staying_wins}")





"""
Test 1:
Count: 1000
Winning probability when always switching: 0.673
Winning probability when never switching: 0.325

Test 2:
Count: 10000
Winning probability when always switching: 0.6648
Winning probability when never switching: 0.3338

Test 3:
Count: 100000
Winning probability when always switching: 0.6658
Winning probability when never switching: 0.33447

Note: It seems even in trials, switching has a higher probability. Therefore the contestant should usually 
switch doors when placed in this scenario.

"""

# Python code to sort a list of numbers in ascending order using a basic for loop (Bubble Sort)

def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Example list of numbers
numbers = [4, 3, 2, 1]

# Sort the list using Bubble Sort
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

