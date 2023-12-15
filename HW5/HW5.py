from scipy.optimize import fsolve
import numpy as np

# Given values
rho = 1.0  # kg/m^3
mu = 1.5e-5  # kg/(m s)
U0 = 10  # m/s
R = 0.1  # m
Re_D = (rho * U0 * R) / mu

# Function to find lambda_DW using the Colebrook equation
def colebrook(lambda_dw):
    return 1/np.sqrt(lambda_dw) - 2.0 * np.log10(Re_D * np.sqrt(lambda_dw)) + 0.8

# Initial guess for lambda_DW
initial_guess = 0.02

# Solve for lambda_DW
lambda_DW_solution = fsolve(colebrook, initial_guess)

# Calculate friction velocity u*
u_star = np.sqrt(lambda_DW_solution * (U0**2) / (2 * R))

lambda_DW_solution[0], u_star[0]

print(lambda_DW_solution)
