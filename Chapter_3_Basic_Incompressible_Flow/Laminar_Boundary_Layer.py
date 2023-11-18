import numpy as np
import matplotlib.pyplot as plt

def calculate_boundary_layer_properties(U_inf, nu, x):
    """
    Calculate boundary layer thickness and skin friction coefficient based on Blasius solution.

    Parameters:
    U_inf (float): Free-stream velocity (m/s)
    nu (float): Kinematic viscosity of the fluid (m^2/s)
    x (float or array): Distance from the leading edge of the plate (m)

    Returns:
    delta (float or array): Boundary layer thickness (m)
    cf (float or array): Skin friction coefficient
    """
    Re_x = U_inf * x / nu
    delta = 5.0 * x / np.sqrt(Re_x)
    cf = 0.664 / np.sqrt(Re_x)
    return delta, cf

# Example usage
U_inf = 2.0    # Free-stream velocity in m/s
nu = 1.5e-5    # Kinematic viscosity in m^2/s
x_values = np.linspace(0.01, 2.0, 100)  # Distance from leading edge in m

# Calculate boundary layer properties
delta_values, cf_values = calculate_boundary_layer_properties(U_inf, nu, x_values)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, delta_values)
plt.xlabel('Distance from leading edge, x (m)')
plt.ylabel('Boundary layer thickness, δ (m)')
plt.title('Boundary Layer Thickness along a Flat Plate')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_values, cf_values)
plt.xlabel('Distance from leading edge, x (m)')
plt.ylabel('Skin friction coefficient, Cf')
plt.title('Skin Friction Coefficient along a Flat Plate')
plt.grid(True)

plt.tight_layout()
plt.show()
