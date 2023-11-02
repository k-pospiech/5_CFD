from sympy import symbols, Eq, solve

def parse_dimensions(dim_str):
    """Parses dimension string into a dictionary."""
    dimensions = {}
    i = 0
    while i < len(dim_str):
        if dim_str[i] in ['^', '-']:
            power = int(dim_str[i+1])
            if dim_str[i] == '-':
                power = -power
            dimensions[dim_str[i-1]] = power
            i += 2
        else:
            dimensions[dim_str[i]] = 1
            i += 1
    return dimensions

def buckingham_pi(variables, basic_dims):
    pi_terms = []

    # List of symbols
    coeffs = symbols('a0:' + str(len(variables)))
    equations = []

    for dim in basic_dims:
        equation = sum([coeffs[j] * parse_dimensions(dim_val).get(dim, 0) for j, dim_val in enumerate(variables.values())])
        equations.append(equation)

    solutions = solve(equations, coeffs)

    # Generate the Pi terms
    for i, coeff in enumerate(coeffs):
        pi_term = f"Pi_{i+1} = {variables.keys()[i]}^{solutions[coeff]}"
        pi_terms.append(pi_term)

    return pi_terms

if __name__ == "__main__":
    variables = {
        'V': 'LT^-1',
        'L': 'L',
        'rho': 'ML^-3',
        'mu': 'ML^-1T^-1',
        'g': 'LT^-2'
    }
    dimensions = ['M', 'L', 'T']

    pi_groups = buckingham_pi(variables, dimensions)
    for group in pi_groups:
        print(group)
