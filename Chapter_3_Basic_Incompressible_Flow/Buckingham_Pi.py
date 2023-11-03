from sympy import symbols, solve, Eq

def get_dimensions(var):
    return variables[var]

def form_dimensionless_product(target, repeating_vars):
    a, b, c = symbols('a b c')
    target_dims = get_dimensions(target)

    # Creating the dimensional equation for the product
    product_dims = {
        'M': 0,
        'L': 0,
        'T': 0
    }

    symbol_to_var = {}  # To map back symbols to variable names
    for var, symbol in repeating_vars.items():
        dims = get_dimensions(var)
        for dim, value in dims.items():
            product_dims[dim] += value * symbol
        symbol_to_var[symbol] = var

    # Setting up the equations based on the powers of dimensions
    eqns = []
    for dim, power in target_dims.items():
        eqns.append(Eq(product_dims[dim] + power, 0))

    sol = solve(eqns, (a, b, c))
    
    # Constructing the Pi term
    pi_term = f"{target} / ("
    for symbol, power in sol.items():
        var = symbol_to_var[symbol]
        pi_term += f"{var}^{power} * "
    pi_term = pi_term.rstrip(" * ") + ")"

    return pi_term

if __name__ == "__main__":
    # Example usage
    variables = {
        'V': {'L': 1, 'T': -1},
        'L': {'L': 1},
        'rho': {'M': 1, 'L': -3},
        'mu': {'M': 1, 'L': -1, 'T': -1},
        'g': {'L': 1, 'T': -2}
    }
    
    # Choosing three repeating variables (as an example)
    repeating = {
        'V': symbols('a'),
        'L': symbols('b'),
        'rho': symbols('c')
    }

    # Find dimensionless products for the rest of the variables
    for var in set(variables.keys()) - set(repeating.keys()):
        print(form_dimensionless_product(var, repeating))
