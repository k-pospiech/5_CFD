import numpy as np

# Constants and flow properties
mu = 1.0e-3    # Dynamic viscosity (Pa.s or N.s/m^2)
U_0 = 2.0      # Average velocity (m/s)
L = 1.0        # Length of the tube (m)
R = 0.05       # Radius of the tube (m)
rho = 1000     # Density of the fluid (kg/m^3)
nu = mu / rho  # Kinematic viscosity (m^2/s)

# Calculate Reynolds number
Re = U_0 * (2 * R) / nu

# Function to calculate entrance length
def calculate_entrance_length(Re, R):
    return (0.06 * Re) * R

# Function to calculate skin friction coefficient in developing flow (using Blasius)
def calculate_skin_friction_developing(Re):
    return 0.664 / np.sqrt(Re)

# Function to calculate skin friction coefficient in fully developed flow
def calculate_skin_friction_fully_developed(Re):
    return 16 / Re

# Function to calculate pressure drop using Hagen-Poiseuille equation
def calculate_pressure_drop(mu, U_0, L, R):
    return (8 * mu * U_0 * L) / (np.pi * R**4)

# Perform calculations
x_0 = calculate_entrance_length(Re, R)
cf_developing = calculate_skin_friction_developing(Re)
cf_fully_de
