import numpy as np

# Given data
mu = 1.0e-3    # Dynamic viscosity in kg/(m·s)
rho = 1000     # Density of fluid in kg/m^3
U_avg = 2.0    # Average velocity in m/s
L = 1.0        # Length of the pipe in m
R = 0.05       # Radius of the pipe in m
P_0 = 101325   # Reference pressure (atmospheric) in Pa

# Calculate pressure drop Delta P using the Hagen-Poiseuille equation
Delta_P = (8 * mu * U_avg * L) / (R**2)

# Wall shear stress tau_w
tau_w = (Delta_P * R) / (2 * L)

# Calculate the pressure coefficient Cp (assuming P at the exit is P_0)
Cp = (2 * (P_0 - (P_0 - Delta_P))) / (rho * U_avg**2)

# Calculate the friction coefficient cf
cf = (2 * tau_w) / (rho * U_avg**2)

print(f"Pressure coefficient Cp: {Cp}")
print(f"Friction coefficient cf: {cf}")
