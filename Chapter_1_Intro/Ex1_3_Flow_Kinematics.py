import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# # Given parameters
# U_inf = 1  # Freestream velocity [unit]
# L = 1  # Some length scale [unit]

# Define symbolic variables
x, y, U_inf, L = sp.symbols('x y U_inf L')

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
# x_prime, y_prime = x/L, y/L
# U_prime, V_prime = U/U_c, V/V_c

# Define symbolic variables
x_prime, y_prime = sp.symbols('x_prime y_prime')
U_prime = (1 + x_prime/(x_prime**2 + y_prime**2))
V_prime = (y_prime/(x_prime**2 + y_prime**2))

# Find stagnation points in dimensionless coordinates
stagnation_points_prime = sp.solve([U_prime, V_prime], (x_prime, y_prime))
print(f"Dimensionless Stagnation Points: {stagnation_points_prime}")

# Define the streamline ODE
def streamline_ODE(t, z):
    x_val, y_val = z
    U_val = float(U_prime.subs({x_prime: x_val, y_prime: y_val}))
    V_val = float(V_prime.subs({x_prime: x_val, y_prime: y_val}))
    return [U_val, V_val]

# Initial condition very close to stagnation point
z0 = [-0.999, 0.5]
t_eval = np.linspace(0, 5, 1000)

# Solve the ODE
sol = solve_ivp(streamline_ODE, [0, 5], z0, t_eval=t_eval)

# Plotting the streamline
plt.figure(figsize=(10,10))
plt.plot(sol.y[0], sol.y[1], 'b', label='Streamline')
plt.scatter([-1], [0], color='red', s=100, label='Stagnation Point (-1,0)')
plt.xlabel('x_prime')
plt.ylabel('y_prime')
plt.title('Dimensionless Streamline Radiating from Stagnation Point')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()