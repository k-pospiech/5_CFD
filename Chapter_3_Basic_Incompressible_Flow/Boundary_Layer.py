import numpy as np
from scipy.integrate import quad

# Define the fluid and flow conditions
U_inf = 10  # Free-stream velocity in m/s
nu = 1.5e-5  # Kinematic viscosity of the fluid in m^2/s
x = 0.5  # Distance from the leading edge of the plate in meters

# Calculate Reynolds number at distance x
Re_x = U_inf * x / nu

# Boundary layer thickness (delta)
delta = 5.0 * x / np.sqrt(Re_x)

# Function for the integrand of displacement thickness
def displacement_thickness_integrand(eta):
    return 2.0 * eta * np.exp(-eta**2)

# Displacement thickness (delta_star)
delta_star, _ = quad(displacement_thickness_integrand, 0, 10)
delta_star *= x / np.sqrt(Re_x)

# Function for the integrand of momentum thickness
def momentum_thickness_integrand(eta):
    return eta * (1 - np.exp(-eta**2))

# Momentum thickness (theta)
theta, _ = quad(momentum_thickness_integrand, 0, 10)
theta *= x / np.sqrt(Re_x)

# Output results
print(f"Boundary layer thickness (delta) at x={x} m: {delta:.4f} m")
print(f"Displacement thickness (delta_star) at x={x} m: {delta_star:.4f} m")
print(f"Momentum thickness (theta) at x={x} m: {theta:.4f} m")
