import numpy as np
import matplotlib.pyplot as plt

def cylinder_potential_flow(U_inf, a, r, theta):
    """Calculate the potential and stream functions for flow around a cylinder."""
    phi = U_inf * r * np.cos(theta) * (1 + (a**2 / r**2))
    psi = U_inf * r * np.sin(theta) * (1 - (a**2 / r**2))
    return phi, psi

# Parameters
U_inf = 1.0    # Free-stream velocity
a = 1.0        # Radius of the cylinder
r = np.linspace(a, 5*a, 100)  # Radial distance from cylinder
theta = np.linspace(0, 2*np.pi, 100)  # Angle in radians

R, Theta = np.meshgrid(r, theta)
Phi, Psi = cylinder_potential_flow(U_inf, a, R, Theta)

# Convert to Cartesian coordinates for plotting
X, Y = R * np.cos(Theta), R * np.sin(Theta)

# Plotting
plt.figure(figsize=(10, 6))
plt.contour(X, Y, Phi, colors='red', levels=20)  # Potential lines
plt.contour(X, Y, Psi, colors='blue', levels=20)  # Streamlines
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Potential Flow around a Cylinder')
plt.grid(True)
plt.show()
