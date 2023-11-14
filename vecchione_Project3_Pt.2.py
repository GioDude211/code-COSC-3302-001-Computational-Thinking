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

def f(x):
    return ((0.34 * x**2) + (2.98 * x) + 1.53)

#determine if the total area is close to accurate
def approximate_area(a, b, n):
    width = (b-a) / n           #calculates width
    total_area = 0              #init. variable to hold total area

    for i in range(n):          #iterates over given sub-intervals
        height = f(a + i * width)
        total_area += height * width
    
    return total_area           #returns calculated area

#ask professor if this function is allowed, this ensures the error is below the tol
def find_area_with_tolerance(a, b, initial_n, tol):
    n = initial_n
    previous_area = approximate_area(a, b, n)
    while True:
        n *= 2
        current_area = approximate_area(a, b, n)
        if abs(current_area - previous_area) < tol:
            break
        previous_area = current_area

    return current_area, n

a, b = 2, 4
initial_n = 10  # initial number of sub-intervals
tol = 0.001  # tolerance

area, final_n = find_area_with_tolerance(a, b, initial_n, tol)
print(f"Approximate area: {area}, Number of sub-intervals: {final_n}")