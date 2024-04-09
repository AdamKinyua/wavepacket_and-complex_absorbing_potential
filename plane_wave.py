import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
A = 0.1  # Amplitude of the wave
k = 5  # Wave number

# Generate x values
x = np.linspace(-3, 2*np.pi, 1000)  # Range from 0 to 2*pi

# Calculate the wave function
psi = A * np.sin(k * x)

# Plot the wave function
plt.plot(x, psi, label=r'$\psi(x) = A \sin(kx)$')

# Label the axes
plt.xlabel('x')
plt.ylabel(r'$\psi$')

# Add a legend
plt.legend()

# Show the plot
plt.show()
