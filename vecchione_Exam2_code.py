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

def prob_dice_NO_reroll():

    prob_value_NR = 0

    prob_value_NR = ((1 / 6) ** 5) * 6

    return prob_value_NR

def prob_dice_Reroll():
    prob_value_R = 0
    prob_value_R = (((1 / 6) ** 4) * (1/3)) * 6

    return prob_value_R

def prob_three_doors():
    prob_value_3doors = 0
    
    prob_value_3doors = ((1/3) + ((1/3) * (1/2)))
    """
    Im pretty sure that the prob_value_3doors needs to be .67
    still debuggin this
    """

    return prob_value_3doors


print (f"Probability of dice W/O Reroll: {prob_dice_NO_reroll()}")
print (f"Probability of dice W Reroll: {prob_dice_Reroll()}")
print (f"Probability of 3 Doors scenerio: {prob_three_doors()}")