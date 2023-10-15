import numpy as np
import matplotlib.pyplot as plt

# Given initial conditions
r0_values = [8]
theta0_values = [np.pi - 0.01, np.pi + 0.01, np.pi + 0.05, np.pi - 0.05, np.pi + 0.1, np.pi - 0.1]

# Set up the plot
plt.figure(figsize=(10, 6))

# Integration settings
delta_xi = 0.01
xi_values = np.arange(0, 10, delta_xi)

for r0 in r0_values:
    for theta0 in theta0_values:
        r_values = [r0]
        theta_values = [theta0]
        for xi in xi_values[1:]:
            # Euler forward method
            dr_dxi = (1 - 1 / r_values[-1]**2) * np.cos(theta_values[-1])
            dtheta_dxi = -(1 + 1 / r_values[-1]**2) * np.sin(theta_values[-1])
            
            r_new = r_values[-1] + delta_xi * dr_dxi
            theta_new = theta_values[-1] + delta_xi * dtheta_dxi
            
            r_values.append(r_new)
            theta_values.append(theta_new)
            
        x_values = [r * np.cos(theta) for r, theta in zip(r_values, theta_values)]
        y_values = [r * np.sin(theta) for r, theta in zip(r_values, theta_values)]
        
        plt.plot(x_values, y_values)

plt.xlabel("x'")
plt.ylabel("y'")
plt.title("Numerically Integrated Streamlines")
plt.grid(True)
plt.axis("equal")
plt.show()
