# Given upstream temperature T1 (ambient temperature)
T1 = 288  # in Kelvin
M1n = 1.021
M2n = 0.979
gamma = 1.4

# Calculate the temperature ratio using the incident Mach number (M1n)
temperature_ratio = ((2*gamma*M1n**2 - (gamma - 1))/(gamma + 1))*((2 + ((gamma - 1)*M1n**2))/((gamma + 1) * M1n**2))

# Calculate the downstream temperature T2
T2 = temperature_ratio * T1
print(temperature_ratio, T2)

# Given values
R = 287.1  # Specific gas constant for air, J/(kg·K)

# Calculate the speed of sound upstream of the shock (a1)
a1 = (gamma * R * T2)**0.5

# Calculate the velocity behind the shock with respect to the ground (Vi)
# Using the Mach number downstream of the shock (M2n)
V1 = M2n * a1
print(a1, V1)
