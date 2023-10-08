import numpy as np
import matplotlib.pyplot as plt

def visualize_particle_motion(k, x0, y0, t_max):
    """
    Visualize the temporal evolution and trajectory of a particle in a 2D Eulerian velocity field

    Parameters:
    - k: constant parameter in the velocity field
    - x0, y0: initial positions of the particle in the x and y directions respectively
    - t_max: maximum time for the simulation

    Outputs:
    - Two plots:
        1. Temporal evolution of x(t) and y(t)
        2. Trajectory in the xy-plane
    """

    # Time vector
    t = np.linspace(0, t_max, 100)

    # Equations of motion
    x_t = x0 * np.exp(k*t)
    y_t = y0 * np.exp(-k*t)

    # Plotting x(t) and y(t)
    plt.figure(figsize=[12,6])

    plt.subplot(1,2,1)
    plt.plot(t, x_t, label=r"$x(t) = x_0 e^{kt}$")
    plt.plot(t, y_t, label=r"$y(t) = y_0 e^{-kt}$")
    plt.xlabel('Time, t')
    plt.ylabel('Position')
    plt.title('Temporal Evolution')
    plt.legend()
    plt.grid(True)

    # Plotting the trajectory in xy-plane
    plt.subplot(1,2,2)
    x = np.linspace(0.1, 2*x0, 400)  # Ensuring x does not go to zero to avoid division by zero
    y = x0 * y0 / x  # Using xy = x0y0 to get y as a function of x
    plt.plot(x, y, label=r"Trajectory: $xy = x_0y_0$")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Particle Path')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def visualize_additional_paths(k, x0, y0_values, t_max):
    """
    Visualize the trajectories of particles with different initial conditions in the y direction.
    
    Parameters:
    - k: constant parameter in the velocity field
    - x0: initial position in the x direction
    - y0_values: array-like, initial positions in the y direction
    - t_max: maximum time for the simulation
    
    Outputs:
    - Plot of different trajectories in the xy-plane
    """
    
    # Time vector
    t = np.linspace(0, t_max, 100)  
    
    # Plotting additional paths
    plt.figure(figsize=[6, 6])
    for y0 in y0_values:
        y_t = y0 * np.exp(-k*t)
        x_t = x0 * np.exp(k*t)
        plt.plot(x_t, y_t, label=f"y0 = {y0}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Additional Particle Paths')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Example usage
k = 1
x0, y0 = 1, 1
t_max = 2
y0_values = np.arange(0.5, 3.1, 0.5)

visualize_particle_motion(k, x0, y0, t_max)
visualize_additional_paths(k, 0.1, y0_values, t_max)