import numpy as np

class IdealGas:
    def __init__(self, R):
        """Initialize the ideal gas with a specific gas constant R."""
        self.R = R

    def compute_P(self, n, V, T):
        """Compute pressure using the ideal gas equation of state."""
        return n * self.R * T / V

    def compute_V(self, n, P, T):
        """Compute volume using the ideal gas equation of state."""
        return n * self.R * T / P

    def compute_T(self, n, P, V):
        """Compute temperature using the ideal gas equation of state."""
        return P * V / (n * self.R)

    def delta_U(self, n, Cv, delta_T):
        """Compute change in internal energy for an ideal gas."""
        return n * Cv * delta_T

    def delta_H(self, n, Cp, delta_T):
        """Compute change in enthalpy for an ideal gas."""
        return n * Cp * delta_T

    def delta_S(self, n, Cp, T_initial, T_final):
        """Compute entropy change for an ideal gas given initial and final temperatures."""
        return n * Cp * np.log(T_final/T_initial)

# Example usage
R = 8.314  # Universal gas constant in J/(mol*K)
n = 1  # Moles of gas
V = 1  # Volume in m^3
T = 300  # Temperature in K
Cv = 20.8  # Specific heat at constant volume in J/(mol*K)
Cp = 29.1  # Specific heat at constant pressure in J/(mol*K)

gas = IdealGas(R)
P = gas.compute_P(n, V, T)
print(f"Pressure of the gas: {P} Pa")

delta_T = 10  # Temperature change in K
dU = gas.delta_U(n, Cv, delta_T)
print(f"Change in internal energy: {dU} J")

dH = gas.delta_H(n, Cp, delta_T)
print(f"Change in enthalpy: {dH} J")

T_new = T + delta_T
dS = gas.delta_S(n, Cp, T, T_new)
print(f"Change in entropy: {dS} J/mol*K")
