import numpy as np
import matplotlib.pyplot as plt

def centered_interpolation(x, f):
    """
    Perform centered interpolation on a discrete set of data points.

    Parameters:
    x (array): The x-coordinates of the data points.
    f (array): The function values at the data points.

    Returns:
    x_mid (array): The x-coordinates of the midpoints.
    f_mid (array): The interpolated function values at the midpoints.
    """
    x_mid = (x[:-1] + x[1:]) / 2
    f_mid = (f[:-1] + f[1:]) / 2
    return x_mid, f_mid

# Example usage
x = np.linspace(0, 10, 6)          # x-coordinates of the data points
f = np.sin(x)                       # Function values at the data points

# Perform centered interpolation
x_mid, f_mid = centered_interpolation(x, f)

# Plotting the results
plt.plot(x, f, 'o-', label='Original Data')
plt.plot(x_mid, f_mid, 's', label='Interpolated Data')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Centered Interpolation')
plt.grid(True)
plt.show()
