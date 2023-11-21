import numpy as np
import matplotlib.pyplot as plt

def bl_boundary_layer(U_inf, nu, x, y):
    """Calculate boundary layer thickness and velocity profile based on the Blasius solution."""
    Re_x = U_inf * x / nu
    delta = 5.0 * x / np.sqrt(Re_x)  # Boundary layer thickness

    # Velocity profile within the boundary layer (simple linear approximation)
    u = U_inf * np.minimum(y / delta, 1)
    return u

# Parameters
U_inf = 1.0       # Free-stream velocity
nu = 1.5e-5       # Kinematic viscosity
plate_length = 2  # Length of the flat plate

# Grid setup
x = np.linspace(0, plate_length, 100)
y = np.linspace(0, 0.1, 40)  # Extent of boundary layer visualization
X, Y = np.meshgrid(x, y)

# Velocity in the boundary layer
U = bl_boundary_layer(U_inf, nu, X, Y)

# Plotting
plt.figure(figsize=(10, 5))
plt.streamplot(X, Y, U, np.zeros_like(U), density=1.5)
plt.xlim(0, plate_length)
plt.ylim(0, max(y))
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Flow over a Flat Plate with Boundary Layer Visualization')
plt.grid(True)
plt.show()
