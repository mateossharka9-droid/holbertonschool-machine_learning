#!/usr/bin/env python3
"""Sort a DataFrame by the High price."""


def high(df):
    """Sort DataFrame by High price in descending order."""
    return df.sort_values(by='High', ascending=False)
