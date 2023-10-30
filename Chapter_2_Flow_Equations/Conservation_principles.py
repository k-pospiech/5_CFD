import numpy as np

class Fluid:
    def __init__(self, density, viscosity):
        self.rho = density        # Density
        self.mu = viscosity       # Dynamic viscosity

# 1. Conservation of Mass (Continuity Equation)
def continuity_equation(rho, u, A):
    # rho: density
    # u: velocity
    # A: cross-sectional area
    return rho * u * A

# 2. Conservation of Momentum (Euler's equation for inviscid flows)
def momentum_equation(dpdx, u, rho):
    # dpdx: pressure gradient
    # Applying Euler's equation
    # u du/dx = -1/rho * dpdx
    dudx = -1/rho * dpdx
    # Returning the change in velocity due to pressure gradient
    return u + dudx

# 3. Conservation of Energy (Energy Equation)
# For simplicity, considering the Bernoulli's equation for inviscid flows
def bernoulli_equation(rho, u, p):
    # rho: density
    # u: velocity
    # p: pressure
    # Kinetic Energy term + Potential Energy term + Pressure Energy term = constant
    # 0.5 * u^2 + g*z + p/rho = constant
    # For simplicity, assuming change in height (z) is zero
    constant = 0.5 * u**2 + p/rho
    return constant

if __name__ == "__main__":
    # Given fluid properties
    water = Fluid(1000, 0.001)  # rho in kg/m^3, mu in Pa.s
    
    # Example values
    u = 2           # m/s
    A = 0.01        # m^2
    p = 101325      # Pa
    dpdx = -100     # Pa/m, example value for pressure gradient
    
    mass_flow_rate = continuity_equation(water.rho, u, A)
    print(f"Mass Flow Rate: {mass_flow_rate} kg/s")

    new_velocity_due_to_pressure_gradient = momentum_equation(dpdx, u, water.rho)
    print(f"New Velocity due to Pressure Gradient: {new_velocity_due_to_pressure_gradient} m/s")

    energy_conservation = bernoulli_equation(water.rho, u, p)
    print(f"Bernoulli's Constant: {energy_conservation} J/kg")

