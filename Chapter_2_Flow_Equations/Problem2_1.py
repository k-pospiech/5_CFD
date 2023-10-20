import math

def jet_deflector_forces(rho, U1, h1, h2, p1, p2, pa, alpha_deg):
    # Convert alpha from degrees to radians
    alpha = math.radians(alpha_deg)
    
    # Conservation of mass to find U2
    U2 = U1 * (h1/h2)
    
    # Y-direction forces
    Y_momentum_2 = rho * U2**2 * h2 * math.sin(alpha)
    Y_pressure_force = (p2 - pa) * h2 * math.sin(alpha)
    Fy_fluid = Y_momentum_2 + Y_pressure_force
    
    # X-direction forces
    X_momentum_1 = -rho * U1**2 * h1
    X_pressure_force_1 = (pa - p1) * h1
    X_momentum_2 = rho * U2**2 * h2 * math.cos(alpha)
    X_pressure_force_2 = (p2 - pa) * h2 * math.cos(alpha)
    Fx_fluid = X_momentum_1 + X_pressure_force_1 + X_momentum_2 - X_pressure_force_2
    
    # Forces that must be externally exerted on the deflector to hold it in place
    Fx_external = -Fx_fluid
    Fy_external = -Fy_fluid
    
    return Fx_external, Fy_external

# Example usage:
rho = 1000  # Density in kg/m^3, example value
U1 = 10     # Velocity at station 1 in m/s, example value
h1 = 0.1    # Height at station 1 in m, example value
h2 = 0.2    # Height at station 2 in m, example value
p1 = 100000 # Pressure at station 1 in Pa, example value
p2 = 90000  # Pressure at station 2 in Pa, example value
pa = 101325 # Ambient pressure in Pa, example value
alpha_deg = 30  # Angle in degrees, example value

Fx, Fy = jet_deflector_forces(rho, U1, h1, h2, p1, p2, pa, alpha_deg)
print(f"Externally exerted force in X-direction: {Fx} N")
print(f"Externally exerted force in Y-direction: {Fy} N")
