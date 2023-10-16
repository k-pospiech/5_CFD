import numpy as np

# Parameters
U0 = 1.0  # This can be any chosen reference velocity, since we're working with dimensionless variables
a = 1.0  # Similarly, this can be any chosen reference length
q_values = [1.0, 0.1, 0.01, 0.001]  # Given q' values

# Dimensionless velocity field
def velocity_field(x, y, q_prime):
    u_prime = 1 + q_prime * ((x + 1)/((x + 1)**2 + y**2) - (x - 1)/((x - 1)**2 + y**2))
    v_prime = q_prime * (y/((x + 1)**2 + y**2) - y/((x - 1)**2 + y**2))
    return u_prime, v_prime

# Forward Euler method to integrate streamline equations
def integrate_streamline(x0, y0, q_prime, dt_prime=4E-4, steps=10000):
    x, y = x0, y0
    xs, ys = [x], [y]
    for _ in range(steps):
        u, v = velocity_field(x, y, q_prime)
        x += dt_prime * u
        y += dt_prime * v
        xs.append(x)
        ys.append(y)
    return xs, ys

# Anchor points
anchor_points = [(-2, 1E-6), (-2, -1E-6), (-2.025, 0.75), (-2, -0.75), (-2.1, 0), (-2, -1)]

streamlines = {}
for q_prime in q_values:
    for point in anchor_points:
        x_vals, y_vals = integrate_streamline(point[0], point[1], q_prime)
        streamlines[(q_prime, point)] = (x_vals, y_vals)

print("Streamlines computed for all anchor points and q' values.")
