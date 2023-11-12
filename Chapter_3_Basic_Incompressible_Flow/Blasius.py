import scipy.integrate as spi
import numpy as np

# Parameters
U_0 = 1.0       # Free-stream velocity in m/s
nu = 1.5e-5     # Kinematic viscosity in m^2/s
x = 0.1         # Distance from the leading edge of the plate in m

# Calculate local Reynolds number
Re_x = U_0 * x / nu

# Blasius solution for the boundary layer thickness (delta) and skin friction coefficient (cf)
delta = 5.0 * x / np.sqrt(Re_x)  # Approximate boundary layer thickness
cf = 0.664 / np.sqrt(Re_x)       # Skin friction coefficient using Blasius solution

print(f"Local Reynolds number at x={x} m: Re_x = {Re_x:.2f}")
print(f"Boundary layer thickness at x={x} m: delta = {delta:.5f} m")
print(f"Skin friction coefficient at x={x} m: cf = {cf:.5f}")
