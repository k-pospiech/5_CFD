import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Given parameters
U_inf = 1  # Freestream velocity [unit]
L = 1  # Some length scale [unit]

# Define symbolic variables
x, y = sp.symbols('x y')

# Define the velocity field in Cartesian coordinates
U = U_inf * (1 + L*x/(x**2 + y**2))
V = U_inf * (L*y/(x**2 + y**2))

# Find stagnation points by setting U and V to zero and solving
stagnation_points = sp.solve([U, V], (x, y))
print(f"Stagnation Points: {stagnation_points}")

# Define characteristic length and velocity
L_c = L  # Example, this might depend on problem insight [unit]
U_c = U_inf  # Example, this might depend on problem insight [unit]

# Define dimensionless variables
x_bar, y_bar = x/L_c, y/L_c
U_bar = U/U_c
V_bar = V/U_c

# ODE for streamline in dimensionless coordinates
def streamline_ODE(t, Y):
    # Extract coordinates from the current position Y
    x, y = Y

    # Calculate dimensionless velocities U' and V'
    U_prime = U_bar.subs({x_bar: x, y_bar: y}).evalf()
    V_prime = V_bar.subs({x_bar: x, y_bar: y}).evalf()

    # Return the dimensionless velocities
    return [U_prime, V_prime]


def plot_dimensionless_streamlines(x0_values, y0_values, t_max=10):
    plt.figure(figsize=(8, 8))
    
    for x0, y0 in zip(x0_values, y0_values):
        sol = solve_ivp(streamline_ODE, [0, t_max], [x0, y0], t_eval=np.linspace(0, t_max, 1000))
        plt.plot(sol.y[0], sol.y[1], label=f'Initial Point: ({x0}, {y0})')

    # Adding radial lines near origin
    theta = np.linspace(0, 2*np.pi, 100)
    for r in [0.1, 0.2, 0.3, 0.4]:
        plt.plot(r * np.cos(theta), r * np.sin(theta), 'k--')
    
    plt.xlabel('x\'')
    plt.ylabel('y\'')
    plt.title('Dimensionless Streamlines')
    plt.legend()
    plt.grid(True)
    plt.axis

# Example initial points
x0_values = [-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2]
y0_values = [0, 0, 0, 0, 0, 0, 0, 0]

# Plotting the streamlines
plot_dimensionless_streamlines(x0_values, y0_values)

# Display the figure
plt.show()
