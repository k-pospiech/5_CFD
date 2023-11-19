import numpy as np
import matplotlib.pyplot as plt

def momentum_thickness(x, U_inf, nu):
    """
    Calculate the momentum thickness for laminar boundary layer on a flat plate.

    Parameters:
    x (array): Distance from the leading edge of the plate (m)
    U_inf (float): Free-stream velocity (m/s)
    nu (float): Kinematic viscosity of the fluid (m^2/s)

    Returns:
    theta (array): Momentum thickness (m)
    """
    Re_x = U_inf * x / nu
    # Using Blasius solution for laminar flow
    theta = 0.664 * np.sqrt(nu * x / U_inf) * np.sqrt(nu / (U_inf * x))
    return theta

# Example usage
U_inf = 2.0    # Free-stream velocity in m/s
nu = 1.5e-5    # Kinematic viscosity in m^2/s
x_values = np.linspace(0.01, 1.0, 100)  # Distance from leading edge in m

# Calculate momentum thickness
theta_values = momentum_thickness(x_values, U_inf, nu)

# Plotting
plt.plot(x_values, theta_values)
plt.xlabel('Distance from leading edge, x (m)')
plt.ylabel('Momentum thickness, θ (m)')
plt.title('Momentum Thickness along a Flat Plate')
plt.grid(True)
plt.show()
