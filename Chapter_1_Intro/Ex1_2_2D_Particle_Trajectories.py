import numpy as np
import matplotlib.pyplot as plt

def compute_trajectory(r_0, theta_0, t_max, dt):
    """
    Computes the trajectory of a particle in a velocity field defined in polar coordinates.

    Parameters:
    - r_0: initial radial distance
    - theta_0: initial angular position
    - t_max: maximum time for computation
    - dt: time step size
    
    Returns:
    - x_vals, y_vals: x and y coordinates of the particle's position over time
    """
    times = np.arange(0, t_max, dt)
    theta_vals = theta_0 + times / (2 * np.pi * r_0)
    r_vals = r_0 * np.ones_like(times)
    
    x_vals = r_vals * np.cos(theta_vals)
    y_vals = r_vals * np.sin(theta_vals)
    
    return x_vals, y_vals

def plot_trajectory(r_0_values, theta_0, t_max, dt):
    """
    Plots the trajectory of a particle based on the specified initial conditions and time parameters.

    Parameters:
    - r_0_values: list of initial radial distances
    - theta_0: initial angular position
    - t_max: maximum time for computation
    - dt: time step size
    """
    plt.figure(figsize=(8, 8))
    
    for r_0 in r_0_values:
        x_vals, y_vals = compute_trajectory(r_0, theta_0, t_max, dt)
        plt.plot(x_vals, y_vals, label=f'$r_0$ = {r_0}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Particle Trajectories in a Velocity Field')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Given/Assumed Values
r_0_values = [0.2, 0.3, 0.4, 0.5]
theta_0 = 0  # Assuming an initial angle of 0 for simplicity
t_max = 3  # Maximum time
dt = 0.01  # Time step

# Plotting the trajectory
plot_trajectory(r_0_values, theta_0, t_max, dt)
