import numpy as np
import matplotlib.pyplot as plt

def compute_trajectory(r_0, theta_0, t, k):
    """
    Compute the trajectory of a particle in a flow field defined in cylindrical coordinates.

    Parameters:
    - r_0 (float): initial radial distance of the particle.
    - theta_0 (float): initial angle of the particle.
    - t (float or np.array): time or time points at which the position is calculated.
    - k (float): a constant defined in the flow field equations.

    Returns:
    - r_t (float or np.array): radial position(s) of the particle at time t.
    - theta_t (float or np.array): angular position(s) of the particle at time t.
    """
    r_t = r_0
    theta_t = theta_0 + k * t / (2 * np.pi * r_0)
    return r_t, theta_t

def plot_trajectories(t, r_0_values, k):
    """
    Plot the trajectories of particles in a polar plot.
    
    Parameters:
    - t (float): time point up to which to plot the trajectories.
    - r_0_values (list of float): initial radial distances for which to plot the trajectories.
    - k (float): a constant defined in the flow field equations.
    """
    # Create a polar subplot
    ax = plt.subplot(111, projection='polar')
    
    # For each initial radial distance
    for r_0 in r_0_values:
        theta_0 = 0  # initial angular position
        r_t, theta_t = compute_trajectory(r_0, theta_0, t, k)
        
        # Plotting
        ax.plot([theta_0, theta_t], [r_0, r_t], label=f"$r_0$ = {r_0}")
    
    ax.set_title("Trajectories of Particles ($t$ = {:.2f})".format(t))
    ax.legend()
    plt.show()

# Constants and Parameters
k = 1
t = 3  # time up to which trajectories are plotted
r_0_values = [0.2, 0.3, 0.4, 0.5]  # initial radial distances

# Plotting
plot_trajectories(t, r_0_values, k)