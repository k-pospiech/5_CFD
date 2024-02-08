# Given values
Ta = 288  # Ambient temperature in K
gamma = 1.4  # Specific heat ratio
Rg = 287.1  # Specific gas constant for air in J/(kg·K)

# Calculated values
M1 = 1.021  # Incident Mach number upstream of the shock
M2 = 0.979  # Transmitted Mach number downstream of the shock
a1 = (gamma * Rg * Ta)**0.5  # Speed of sound upstream of the shock

# Calculate the temperature ratio using the incident Mach number (M1n)
temperature_ratio = ((2*gamma*M1**2 - (gamma - 1))/(gamma + 1))*((2 + ((gamma - 1)*M1**2))/((gamma + 1) * M1**2))

# Calculate the downstream temperature T2
T2 = temperature_ratio * Ta
a2 = (gamma * Rg * T2)**0.5  # Speed of sound downstream of the shock

# Calculate the speed behind the shock wave
U2 = M2 * a2

# Calculate the speed of the shock wave
Usw = M1 * a1

# Calculate the speed of the air behind the shock wave
U1 = Usw - U2

print(a1, a2, U2, Usw, U1)

# Output: 340.233331700467 342.5909777776772 335.396567244346 347.37823166617676 11.981664421830772