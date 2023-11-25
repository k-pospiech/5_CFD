import numpy as np

def least_squares_gradient(scalar_field, dx, dy):
    """
    Calculate the gradient of a scalar field in a 2D structured grid using the least squares method.

    Parameters:
    scalar_field (2D array): The scalar field values at cell centers.
    dx (float): Cell width in the x-direction.
    dy (float): Cell height in the y-direction.

    Returns:
    gradient_x, gradient_y (2D arrays): The x and y components of the gradient.
    """
    nx, ny = scalar_field.shape
    gradient_x = np.zeros_like(scalar_field)
    gradient_y = np.zeros_like(scalar_field)

    for i in range(1, nx-1):
        for j in range(1, ny-1):
            A = np.array([[dx, 0], [0, dy], [-dx, 0], [0, -dy]])
            b = np.array([scalar_field[i+1, j] - scalar_field[i, j], 
                          scalar_field[i, j+1] - scalar_field[i, j],
                          scalar_field[i-1, j] - scalar_field[i, j],
                          scalar_field[i, j-1] - scalar_field[i, j]])

            # Least squares solution
            ATA_inv = np.linalg.inv(A.T @ A)
            ATb = A.T @ b
            grad = ATA_inv @ ATb

            gradient_x[i, j], gradient_y[i, j] = grad

    return gradient_x, gradient_y

# Example usage
nx, ny = 10, 10  # Grid dimensions
dx, dy = 1.0, 1.0  # Cell dimensions
scalar_field = np.random.rand(nx, ny)  # Example scalar field

# Calculate gradient
grad_x, grad_y = least_squares_gradient(scalar_field, dx, dy)

# Print results
print("Gradient in x-direction:\n", grad_x)
print("Gradient in y-direction:\n", grad_y)
