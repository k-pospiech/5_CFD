import sympy as sp

def find_stagnation_points(U_inf, R):
    """
    Find the stagnation points of a 2D Eulerian velocity field in polar coordinates.
    
    The function calculates the stagnation points of a given velocity field defined as:
    U_r = U_inf * (1 - r^2/R^2) * cos(theta)
    U_theta = -U_inf * (1 + R^2/r^2) * sin(theta)
    
    Parameters:
    - U_inf: A symbolic expression or float, representing the characteristic velocity.
    - R: A symbolic expression or float, representing the characteristic length.
    
    Returns:
    - stagnation_points: A list of tuples representing the stagnation points in the format (r, theta).
    
    Example Usage:
    >>> U_inf, R = sp.symbols('U_inf R')
    >>> find_stagnation_points(U_inf, R)
    """
    
    # Define symbols
    r, theta = sp.symbols('r theta')
    
    # Define velocity components
    U_r = U_inf * (1 - r**2/R**2)*sp.cos(theta)
    U_theta = -U_inf * (1 + R**2/r**2)*sp.sin(theta)
    
    # Set them equal to zero and solve for r and theta
    stagnation_points = sp.solve([U_r, U_theta], (r, theta))
    
    return stagnation_points


# # Example usage:
# U_inf, R = sp.symbols('U_inf R')  # You can replace these with actual values if needed
# stagnation = find_stagnation_points(U_inf, R)

# print(stagnation)