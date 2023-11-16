def ideal_gas_law(P=None, V=None, T=None, n=None, R=8.314):
    """
    Calculate the missing variable from the ideal gas law.
    PV = nRT
    """
    if P is None:
        return n * R * T / V
    elif V is None:
        return n * R * T / P
    elif T is None:
        return P * V / (n * R)
    elif n is None:
        return P * V / (R * T)
    else:
        return None

# Example usage:
P = ideal_gas_law(V=0.0224, T=273.15, n=1)  # Standard temperature and pressure
print(f"Pressure: {P} Pa")

T = ideal_gas_law(P=101325, V=0.0224, n=1)  # Standard pressure and molar volume
print(f"Temperature: {T} K")
