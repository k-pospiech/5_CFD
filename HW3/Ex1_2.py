from sympy import symbols, Function, diff, simplify, init_printing, latex
from sympy.printing import pprint

# Initialize pretty printing
init_printing()

# Define the symbolic variables
U0, R, nu, rho, P0, Pa = symbols('U_0 R nu rho P_0 P_a')

# Define dimensionless symbols
x_tilde, r_tilde = symbols('x_tilde r_tilde')
U_tilde = Function('U_tilde')(x_tilde, r_tilde)
V_tilde = Function('V_tilde')(x_tilde, r_tilde)
P_tilde = Function('P_tilde')(x_tilde, r_tilde)

# Define the derivatives for U_tilde and V_tilde
dU_tilde_dx_tilde = diff(U_tilde, x_tilde)
dV_tilde_dr_tilde = diff(V_tilde, r_tilde)
dU_tilde_dr_tilde = diff(U_tilde, r_tilde)
dV_tilde_dx_tilde = diff(V_tilde, x_tilde)
dP_tilde_dx_tilde = diff(P_tilde, x_tilde)

# Dimensionless derivatives needed for the equations
d2U_tilde_dx_tilde2 = diff(U_tilde, x_tilde, 2)
d2V_tilde_dr_tilde2 = diff(V_tilde, r_tilde, 2)

# Dimensionless equations based on the provided equations
dimensionless_equations = [
    simplify(dU_tilde_dx_tilde + (1/r_tilde) * diff(r_tilde * V_tilde, r_tilde) - dP_tilde_dx_tilde + nu * (d2U_tilde_dx_tilde2 + (1/r_tilde) * diff(r_tilde * dU_tilde_dr_tilde, r_tilde))),
    simplify(dV_tilde_dx_tilde + dV_tilde_dr_tilde - dP_tilde_dx_tilde + nu * (d2V_tilde_dr_tilde2 + (1/r_tilde) * diff(r_tilde * dV_tilde_dr_tilde, r_tilde) - V_tilde / r_tilde**2))
]

# Pretty print the dimensionless equations
for eq in dimensionless_equations:
    pprint(eq)
    print("\nLaTeX representation:")
    print(latex(eq))
    print('-'*50)
