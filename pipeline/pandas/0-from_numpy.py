#!/usr/bin/env python3
"""Module that creates a pd.DataFrame from a np.ndarray"""
import pandas as pd
import numpy as np


def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray.

    Args:
        array: the np.ndarray from which to create the pd.DataFrame.

    The columns are labeled in alphabetical order and capitalized
    (A, B, C, ...). There will not be more than 26 columns.

    """
    columns = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
