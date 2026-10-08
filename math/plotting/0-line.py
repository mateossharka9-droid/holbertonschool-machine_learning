#!/usr/bin/env python3
"""Module that plots a line graph of y = x^3 for x in range(0, 11)"""
import numpy as np
import matplotlib.pyplot as plt


def line():
"""Plot a line graph of a cubic function."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, 'r-')
    plt.xlim(0, 10)
    plt.show()
