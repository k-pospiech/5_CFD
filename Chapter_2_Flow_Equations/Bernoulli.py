class BernoulliEquation:
    def __init__(self, rho, g):
        self.rho = rho
        self.g = g

    def compute_pressure(self, v, h, constant):
        """Given velocity, height, and Bernoulli constant, compute the pressure."""
        P = constant - 0.5 * self.rho * v**2 - self.rho * self.g * h
        return P

    def compute_velocity(self, P, h, constant):
        """Given pressure, height, and Bernoulli constant, compute the velocity."""
        v = ((constant - P - self.rho * self.g * h) * 2 / self.rho)**0.5
        return v

    def compute_height(self, P, v, constant):
        """Given pressure, velocity, and Bernoulli constant, compute the height."""
        h = (constant - P - 0.5 * self.rho * v**2) / (self.rho * self.g)
        return h

    def compute_bernoulli_constant(self, P, v, h):
        """Given pressure, velocity, and height, compute the Bernoulli constant."""
        constant = P + 0.5 * self.rho * v**2 + self.rho * self.g * h
        return constant

# Example usage
rho = 1000  # density of water in kg/m^3
g = 9.81  # gravitational acceleration in m/s^2
bernoulli = BernoulliEquation(rho, g)

P = 101325  # atmospheric pressure in Pascals
v = 10  # velocity in m/s
h = 5  # height in meters

# Compute the Bernoulli constant for given P, v, and h
constant = bernoulli.compute_bernoulli_constant(P, v, h)
print(f"Bernoulli Constant: {constant} Pa")

# Compute the velocity for given P, h, and Bernoulli constant
v_new = bernoulli.compute_velocity(P, 2, constant)
print(f"Velocity at height 2m: {v_new} m/s")