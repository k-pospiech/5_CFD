def reynolds_number(rho, u, L, mu):
    """
    rho: fluid density (kg/m^3)
    u: flow speed (m/s)
    L: characteristic length (m)
    mu: dynamic viscosity (Pa·s)
    """
    Re = (rho * u * L) / mu
    return Re

def froude_number(u, L, g):
    """
    u: flow speed (m/s)
    L: characteristic length (m)
    g: acceleration due to gravity (m/s^2)
    """
    Fr = u / (g * L)**0.5
    return Fr

def euler_number(p, rho, u):
    """
    p: pressure difference (Pa)
    rho: fluid density (kg/m^3)
    u: flow speed (m/s)
    """
    Eu = p / (rho * u**2)
    return Eu

def mach_number(u, a):
    """
    u: flow speed (m/s)
    a: speed of sound in the fluid (m/s)
    """
    Ma = u / a
    return Ma

def bond_number(rho_l, rho_g, L, g, sigma):
    """
    rho_l: density of liquid (kg/m^3)
    rho_g: density of gas (kg/m^3)
    L: characteristic length (m)
    g: acceleration due to gravity (m/s^2)
    sigma: surface tension (N/m)
    """
    Bo = (rho_l - rho_g) * g * L**2 / sigma
    return Bo

def weber_number(rho, u, L, sigma):
    """
    rho: fluid density (kg/m^3)
    u: flow speed (m/s)
    L: characteristic length (m)
    sigma: surface tension (N/m)
    """
    We = rho * u**2 * L / sigma
    return We

def nusselt_number(h, L, k):
    """
    h: convective heat transfer coefficient (W/m^2·K)
    L: characteristic length (m)
    k: thermal conductivity of the fluid (W/m·K)
    """
    Nu = h * L / k
    return Nu

# Example usage:
# You would replace the following with the actual values for your specific situation.
rho = 1000    # Fluid density in kg/m^3
u = 2         # Flow speed in m/s
L = 0.5       # Characteristic length in m
mu = 0.001    # Dynamic viscosity in Pa·s
g = 9.81      # Gravity in m/s^2
p = 101325    # Pressure difference in Pa
a = 343       # Speed of sound in m/s
sigma = 0.072 # Surface tension in N/m
rho_g = 1.2   # Density of gas in kg/m^3
h = 50        # Convective heat transfer coefficient in W/m^2·K
k = 0.6       # Thermal conductivity in W/m·K

print(f"Reynolds number: {reynolds_number(rho, u, L, mu)}")
print(f"Froude number: {froude_number(u, L, g)}")
print(f"Euler number: {euler_number(p, rho, u)}")
print(f"Mach number: {mach_number(u, a)}")
print(f"Bond number: {bond_number(rho, rho_g, L, g, sigma)}")
print(f"Weber number: {weber_number(rho, u, L, sigma)}")
print(f"Nusselt number: {nusselt_number(h, L, k)}")
