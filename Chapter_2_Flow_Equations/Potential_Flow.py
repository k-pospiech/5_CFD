import numpy as np

class SourceFlow:
    def __init__(self, m):
        """Initialize the source flow with a given strength m."""
        self.m = m

    def potential(self, x, y):
        """Calculate the potential function at a given point (x, y)."""
        r = np.sqrt(x**2 + y**2)
        if r == 0:
            return float('inf')  # Avoid division by zero
        return (self.m / (2 * np.pi)) * np.log(r)

    def velocity(self, x, y):
        """Calculate the velocity components (u, v) at a given point (x, y)."""
        r_sq = x**2 + y**2
        if r_sq == 0:
            return (0, 0)  # Avoid division by zero
        u = (self.m / (2 * np.pi)) * (x / r_sq)
        v = (self.m / (2 * np.pi)) * (y / r_sq)
        return (u, v)

# Example usage
source_strength = 5  # Arbitrary source strength
flow = SourceFlow(source_strength)

x, y = 1, 1  # Coordinates of the point

phi = flow.potential(x, y)
u, v = flow.velocity(x, y)

print(f"Potential at ({x}, {y}): {phi}")
print(f"Velocity at ({x}, {y}): u = {u}, v = {v}")