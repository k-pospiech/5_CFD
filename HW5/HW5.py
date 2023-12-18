import numpy as np
from scipy.optimize import fsolve

# Given values
rho = 1.0  # density of air in kg/m^3
U0 = 10  # average flow velocity in m/s
R = 0.1  # outer radius of the duct in meters
mu = 1e-5  # dynamic viscosity in kg/(m s)

# Calculate kinematic viscosity
nu = mu / rho  # kinematic viscosity in m^2/s

# Calculate the Reynolds number
Re_D = (rho * U0 * R) / mu

# Define the Colebrook equation to solve for lambda_DW
def colebrook(lambda_dw):
    return 1/np.sqrt(lambda_dw) - 2.0 * np.log10(Re_D * np.sqrt(lambda_dw)) + 0.8

# Initial guess for lambda_DW
initial_guess = 0.02

# Solve for lambda_DW
lambda_DW_solution = fsolve(colebrook, initial_guess)

# Calculate friction velocity u*
u_star = np.sqrt(lambda_DW_solution * (U0**2) / (2 * R))

# Calculate the axial pressure gradient
dp_dx = lambda_DW_solution * (rho * U0**2) / (2 * R)

# Display the results
print(Re_D, lambda_DW_solution[0], u_star[0], dp_dx[0], nu)