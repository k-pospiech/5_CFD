def jet_deflector_calculations(U1, h1, h2, alpha_degrees, rho=1000, pa=101325):
    """
    Calculates the velocity U2 and the forces exerted on a jet deflector.

    Parameters:
    - U1: Initial velocity of the fluid (m/s)
    - h1: Initial height of the jet (m)
    - h2: Height of the jet after deflection (m)
    - alpha_degrees: Deflection angle in degrees
    - rho: Density of the fluid (default is 1000 kg/m^3 for water)
    - pa: Atmospheric pressure (default is 101325 Pa)

    Returns:
    - U2: Velocity of the fluid after deflection (m/s)
    - F_net_x: Net force in the x-direction (N)
    - F_net_y: Net force in the y-direction (N)
    """
    import math

    # Convert angle to radians
    alpha = math.radians(alpha_degrees)

    # Calculate U2 from conservation of mass
    U2 = (h1 / h2) * U1

    # Calculate momentum forces
    m_dot = rho * h1 * U1  # Mass flow rate
    Fx = m_dot * U2 * math.cos(alpha) - m_dot * U1
    Fy = m_dot * U2 * math.sin(alpha)

    # Calculate pressure forces
    F_pressure_y = pa * h1

    # Calculate net forces to hold the deflector in place
    F_net_x = -Fx
    F_net_y = -(Fy + F_pressure_y)

    return U2, F_net_x, F_net_y

# Example usage:
U1 = 10  # m/s, just a sample value
h1 = 0.05  # m, just a sample value
h2 = 0.03  # m, just a sample value
alpha_degrees = 30  # degrees, just a sample value

U2, F_net_x, F_net_y = jet_deflector_calculations(U1, h1, h2, alpha_degrees)
print(f"U2: {U2:.2f} m/s")
print(f"F_net_x: {F_net_x:.2f} N")
print(f"F_net_y: {F_net_y:.2f} N")