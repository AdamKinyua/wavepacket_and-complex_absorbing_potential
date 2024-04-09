import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
h_bar = 1  # Planck's constant (for simplicity, taken as 1)
A = 1  # Amplitude of the wavepacket
k0 = 1  # Central wave number (for the initial wavepacket)
sigma = 0.1  # Width of the wavepacket
x_min = -5
x_max = 5
t_max = 10
frames = 100


# Define the wavefunction for a single plane wave
def plane_wave(x, k):
    return np.sin(k * x)


# Define the Gaussian envelope for the wavepacket
def gaussian_envelope(x, x0, sigma):
    return np.exp(-0.5 * ((x - x0) / sigma) ** 2)


# Create the animation function
def animate_wavepacket(frame):
    t = frame * t_max / frames
    ax.clear()
    ax.set_title(f"Time = {t:.2f}")
    ax.set_xlabel("Position")
    ax.set_ylabel("Probability Density")

    # Calculate the wavepacket by superposition of plane waves
    wavepacket = np.zeros_like(x)
    for k in range(-10, 11):
        wavepacket += A * plane_wave(x, k / 10) * gaussian_envelope(x, 0.5 * t, sigma)

    # Plot the wavepacket
    ax.plot(x, wavepacket ** 2, color='blue')


# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, 1.1)
ax.axhline(0, color='black', lw=0.5)

# Generate x values
x = np.linspace(x_min, x_max, 1000)

# Create the animation
ani = FuncAnimation(fig, animate_wavepacket, frames=frames, interval=50)

plt.show()
