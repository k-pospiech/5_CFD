import numpy as np
import matplotlib.pyplot as plt

def solve_convection_diffusion_1d(phi, u, Gamma, dx, dt, nt, S=0):
    """
    Solve the 1D unsteady convection-diffusion equation using finite difference method.
    
    Parameters:
    phi (array): Initial scalar field
    u (float): Velocity of the fluid
    Gamma (float): Diffusion coefficient
    dx (float): Spatial step size
    dt (float): Time step size
    nt (int): Number of time steps
    S (float, optional): Source term (default is 0)
    
    Returns:
    phi (array): Scalar field after nt time steps
    """
    for t in range(nt):
        phi_old = phi.copy()
        for i in range(1, len(phi) - 1):
            convection = u * (phi_old[i] - phi_old[i-1]) / dx
            diffusion = Gamma * (phi_old[i+1] - 2*phi_old[i] + phi_old[i-1]) / dx**2
            phi[i] = phi_old[i] + dt * (-convection + diffusion + S)

        # Apply boundary conditions (e.g., Dirichlet or Neumann)
        phi[0], phi[-1] = phi[1], phi[-2]  # Simple Neumann boundary conditions for demonstration

    return phi

# Parameters
L = 10.0       # Length of the domain
nx = 100       # Number of spatial points
dx = L / nx    # Spatial step size
u = 1.0        # Fluid velocity
Gamma = 0.1    # Diffusion coefficient
dt = 0.01      # Time step size
nt = 100       # Number of time steps

# Initial condition (e.g., Gaussian distribution)
x = np.linspace(0, L, nx)
phi_initial = np.exp(-((x - L/2)**2) / 0.1)

# Solve
phi = solve_convection_diffusion_1d(phi_initial, u, Gamma, dx, dt, nt)

# Plotting
plt.plot(x, phi, label='Phi at t={:.2f}'.format(nt*dt))
plt.xlabel('x')
plt.ylabel('Phi')
plt.title('1D Unsteady Convection-Diffusion')
plt.legend()
plt.show()
