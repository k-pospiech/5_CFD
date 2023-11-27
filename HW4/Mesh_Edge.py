def calculate_mesh_parameters(d1, dn, L):
    """
    Calculate the bias factor and number of elements for a mesh.
    
    Parameters:
    d1 (float): Size of the first element.
    dn (float): Size of the final element.
    L (float): Total length of the segment.

    Returns:
    n (int): Number of elements.
    q (float): Bias factor.
    """
    # Initial guess for n and q
    n = 2
    q = (dn / d1) ** (1 / (n - 1))

    while True:
        # Sum of geometric series
        L_calc = d1 * (1 - q**n) / (1 - q)

        if L_calc > L:
            break
        else:
            n += 1
            q = (dn / d1) ** (1 / (n - 1))

    return n, q

# Example usage
d1 = 0.028  # Size of the first element
dn = 1.22  # Size of the final element
L = 125.0   # Total length of the segment

n, q = calculate_mesh_parameters(d1, dn, L)

print(f"Number of elements: {n}")
print(f"Bias factor: {q:.2f}")
