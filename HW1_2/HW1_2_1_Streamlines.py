import sympy as sp

# Define the symbolic variables
x_prime, y_prime, q_prime = sp.symbols('x_prime y_prime q_prime')

# Dimensionless velocities as previously derived
u_prime_expr = 1 + q_prime/2 * (
    (x_prime + 1) / ((x_prime + 1)**2 + y_prime**2) - 
    (x_prime - 1) / ((x_prime - 1)**2 + y_prime**2)
)
    
v_prime_expr = q_prime * y_prime / 2 * (
    1 / ((x_prime + 1)**2 + y_prime**2) - 
    1 / ((x_prime - 1)**2 + y_prime**2)
)

# Forward Euler update with termination condition
def euler_step(x, y, dt, q_val, epsilon=1e-10):
    u_val = sp.N(u_prime_expr.subs({x_prime: x, y_prime: y, q_prime: q_val}))
    v_val = sp.N(v_prime_expr.subs({x_prime: x, y_prime: y, q_prime: q_val}))
    
    if abs(u_val) < epsilon and abs(v_val) < epsilon:
        return x, y
    
    x_new = x + dt * u_val
    y_new = y + dt * v_val
    return x_new, y_new

# Parameters
dt = 4.0E-4
q_val = 1.0
x_current, y_current = -2, -10**-6
n_steps = 1000

x_values = [x_current]
y_values = [y_current]
V_prime_values = []
Cp_values = []

for step in range(n_steps): 
    current_x = x_values[-1]
    current_y = y_values[-1]
    
    u_prime_val = u_prime_expr.subs({x_prime: current_x, y_prime: current_y, q_prime: q_val})
    v_prime_val = v_prime_expr.subs({x_prime: current_x, y_prime: current_y, q_prime: q_val})
    
    V_prime = sp.N(sp.sqrt(u_prime_val**2 + v_prime_val**2))
    V_prime_values.append(V_prime)
    
    # Compute pressure coefficient
    Cp = 1 - V_prime**2
    Cp_values.append(Cp)
    
    next_x, next_y = euler_step(current_x, current_y, dt, q_val)
    
    if next_x == current_x and next_y == current_y:
        print(f"Terminated at step {step} due to stagnation.")
        break
    
    x_values.append(next_x)
    y_values.append(next_y)

# Print results
print("Completed integration.")
for x, y, v, cp in zip(x_values, y_values, V_prime_values, Cp_values):
    print(f"Path: ({x:.6f}, {y:.6f}), V': {v:.6f}, Cp: {cp:.6f}")
