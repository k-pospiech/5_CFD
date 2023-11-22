import numpy as np
import matplotlib.pyplot as plt

# Parameters
nx, ny = 40, 40        # Number of grid points
dx, dy = 1.0/nx, 1.0/ny  # Grid spacing
nt = 500               # Number of time steps
dt = 0.001             # Time step size
U_top = 1.0            # Lid velocity
nu = 0.01              # Kinematic viscosity

# Initialize velocity and pressure fields
u = np.zeros((ny, nx))
v = np.zeros((ny, nx))
p = np.zeros((ny, nx))

for n in range(nt):
    un = u.copy()
    vn = v.copy()

    # Velocity field (u, v) update using central differences and Euler forward method
    u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
                     dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                     dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) +
                     nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                     nu * dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))

    v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                     dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                     dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) +
                     nu * dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                     nu * dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1]))

    # Boundary conditions
    u[0, :], u[-1, :], u[:, 0], u[:, -1] = 0, 0, 0, 0  # u = 0 at walls
    v[0, :], v[-1, :], v[:, 0], v[:, -1] = 0, 0, 0, 0  # v = 0 at walls
    u[-1, :] = U_top  # Lid moving at U_top

# Plot the velocity field
Y, X = np.mgrid[0:1:ny*1j, 0:1:nx*1j]
plt.streamplot(X, Y, u, v, density=2, arrowstyle='->', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Lid-driven Cavity Flow')
plt.show()
