import numpy as np
import matplotlib.pyplot as plt

def u(x, y, q_prime):
    return 1 + q_prime * (y / (x**2 + y**2))

def v(x, y, q_prime):
    return -q_prime * (x / (x**2 + y**2))

def generate_streamline(x0, y0, q_prime, delta_t, t_range):
    x_vals, y_vals = [x0], [y0]

    for t in t_range:
        dx_dt = u(x_vals[-1], y_vals[-1], q_prime)
        dy_dt = v(x_vals[-1], y_vals[-1], q_prime)

        new_x = x_vals[-1] + dx_dt * delta_t
        new_y = y_vals[-1] + dy_dt * delta_t

        x_vals.append(new_x)
        y_vals.append(new_y)

    return x_vals, y_vals

# Parameters
q_primes = [1.0, 0.1, 0.01, 0.001]
anchor_points = [(-2, 10**-6), (-2, -10**-6), (-2, 0.25), (-2.1, 0), (-2, 0.5), (-2, -0.5)]
delta_t = 4e-4
t_values = np.linspace(-2, 2, int(4/delta_t))

plt.figure(figsize=(10, 6))

for q_prime in q_primes:
    for point in anchor_points:
        x_vals, y_vals = generate_streamline(point[0], point[1], q_prime, delta_t, t_values)
        plt.plot(x_vals, y_vals, label=f"Start: {point}, q': {q_prime}")

plt.title('Streamlines for Different q\' values and Starting Points')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

def velocity_modulus(x, y, q_prime):
    u_val = u(x, y, q_prime)
    v_val = v(x, y, q_prime)
    return np.sqrt(u_val**2 + v_val**2)

def pressure_coefficient(x, y, q_prime):
    rho = 1  # Assuming a unit density for the fluid
    P_inf = 0  # Far field pressure
    U_inf = 1  # Free stream velocity

    V_prime = velocity_modulus(x, y, q_prime)
    P = P_inf + 0.5 * rho * U_inf**2 - 0.5 * rho * V_prime**2
    Cp = 2 * (P - P_inf) / (rho * U_inf**2)

    return Cp

# Velocity Modulus
plt.figure(figsize=(10, 6))
for q_prime in q_primes:
    for point in anchor_points:
        x_vals, y_vals = generate_streamline(point[0], point[1], q_prime, delta_t, t_values)
        V_prime_vals = [velocity_modulus(x, y, q_prime) for x, y in zip(x_vals, y_vals)]
        plt.plot(x_vals, V_prime_vals, label=f"Start: {point}, q': {q_prime}")

plt.title('Velocity Modulus for Different q\' values and Starting Points')
plt.xlabel('x')
plt.ylabel('Velocity Modulus')
plt.grid(True)
plt.legend()
plt.show()

# Pressure Coefficient
plt.figure(figsize=(10, 6))
for q_prime in q_primes:
    for point in anchor_points:
        x_vals, y_vals = generate_streamline(point[0], point[1], q_prime, delta_t, t_values)
        Cp_vals = [pressure_coefficient(x, y, q_prime) for x, y in zip(x_vals, y_vals)]
        plt.plot(x_vals, Cp_vals, label=f"Start: {point}, q': {q_prime}")

plt.title('Pressure Coefficient for Different q\' values and Starting Points')
plt.xlabel('x')
plt.ylabel('Cp')
plt.grid(True)
plt.legend()
plt.show()