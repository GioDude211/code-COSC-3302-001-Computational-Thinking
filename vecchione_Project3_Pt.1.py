"""
Programmer: Giovanni Vecchione
Date: 11/13/23
Subject: Project 3 Pt. 1
Description:
Part 1 -- Numerical Differentiation:

a. Let f(x) = 4x^3 + 2x^2 - 3x + 5.
Approximate the derivative (also known as the slope of the tangent line and the instantaneous rate of change) of f(x) at x = a
Use the following technique:
1. choose a value for your acceptable error, aka your tolerance.
2. choose an initial value for h (which represents the difference between x values) - DONE
3. calculate [f(a+ h) - f(a)]/h for decreasing values of h
4. continue systematically decreasing h until the value of the differences of calculated quantites between steps is lower than your acceptable error.
Do the above algorithm twice -- once for x = 1 and a second time for x = -3 (that is let a = 1 and then let a = -3 in the above calculations to find the derivative of f(x) at two different points).

Report your answers, your initial value of h, the method used to modify h, the value of h when you halted, and the error you used. (answers for derivative of f(x) at x = 1 and x = -3 respectivelly are 13 and 93).

b. Repeat the above for this function -- f(x) = x^2 *cos(x) at x = 0 and x = PI
"""
"""
FUNCTION FOR SECTION A is Below
"""
def derivative_of_function(func, x_value, h=.000001):
    """
    Calculate the derivative of a given function at a given point using the limit definition of derivative.
    
    Args:
    func (function): The function to differentiate.
    x_value (float): The point at which to evaluate the derivative.
    h (float): A small number to approximate the limit. Default is 0.0001.
    
    Returns:
    float: The approximate derivative of the function at the given points
    """
    return (func(x_value + h) - func(x_value)) / h #derivative formula returns

def function(x):
    return ((4*x**3) + (2*x**2) - (3*x) + 5) #input formula

# Calculate the derivative at a specific point, for example x = 1
point = 1
derivative_at_point = derivative_of_function(function, point) #calls function to find derivative, given function and point

print("The approximate derivative for section A at x =", point, "is:", derivative_at_point)

"""
SECTION A REPORT:

Inital Start up:
Inital value of h = .0001 
Starting here since this is a common point to begin inital value.
Will drop or raise to what is neccessary, which with every test I will drop
the h value by a decimal point (ex. .0001, .00001, etc.)

Tolerance seleted = .000001
Also did some research, this seems to be the common error amount for software. However this of course 
has many exceptions to what is considered acceptable error. I went with a saying "six nines" which is 
an acceptable correct range of 99.9999% which is an error acceptable range of .000001.


Testing:
Tolerance = .000001
Actual answer for x = 1 : 13.00000
Actual answer for x = -3 : 93.00000

Test 1:
h = .0001
The approximate derivative at x = 1 is: 13.001400039982514 
error: .00011
Error NOT within acceptable tolerance.

The approximate derivative at x = -3 is: 92.99660004032262
error: .000037
Error NOT within acceptable tolerance.

Test 2:
h = .00001
The approximate derivative at x = 1 is: 13.00014000040761
error: .000011
Error NOT within acceptable tolerance.

The approximate derivative at x = -3 is: 92.99966000071434
error: .0000037
Error NOT within acceptable tolerance.

Test 3:
h = .000001
The approximate derivative at x = 1 is: 13.000014000397186
error: .0000011
Error IS within acceptable tolerance.

The approximate derivative at x = -3 is: 92.99996602862848
error: .00000036
Error IS within acceptable tolerance.

FINAL NOTE:
Test 3 is the point in which I stopped the program. h = .000001 seems to be the appropriate differernce between x values.


error was calculated using the formula: (approx. value - actual value) / actual value
Sidenote: I used decimal form but if you wanted percentage mulitply the error by 100.


"""

"""
SECTION B FUNCTION is BELOW:
COPY OF FUNCTION 1 for SectionB, specifically changed variables to have 2 next to it (ex. x2 instead of x)
importing math to facilitate the cos function
"""
import math

def derivative_of_function2(func2, x_value2, h2=.0000001):
    """
    Calculate the derivative of a given function at a given point using the limit definition of derivative.
    
    Args:
    func2 (function): The function to differentiate.
    x_value2 (float): The point at which to evaluate the derivative.
    h2 (float): A small number to approximate the limit. Default is 0.0001.
    
    Returns:
    float: The approximate derivative of the function at the given points
    """
    return (func2(x_value2 + h2) - func2(x_value2)) / h2

def function2(x2):
    return ((x2**2) * (math.cos(x2)))

# Calculate the derivative at a specific point, for example x = 1
point2 = 0
derivative_at_point2 = derivative_of_function2(function2, point2)

print("The approximate derivative for section B at x =", point2, "is:", derivative_at_point2)



"""
SECTION B REPORT:

Inital Start up:
x = 0 
actual output : 0

x = 3.141592653589793 
actual output : -6.28319 

3.141592653589793 is the pi value used by the imported math library for pi

Inital value of h = .000001
Stated at .000001 due to the previous testing showed good results at this point.

Tolerance seleted = .000001

TEST 1:
Inital value of h = .000001
The approximate derivative for section B at x = 0 is: 9.999999999995e-07
error: .000001
Error IS within acceptable tolerance.

The approximate derivative for section B at x = 3.141592653589793 is: -6.283181372523927
error: .0000014
Error NOT within acceptable tolerance. (just barely)

TEST 2:
Inital value of h = .0000001
The approximate derivative for section B at x = 0 is: 9.999999999999948e-08
error: .0000001
Error IS within acceptable tolerance.

The approximate derivative for section B at x = 3.141592653589793 is: -6.283184905697681
error: .00000081
Error IS within acceptable tolerance.

FINAL NOTE:
Test 2 is the point in which I stopped the program. h = .0000001 seems to be the appropriate differernce between x values.
Took some double checking on the error calculations to ensure I needed to run a second test.

error was calculated using the formula: (approx. value - actual value) / actual value
Sidenote: I used decimal form but if you wanted percentage mulitply the error by 100.



"""