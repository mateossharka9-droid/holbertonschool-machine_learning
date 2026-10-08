#!/usr/bin/env python3
"""Module that plots a cubic line graph"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot a cubic line graph."""
    y = np.arange(0, 11) ** 3
    x = np.arange(0, 11)
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y, 'r-')
    plt.xlim(0, 10)
    plt.show()
