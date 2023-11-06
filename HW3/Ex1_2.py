from sympy import symbols, Function, diff, Derivative, simplify, Eq, init_printing

# Initialize pretty printing
init_printing(use_unicode=True)

# Define the symbolic variables and functions
x, r, nu, rho, P0, Pa, R, U0 = symbols('x r nu rho P_0 P_a R U_0')
x_tilde, r_tilde = symbols('x_tilde r_tilde')  # Define as separate symbols
U = Function('U')(x, r)
V = Function('V')(x, r)
P = Function('P')(x, r)

# Define dimensionless functions in terms of x and r
U_tilde = U / U0
V_tilde = V / U0
P_tilde = (P - Pa) / (rho * U0**2)

# Substitute x_tilde = x / R and r_tilde = r / R in the dimensionless functions
U_tilde = U_tilde.subs({x: x_tilde * R, r: r_tilde * R})
V_tilde = V_tilde.subs({x: x_tilde * R, r: r_tilde * R})
P_tilde = P_tilde.subs({x: x_tilde * R, r: r_tilde * R})

# Now take the derivatives with respect to x_tilde and r_tilde
dU_tilde_dx_tilde = diff(U_tilde, x_tilde)
dU_tilde_dr_tilde = diff(U_tilde, r_tilde)
dV_tilde_dx_tilde = diff(V_tilde, x_tilde)
dV_tilde_dr_tilde = diff(V_tilde, r_tilde)
dP_tilde_dx_tilde = diff(P_tilde, x_tilde)

# Define the dimensionless equations
# Continuity equation
eq1 = Eq(dU_tilde_dx_tilde + (1/r_tilde) * diff(r_tilde * V_tilde, r_tilde), 0)

# Radial momentum equation
eq2 = Eq(dU_tilde_dx_tilde + V_tilde*dU_tilde_dr_tilde - dP_tilde_dx_tilde +
         nu * (diff(U_tilde, x_tilde, x_tilde) + (1/r_tilde) * diff(r_tilde * dU_tilde_dr_tilde, r_tilde)), 0)

# Axial momentum equation
eq3 = Eq(dV_tilde_dx_tilde + V_tilde*dV_tilde_dr_tilde - (1/rho)*dP_tilde_dx_tilde +
         nu * (diff(V_tilde, x_tilde, x_tilde) + (1/r_tilde) * diff(r_tilde * dV_tilde_dr_tilde, r_tilde) - V_tilde/r_tilde**2), 0)

# Output the dimensionless equations
print(eq1, eq2, eq3)
