import numpy as np

# 1. Define Constants and Hartree-Fock (HF) Equations:
# atomic positions
positions = np.array([
    [0.0, 0.0, 0.37],
    [0.0, 0.0, -0.37]
])

# nuclear charges
charges = np.array([1, 1])

# atomic masses
masses = np.array([1.007825, 1.007825])  # In atomic mass units (amu)

"""
Harmonic oscillator constant (k): This value depends on the specific bond and needs to be obtained from 
literature or other calculations. For this example, we'll assume a representative value.
"""
# harmonic oscillator constant
k = 420.0  # Harmonic oscillator constant (au)

"""
Conversion factor: Convert from atomic units (au) to cm^-1 for vibrational frequencies.
"""
au_to_cm = 219474.6  # Conversion factor (cm^-1/au)

"""
Hartree-Fock (HF) equations: While not explicitly implemented here due to their complexity, 
these equations form the foundation of the calculation. They are a set of coupled differential 
equations that describe the electronic structure of a molecule, including the potential energy.
"""


# implementing numerical differentiation

def get_energy(positions):
    # Simulate a calculation here (replace with your actual calculation)
    # This is a placeholder, as the actual energy calculation would involve
    # solving the HF equations or using an appropriate computational chemistry method.
    energy = 0.0
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                distance = np.linalg.norm(positions[i] - positions[j])
                energy += -1 / distance
    return energy


def get_force(positions, index):
    """
    Calculates the forces acting on the atom at index 'index' in all directions (x, y, z).

    Args:
        positions (numpy.ndarray): Array of atomic positions (shape: n_atoms x 3).
        index (int): Index of the atom for which to calculate the force.

    Returns:
        numpy.ndarray: Array containing the forces in x, y, and z directions (shape: 3).
    """

    # Small displacement for numerical differentiation
    epsilon = 1e-4

    # Calculate forces in positive and negative displacement directions
    positive_displacement = positions.copy()
    positive_displacement[index] += epsilon
    negative_displacement = positions.copy()
    negative_displacement[index] -= epsilon

    # Calculate energy differences
    delta_energy_positive = get_energy(positive_displacement) - get_energy(positions)
    delta_energy_negative = get_energy(negative_displacement) - get_energy(positions)

    # Calculate forces using central difference formula
    forces = (delta_energy_positive - delta_energy_negative) / (2 * epsilon)

    return forces


# calculating hessian
hessian = np.zeros((len(positions) * 3, len(positions) * 3))
print(hessian)
for i in range(len(positions)):
    for j in range(len(positions)):
        for k in range(3):  # Loop over all Cartesian coordinates
            print(i,j,k)
            forces = get_force(positions.copy(), i * 3 + k)
            hessian[i * 3 + k, j * 3 + k] = forces[k]  # Access correct element based on k

# solving the eigenvalue problem
eigenvalues, eigenvectors = np.linalg.eig(hessian)

# interpreting the results
"""
The diagonal elements of the Hessian matrix correspond to the force constants for individual vibrational modes.
The eigenvalues represent the squares of the vibrational frequencies in atomic units (au). 
Convert them to cm^-1 using the au_to_cm factor.
The eigenvectors describe the normal modes of vibration, which can be analyzed to understand the specific 
atomic motions involved in each mode.
"""
