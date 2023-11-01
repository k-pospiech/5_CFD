from sympy import symbols, Eq, solve

def buckingham_pi(variables, dimensions):
    """
    Applies the Buckingham Pi theorem to get dimensionless groups.

    Parameters:
    - variables: Dictionary of variables and their dimensions. E.g., {'V': 'LT^-1', 'rho': 'ML^-3'}
    - dimensions: List of basic dimensions. E.g., ['M', 'L', 'T']

    Returns:
    List of dimensionless groups.
    """
    pi_terms = []

    # Number of variables
    n = len(variables)

    # Number of fundamental dimensions
    k = len(dimensions)

    # Calculate the number of Pi terms
    r = n - k

    for i in range(r):
        coeffs = symbols('a:{}:{}'.format(i, n))
        equation = []

        for j, (var, dim) in enumerate(variables.items()):
            term = ''.join([dim[dim_index] + str(int(dim[dim_index+1]) + coeffs[j]) for dim_index in range(0, len(dim), 2)])
            equation.append(term)

        # Setting up the equation such that the sum of the coefficients for each dimension is zero
        equations = [Eq(''.join([eqn[2 * i + 1] for eqn in equation if eqn[2 * i] == dim]), 0) for i, dim in enumerate(dimensions)]

        solutions = solve(equations)

        pi_term = 'Pi_{} = '.format(i+1) + ' * '.join(['{}^{}'.format(var, sol) for var, sol in zip(variables.keys(), solutions)])
        pi_terms.append(pi_term)

    return pi_terms

if __name__ == "__main__":
    # Example
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
