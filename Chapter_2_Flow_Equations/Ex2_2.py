def compute_forces(rho, U1, P1, P2, Pa, A):
    """Compute the forces Fx and Fy exerted by the fluid on the elbow of the pipe."""
    Fx = -rho * U1**2 * (P1 - Pa) * A
    Fy = -rho * U1**2 * (P2 - Pa) * A
    return Fx, Fy

# Given values (you can replace these with actual values)
rho = 1000  # Fluid density in kg/m^3 (assuming water for this example)
U1 = 1.0  # Velocity at the elbow's inlet in m/s
P1 = 101325 + 5000  # Pressure at station 1 in Pa (assuming a bit higher than atmospheric pressure)
P2 = 101325 + 3000  # Pressure at station 2 in Pa (assuming a bit higher than atmospheric pressure)
Pa = 101325  # Atmospheric pressure in Pa
A = 0.01  # Cross-sectional area of the pipe in m^2

# Compute the forces
Fx, Fy = compute_forces(rho, U1, P1, P2, Pa, A)
print(f"Force Fx: {Fx} N")
print(f"Force Fy: {Fy} N")
