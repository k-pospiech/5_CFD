import numpy as np
import matplotlib.pyplot as plt

def compute_trajectory(r_0, theta_0, t_max, dt, Gamma):
    """
    Compute the trajectory of a particle in a velocity field defined in polar coordinates.
    
    Parameters:
        r_0 (float): Initial radial distance.
        theta_0 (float): Initial angular position in radians.
        t_max (float): Maximum time for computation.
        dt (float): Time step size.
        Gamma (float): Angular velocity coefficient.
        
    Returns:
        tuple: x and y coordinates (NumPy arrays) of the particle's position over time.
    """
    times = np.arange(0, t_max, dt)
    theta_vals = theta_0 + Gamma * times / (2 * np.pi * r_0**2)
    r_vals = r_0 * np.ones_like(times)
    
    x_vals = r_vals * np.cos(theta_vals)
    y_vals = r_vals * np.sin(theta_vals)
    
    return x_vals, y_vals

# Additional comments and descriptions have been added for clarity.

def plot_trajectory(r_0_values, theta_0, t_max, dt, Gamma):
    """
    Plot the trajectory of a particle for different initial radial distances.

    Parameters:
        r_0_values (list of float): Initial radial distances.
        theta_0 (float): Initial angular position in radians.
        t_max (float): Maximum time for computation.
        dt (float): Time step size.
        Gamma (float): Angular velocity coefficient.
    """
    plt.figure(figsize=(8, 8))
    
    for r_0 in r_0_values:
        x_vals, y_vals = compute_trajectory(r_0, theta_0, t_max, dt, Gamma)
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
t_max = 0.24  # Maximum time
dt = 0.01  # Time step
Gamma = 2*np.pi # Angular velocity coefficient

# Updated to include Gamma in function call
plot_trajectory(r_0_values, theta_0, t_max, dt, Gamma)
