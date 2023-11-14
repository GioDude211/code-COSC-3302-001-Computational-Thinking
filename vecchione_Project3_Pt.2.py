"""
Programmer: Giovanni Vecchione
Date: 11/13/23
Subject: Project 3 Pt. 2

Description: Numerical Integration
1. Find the area below the curve of f(x) = .34x^2 + 2.98x + 1.53 from x = 2 to x = 4 
and above the x axis. Use the method of rectangles as described in class.

2. Choose a tolerance, tol,  and an initial number of sub-intervals, n. 

3. Calculate the approximate area. 

Repeat the calculation with a greater n and continue the process until successive 
approximations have a difference less than tol. 

Report all choices and results.
"""
#function 1 that will pass the formula needed (f(x) = .34x^2 + 2.98x + 1.53)
#returns the formula
def f(x):
    return ((0.34 * x**2) + (2.98 * x) + 1.53)

#function 2 to determine the total area
#returns the total_area
def approximate_area(a, b, n):
    width = (b-a) / n                   #calculates width
    total_area = 0                      #init. variable to hold total area

    for i in range(n):                  #iterates over given sub-intervals
        height = f(a + i * width)       #calculates height
        total_area += height * width    #calculates total area
    
    return total_area                   #returns total area

#function 3 checks if total_area is within tolerance, otherwise it will iterate the while loop until its within acceptable range of error.
#in basic terms its the refinement process, it will further divide into rectangles until the total_area is within tolerance.
#returns the current_area and number of sub-intervals required
def find_area_with_tolerance(a, b, initial_n, tol):
    n = initial_n
    previous_area = approximate_area(a, b, n)       #saves an iteration of calculating the area to a variable
                                                    #this will determine if another iteration of the while loop is needed

    #this loop determines if the absolute value of the difference between the current_area and previous_area is within appropriate tolerance
    while True: 
        n *= 2                                      #This is used to double the number of sub-intervals in each iteration of the while loop
        current_area = approximate_area(a, b, n)   
        if abs(current_area - previous_area) < tol: #checks area with tolerance
            break
        previous_area = current_area

    return current_area, n

a, b = 2, 4     #set start and end of range
initial_n = 10  # initial number of sub-intervals
tol = 0.00001     # tolerance

area, final_n = find_area_with_tolerance(a, b, initial_n, tol)
print(f"Approximate area: {area}, Number of sub-intervals: {final_n}")


"""
REPORT:

NOTE: Need to confirm if I created the tolerance check function correctly, from what I can tell it auto determines the required amount
of sub-intervals needed by comparing the values of the previous total area iterations. Otherwise I accidently created a function that 
auto checks that without needing to adjust n values.

So the area is around the right figure, doing some basic math on my end I was able to determine that a rough estimate of the area within 
the range [2,4] for the formula was '27.74'. Of course this value is way off tolerance however the point was to showcase a rough figure to look at.
So after comparing the program's approximations and the value I found, it seems to be correct.

How I determined a rough estimate by hand:
Step 1: Determine a partial of the area based off a right triangle
(2, 8.85)
(4, 18.89)
Based off these coordinates within the formula provided we can find the area of a triangle for the top of the area(area_of_triangle = ab/2)
which equates to 10.04

Step 2: Determine the rest of the area through use of a broad rectangle below the triangle we calculated.
width of rectangle = 2
height of rectangle = 8.85
(use the first coordinate)
area of rectangle (remaining area) = 17.7

Step 3: Add the partial areas all together to find total area.
17.7 + 10.04 = 27.74
(VERY ROUGH HAND ESTIMATE)

NOTE: Program Tests show the number of sub-intervals that was required to stay within tolerance and outputs the approx. total area of the sub-intervals.
In this case the approx. area is increasing towards the actual value for every refinement of the sub-intervals (n).

TEST 1: 
Set tolerance to .001
Approximate area: 27.285686202239845, Number of sub-intervals: 10240

TEST 2:
Set tolerance to .0001
Approximate area: 27.286605387387652, Number of sub-intervals: 163840

TEST 3:
Set tolerance to .00001
Approximate area: 27.28665900675092, Number of sub-intervals: 1310720

"""