import numpy as np

# Sample velocity field and scalar field
def velocity_field(x, y, z):
    u = y
    v = -x
    w = z
    return u, v, w

def scalar_field(x, y, z):
    return x**2 + y**2 + z**2

# 1. Substantial Derivative
def substantial_derivative(phi, x, y, z, delta=1e-5):
    u, v, w = velocity_field(x, y, z)
    
    dphi_dx = (phi(x + delta, y, z) - phi(x, y, z)) / delta
    dphi_dy = (phi(x, y + delta, z) - phi(x, y, z)) / delta
    dphi_dz = (phi(x, y, z + delta) - phi(x, y, z)) / delta
    
    Dphi_Dt = u*dphi_dx + v*dphi_dy + w*dphi_dz
    return Dphi_Dt

# 2. Convective Flux
def convective_flux(phi, x, y, z):
    u, v, w = velocity_field(x, y, z)
    value = phi(x, y, z)
    return value * np.array([u, v, w])

# Example Usage
x, y, z = 1, 2, 3
print("Substantial Derivative:", substantial_derivative(scalar_field, x, y, z))
print("Convective Flux:", convective_flux(scalar_field, x, y, z))
