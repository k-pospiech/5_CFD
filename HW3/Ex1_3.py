import math

# Given parameters
U_0 = 1.0  # Characteristic velocity (m/s), replace with your value
R = 0.05   # Radius of the tube (m), replace with your value
nu = 1e-6  # Kinematic viscosity (m^2/s), replace with your value

# Compute the Reynolds number
Re = U_0 * R / nu

# Calculate the dimensionless length x_tilde_0
x_tilde_0 = (1/4) * Re

print(f"The dimensionless length x_tilde_0 where viscous effects cover the radial extent of the duct is: {x_tilde_0:.5f}")
