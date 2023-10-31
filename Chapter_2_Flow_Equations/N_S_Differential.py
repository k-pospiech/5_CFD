import sympy as sp

def navier_stokes_differential(rho, mu):
    # Define the velocity components and pressure as functions of space (x, y, z) and time t
    x, y, z, t = sp.symbols('x y z t')
    u = sp.Function('u')(x, y, z, t)
    v = sp.Function('v')(x, y, z, t)
    w = sp.Function('w')(x, y, z, t)
    p = sp.Function('p')(x, y, z, t)

    # Partial derivatives
    du_dt = sp.Derivative(u, t)
    du_dx = sp.Derivative(u, x)
    du_dy = sp.Derivative(u, y)
    du_dz = sp.Derivative(u, z)

    # Viscous terms
    laplacian_u = sp.diff(sp.diff(u, x), x) + sp.diff(sp.diff(u, y), y) + sp.diff(sp.diff(u, z), z)
    viscous_term = mu * laplacian_u

    # Inertia term
    inertia = rho * (u * du_dx + v * du_dy + w * du_dz)

    # Navier-Stokes in the x-direction (similarly, we can define for y and z directions)
    NS_x = sp.Eq(du_dt + inertia, -sp.diff(p, x) + viscous_term)
    
    return NS_x

rho = 1000  # density, kg/m^3
mu = 0.001  # viscosity, Pa.s

eqn = navier_stokes_differential(rho, mu)
print(eqn)
