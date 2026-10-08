#!/usr/bin/env python3
"""Select specific columns and rows from a DataFrame."""


def slice(df):
    """Select specific columns and every 60th row."""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']][::60]
