import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 1 # Assume a value for R; we're using dimensionless units so R = 1 is appropriate

# Define the dimensionless velocities
def Ur(r, theta):
    return (1 - 1/r**2) * np.cos(theta) 

def Utheta(r, theta):
    return -(1 + 1/r**2) * np.sin(theta)

# Determine stagnation points by setting both velocities to zero
def stagnation_points():
    # For Ur = 0:
    r_values = [1, 1]
    theta_values = [0, np.pi]
    
    return r_values, theta_values

# Plotting 
theta = np.linspace(0, 2*np.pi, 200)
r = np.linspace(0.1, 2, 200)
R, Theta = np.meshgrid(r, theta)

U_R = Ur(R, Theta)
U_Theta = Utheta(R, Theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.quiver(Theta, R, U_R, R*U_Theta)  # Plotting the velocity vectors

# Stagnation points
r_stag, theta_stag = stagnation_points()
ax.plot(theta_stag, r_stag, 'ro')  # Red dots for stagnation points

# Streamline for r'=1
ax.plot([0, 2*np.pi], [1, 1], 'g--')  # Dashed green line for streamline

plt.show()