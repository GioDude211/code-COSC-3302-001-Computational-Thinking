def derivative_of_function(func, x_value, h=0.0001):
    """
    Calculate the derivative of a given function at a given point using the limit definition of derivative.
    
    Args:
    func (function): The function to differentiate.
    x_value (float): The point at which to evaluate the derivative.
    h (float): A small number to approximate the limit. Default is 0.0001.
    
    Returns:
    float: The approximate derivative of the function at the given point.
    """
    return (func(x_value + h) - func(x_value)) / h

def function(x):
    return ( (x * x) + (2 * x) + 1)

# Calculate the derivative at a specific point, for example x = 1
point = 2
derivative_at_point = derivative_of_function(function, point)

print("The approximate derivative at x =", point, "is:", derivative_at_point)


