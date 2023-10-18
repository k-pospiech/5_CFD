import numpy as np

def jet_deflector_calculations(U1, h1, h2, alpha, rho, pa):
    """
    Parameters:
    U1: Incoming velocity at section 1 (m/s)
    h1: Height of the jet at section 1 (m)
    h2: Height of the jet at section 2 (m)
    alpha: Angle between the jet at section 2 and horizontal (radians)
    rho: Density of the fluid (kg/m^3)
    pa: Ambient pressure (Pa)

    Returns:
    U2: Velocity at section 2 (m/s)
    Fx: Force exerted in the x-direction (N)
    Fy: Force exerted in the y-direction (N)
    """
    
    # Using conservation of mass to determine U2
    U2 = (U1 * h1) / h2

    # Using momentum equation in x and y directions
    Fx = (rho * U2**2 * h2 * np.cos(alpha)) - (rho * U1**2 * h1)
    Fy = (rho * U2**2 * h2 * np.sin(alpha)) + (pa * h1) - (pa * h2)

    return U2, Fx, Fy

# Example Usage
U1 = 5.0  # Example incoming velocity in m/s
h1 = 0.1  # Example height at section 1 in m
h2 = 0.08  # Example height at section 2 in m
alpha = np.radians(30)  # Example angle in radians (converted from 30 degrees)
rho = 1000  # Density of water in kg/m^3
pa = 101325  # Atmospheric pressure in Pa

U2, Fx, Fy = jet_deflector_calculations(U1, h1, h2, alpha, rho, pa)
print(f"U2: {U2} m/s, Fx: {Fx} N, Fy: {Fy} N")