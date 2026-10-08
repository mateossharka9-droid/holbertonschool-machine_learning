#!/usr/bin/env python3
"""Load a DataFrame from a file."""
import pandas as pd


def from_file(filename, delimiter):
    """Load data from a file as a pandas DataFrame."""
    return pd.read_csv(filename, delimiter=delimiter)
