import numpy as np

# Given data from the document
gamma = 1.4  # Specific heat ratio for air
R = 287  # Specific gas constant for air in J/(kg*K)
T_inf = 288  # Free-stream temperature in Kelvin
P_inf = 100000  # Free-stream pressure in Pascals
a_inf = np.sqrt(gamma * R * T_inf)  # Speed of sound in air at T_inf

# Mach numbers for the cases
M_0_6 = 0.6
M_1_4 = 1.4

# Free-stream velocity calculation
U_inf_0_6 = M_0_6 * a_inf
U_inf_1_4 = M_1_4 * a_inf

# Turbulence intensity (assumed or given)
Tu_inf = 0.01  # Turbulence intensity at free-stream

# Free-stream turbulent kinetic energy calculation
k_inf_0_6 = (3/2) * (U_inf_0_6 * Tu_inf)**2
k_inf_1_4 = (3/2) * (U_inf_1_4 * Tu_inf)**2

# Total pressure calculation using isentropic relations
Pt_inf_0_6 = P_inf * (1 + (gamma - 1)/2 * M_0_6**2)**(gamma/(gamma - 1))
Pt_inf_1_4 = P_inf * (1 + (gamma - 1)/2 * M_1_4**2)**(gamma/(gamma - 1))

print(U_inf_0_6, U_inf_1_4, k_inf_0_6, k_inf_1_4, Pt_inf_0_6, Pt_inf_1_4)