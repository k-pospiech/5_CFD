import numpy as np

# Define the fluid pressure and viscosity
pressure = 101325  # Pressure in Pascals for a static fluid
mu = 1.0e-3        # Dynamic viscosity in Pa.s for a fluid in motion

# Identity matrix for 3D (since stress tensor is a 3x3 matrix)
identity_matrix = np.identity(3)

# Stress tensor for a fluid at rest (only pressure, no shear stress)
stress_tensor_static = -pressure * identity_matrix

# Print the stress tensor for a static fluid
print("Stress tensor for a fluid at rest:")
print(stress_tensor_static)

# Velocity gradient tensor for simple shear flow (example values)
velocity_gradient = np.array([[0, 1, 0],  # du/dx, du/dy, du/dz
                              [0, 0, 0],  # dv/dx, dv/dy, dv/dz
                              [0, 0, 0]]) # dw/dx, dw/dy, dw/dz

# Calculate the deviatoric stress tensor (shear stress) for a fluid in motion
deviatoric_stress_tensor = mu * (velocity_gradient + velocity_gradient.T)

# Combine pressure and shear stress to form the full stress tensor for a fluid in motion
full_stress_tensor = -pressure * identity_matrix + deviatoric_stress_tensor

# Print the full stress tensor for a fluid with simple shear flow
print("\nFull stress tensor for a fluid with simple shear flow:")
print(full_stress_tensor)
