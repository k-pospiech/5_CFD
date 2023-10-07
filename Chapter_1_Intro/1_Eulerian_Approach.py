import numpy as np
import matplotlib.pyplot as plt

def initial_condition(x):
    """
    Defines the initial condition.
    
    Parameters:
        x (np.ndarray): The spatial grid.
        
    Returns:
        np.ndarray: The field variable phi at t=0.
    """
    return np.exp(-40 * (x-5)**2)

def ftcs_advection(phi_old, u, dt, dx):
    """
    Performs one time step of the FTCS scheme for the 1D advection equation.
    
    Parameters:
        phi_old (np.ndarray): The old solution.
        u (float): The velocity.
        dt (float): The time step size.
        dx (float): The spatial step size.
        
    Returns:
        np.ndarray: The new solution after one time step.
    """
    phi_new = phi_old.copy()
    phi_new[1:-1] = phi_old[1:-1] - u*dt/(2*dx) * (phi_old[2:] - phi_old[:-2])
    return phi_new

def plot_results(x, phi0, phi, Nt):
    """
    Plots the initial and final states of the advection solution.
    
    Parameters:
        x (np.ndarray): The spatial grid.
        phi0 (np.ndarray): The initial state.
        phi (np.ndarray): The final state.
        Nt (int): The number of time steps.
    """
    plt.plot(x, phi0, label="Initial condition")
    plt.plot(x, phi, label=f"After {Nt} time steps")
    plt.legend()
    plt.xlabel("Position")
    plt.ylabel("$\phi$")
    plt.title("1D Advection Equation using FTCS scheme")
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to run the 1D advection simulation.
    """
    # Parameters
    L = 10.0         # Length of the domain
    Nx = 100         # Number of spatial points
    dx = L/(Nx-1)    # Spatial step
    u = 1.0          # Velocity
    dt = 0.04        # Time step
    Nt = 25          # Number of time steps
    
    # Discretize the spatial domain
    x = np.linspace(0, L, Nx)

    # Initial condition
    phi = initial_condition(x)
    phi0 = phi.copy()
    
    # Time integration using FTCS
    for _ in range(Nt):
        phi = ftcs_advection(phi, u, dt, dx)

    # Plot the results
    plot_results(x, phi0, phi, Nt)

if __name__ == "__main__":
    main()
