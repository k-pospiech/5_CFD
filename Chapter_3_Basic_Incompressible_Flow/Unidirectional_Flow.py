import sympy as sp

# Define symbolic variables
P1, P2 = sp.symbols('P1 P2')  # Pressure at point 1 and 2
rho = sp.symbols('rho')  # Density of the fluid
A1, A2 = sp.symbols('A1 A2')  # Cross-sectional areas at point 1 and 2
V1, V2 = sp.symbols('V1 V2')  # Flow velocities at point 1 and 2
z1, z2 = sp.symbols('z1 z2')  # Heights at point 1 and 2

# Continuity equation for incompressible flow
continuity_eq = sp.Eq(A1 * V1, A2 * V2)

# Bernoulli's equation
bernoulli_eq = sp.Eq(P1/(rho*9.81) + (V1**2)/(2*9.81) + z1, P2/(rho*9.81) + (V2**2)/(2*9.81) + z2)

# Function to solve the Bernoulli and continuity equations
def solve_flow(P1_val, P2_val, rho_val, A1_val, A2_val, z1_val, z2_val, V1_val=None, V2_val=None):
    # Create a dictionary of known values
    known_values = {P1: P1_val, P2: P2_val, rho: rho_val, A1: A1_val, A2: A2_val, z1: z1_val, z2: z2_val}
    # If one of the velocities is unknown, solve for it using continuity
    if V1_val is None:
        sol = sp.solve(continuity_eq.subs(known_values), V1)
        known_values[V1] = sol[0]
    elif V2_val is None:
        sol = sp.solve(continuity_eq.subs(known_values), V2)
        known_values[V2] = sol[0]
    # Now solve Bernoulli's equation with the known values
    solutions = sp.solve(bernoulli_eq.subs(known_values), (P1, P2, V1, V2))
    return solutions

# Example usage
# Assume some values are known, like pressures, areas, and one of the velocities
P1_val = 101325  # Pa
P2_val = 95000  # Pa
rho_val = 1000  # kg/m^3 (approximate density of water)
A1_val = 0.05  # m^2
A2_val = 0.02  # m^2
z1_val = 10  # m
z2_val = 12  # m

# Call the function with the known values and print the result
results = solve_flow(P1_val, P2_val, rho_val, A1_val, A2_val, z1_val, z2_val, V1_val=5)
print(results)
