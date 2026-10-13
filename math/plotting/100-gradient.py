#!/usr/bin/env python3
"""Plot a scatter plot of mountain elevations."""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Display mountain elevations using a color gradient."""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

    plt.figure(figsize=(6.4, 4.8))

    scatter = plt.scatter(x, y, c=z, cmap='viridis')

    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')

    colorbar = plt.colorbar(scatter)
    colorbar.set_label('elevation (m)')

    plt.show()
