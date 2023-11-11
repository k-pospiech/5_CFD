# Constants for the calculation
mu = 1.0e-3    # Viscosity of the fluid (Pa.s or N.s/m^2), insert the correct value
U_0 = 2.0      # Average velocity (m/s), insert the correct value
L = 1.0        # Length of the tube (m), insert the correct value
R = 0.05       # Radius of the tube (m), insert the correct value

# Calculate the Reynolds number
Re = (U_0 * (2*R)) / mu  # Note: U_0 is typically based on the diameter for pipe flow

# Calculate dimensionless pressure drop (P'0)
P_prime_0 = 8 * L / (Re * R)

# Calculate physical pressure drop (P_0 - P_a)
pressure_drop = P_prime_0 * (mu * U_0 / R**2)

print(f"The dimensionless pressure drop P'0 is: {P_prime_0:.5f}")
print(f"The physical pressure drop (P_0 - P_a) is: {pressure_drop:.5f} Pa")
