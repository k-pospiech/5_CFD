import numpy as np
import matplotlib.pyplot as plt

# Parameters
max_velocity = 2.0    # Maximum velocity in m/s
ramp_up_time = 10.0   # Time to reach maximum velocity in seconds
time_steps = 100      # Number of time steps to analyze

# Time array
time = np.linspace(0, ramp_up_time, time_steps)

# Velocity calculation (linear ramp-up)
velocity = np.minimum(time / ramp_up_time * max_velocity, max_velocity)

# Plotting
plt.plot(time, velocity)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Unsteady Channel Flow - Velocity Ramp-Up')
plt.grid(True)
plt.show()
