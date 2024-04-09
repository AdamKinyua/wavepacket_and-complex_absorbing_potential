import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 1.0  # Amplitude
x0 = 0.0  # Initial center position
sigma = 1.0  # Width parameter
k = 10.0  # Wave number
omega = 1.0  # Angular frequency
x_min = 0.0  # Minimum x value
x_max = 10.0  # Maximum x value

x = np.linspace(x_min, x_max, 1000)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
line_real, = ax.plot([], [], lw=2, label='Real Part')
line_imaginary, = ax.plot([], [], lw=2, label='Imaginary Part')
line_magnitude, = ax.plot([], [], lw=2, linestyle='--', label='Magnitude')


# Initialization function: plot the background of each frame
def init():
    line_real.set_data([], [])
    line_imaginary.set_data([], [])
    line_magnitude.set_data([], [])
    return line_real, line_imaginary, line_magnitude


def animate(t):
    # Calculate the shifted x values
    x_shifted = 10 * np.abs(np.sin(omega * t))
    if x_shifted > x_max:
        x_shifted = x_max

    psi = A * np.exp(-((x - x_shifted - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * (k * (x - x_shifted) - omega * t))

    line_real.set_data(x, psi.real)
    line_imaginary.set_data(x, psi.imag)

    magnitude = np.abs(psi)
    line_magnitude.set_data(x, magnitude)

    return line_real, line_imaginary, line_magnitude, ax.title


# Set plot limits
ax.set_xlim(x_min, x_max)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Position')
ax.set_ylabel('Wavefunction')
ax.set_title('Evolution of wavepacket with time')
ax.legend()

# animating
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 1000), init_func=init, blit=True, interval=20)
plt.show()
