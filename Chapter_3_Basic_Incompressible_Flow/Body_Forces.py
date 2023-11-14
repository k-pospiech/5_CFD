import numpy as np

# Define the control volume dimensions (meters)
length = 2.0  # Length of the control volume in the x-direction
width = 1.0   # Width of the control volume in the y-direction
height = 1.0  # Height of the control volume in the z-direction

# Define the fluid properties
rho = 1000    # Density of the fluid (kg/m^3)
g = 9.81      # Acceleration due to gravity (m/s^2)
pressure = 101325  # Pressure at the top surface of the fluid (Pa)

# Calculate the volume of the control volume
volume = length * width * height

# Calculate the body force due to gravity
body_force = rho * volume * g

# Calculate the force due to pressure on the top surface
# Assuming pressure is only acting on the top surface and is uniform
pressure_force = pressure * length * width

print(f"Body force due to gravity on the fluid: {body_force:.2f} N")
print(f"Force due to pressure on the top surface: {pressure_force:.2f} N")
