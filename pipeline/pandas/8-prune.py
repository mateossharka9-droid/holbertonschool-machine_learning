#!/usr/bin/env python3
"""Remove rows with null values."""


def prune(df):
    """Remove all rows containing at least one null value."""
    return df.dropna(subset=['Close'])
