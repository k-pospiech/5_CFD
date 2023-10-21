import sympy as sp

# Define the symbolic variables
x_prime, y_prime, q_prime = sp.symbols('x_prime y_prime q_prime')

# Define the dimensionless velocities u' and v'
u_prime = 1 + q_prime/2 * (
    (x_prime + 1) / ((x_prime + 1)**2 + y_prime**2) - 
    (x_prime - 1) / ((x_prime - 1)**2 + y_prime**2)
)
    
v_prime = q_prime * y_prime / 2 * (
    1 / ((x_prime + 1)**2 + y_prime**2) - 
    1 / ((x_prime - 1)**2 + y_prime**2)
)

# Set up the equations for the stagnation points
eq1 = sp.Eq(u_prime, 0)
eq2 = sp.Eq(v_prime, 0)

# Solve the equations
stagnation_points = sp.solve((eq1, eq2), (x_prime, y_prime))

print(stagnation_points)
