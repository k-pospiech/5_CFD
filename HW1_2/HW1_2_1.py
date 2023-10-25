import sympy as sp
import matplotlib.pyplot as plt

# User Parameters (Input Section)
q_val = 1.0  # Dimensionless source strength
dt = 4.0E-4  # Time step
x_start, y_start = -2, -10**-6  # Initial point
n_steps = 26000  # Number of integration steps
x_stop = 2  # Stopping value for x

# Define the symbolic variables
x_prime, y_prime, q_prime = sp.symbols('x_prime y_prime q_prime')

# Dimensionless velocities as derived
u_prime_expr = 1 + q_prime/2 * (
    (x_prime + 1) / ((x_prime + 1)**2 + y_prime**2) - 
    (x_prime - 1) / ((x_prime - 1)**2 + y_prime**2)
)
    
v_prime_expr = q_prime * y_prime / 2 * (
    1 / ((x_prime + 1)**2 + y_prime**2) - 
    1 / ((x_prime - 1)**2 + y_prime**2)
)

# Forward Euler update for streamline calculation
def euler_step(x, y, dt, q_val):
    u_val = float(u_prime_expr.subs({x_prime: x, y_prime: y, q_prime: q_val}))
    v_val = float(v_prime_expr.subs({x_prime: x, y_prime: y, q_prime: q_val}))
    x_new = x + dt * u_val
    y_new = y + dt * v_val
    return x_new, y_new

# Integrate for streamline points
path = [(x_start, y_start)]
V_prime_values = []
Cp_values = []

for i in range(n_steps):
    x_current, y_current = path[-1]
    
    # Compute velocities and modulus
    u_prime_val = u_prime_expr.subs({x_prime: x_current, y_prime: y_current, q_prime: q_val})
    v_prime_val = v_prime_expr.subs({x_prime: x_current, y_prime: y_current, q_prime: q_val})
    V_prime = sp.sqrt(u_prime_val**2 + v_prime_val**2)
    
    # Compute pressure coefficient
    Cp = 1 - V_prime**2
    V_prime_values.append(float(V_prime))
    Cp_values.append(float(Cp))
    
    if x_current >= x_stop:
        break
    
    # Compute next coordinates using Euler's method
    next_x, next_y = euler_step(x_current, y_current, dt, q_val)
    path.append((next_x, next_y))

# Print the results
for i, (x, y) in enumerate(path):
    if i < len(V_prime_values):
        print(f"Step {i+1}: Coordinate (x', y') = ({x:.5f}, {y:.5f}), Velocity Modulus V' = {V_prime_values[i]:.5f}, Pressure Coefficient Cp = {Cp_values[i]:.5f}")

# Plotting the streamline
x_values = [point[0] for point in path]
y_values = [point[1] for point in path]

plt.plot(x_values, y_values, '-b')
plt.xlabel("x'")
plt.ylabel("y'")
plt.title("Streamline Plot")
plt.grid(True)
plt.show()

# Plotting Cp vs x'
x_values = [coord[0] for coord in path]
plt.figure(figsize=(10, 5))
plt.plot(x_values, Cp_values, label='Pressure Coefficient, $C_p$', color='blue')
plt.title('$C_p$ vs $x\'$')
plt.xlabel("$x'$")
plt.ylabel("$C_p$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plotting V_prime vs x'
plt.figure(figsize=(10, 5))
plt.plot(x_values, V_prime_values, label='Velocity Modulus, $V\'$', color='red')
plt.title("$V'$ vs $x'$")
plt.xlabel("$x'$")
plt.ylabel("$V'$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()