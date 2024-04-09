import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters
amplitude = 1.0
frequency = 2 * np.pi  # Adjust for desired frequency (cycles/second)
duration = 10.0  # Animation duration (seconds)
fps = 30  # Frames per second

# Generate time values
t = np.linspace(0, duration, int(duration * fps))

# Generate x values
x = np.linspace(0, 2 * np.pi, 100)  # Adjust for number of points in the wave

# Define initial title
title_template = f'Sign Wave at t = {{:.2f}} s'

# Create figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(frequency * x), label='Sign Wave')  # Plot for initial time step

# Set plot limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-amplitude - amplitude / 5, amplitude + amplitude / 5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(title_template.format(t[0]))
ax.legend()


# Initialization function
def init():
    return line,


# Animation function
def animate(i):
    # Update y-values of the line based on current time
    y = amplitude * np.sin(frequency * x - frequency * t[i])
    line.set_ydata(y)

    # Update title with current time
    ax.set_title(title_template.format(t[i]))

    return line,


# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=1000 / fps, blit=True)

# Show the animation
plt.show()
