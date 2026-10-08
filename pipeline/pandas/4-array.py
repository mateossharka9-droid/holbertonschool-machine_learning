#!/usr/bin/env python3

import numpy as np


def array(df):
    """Select the last 10 High and Close values as a NumPy array."""
    return df[['High', 'Close']].tail(10).to_numpy()
