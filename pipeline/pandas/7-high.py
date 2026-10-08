#!/usr/bin/env python3


def high(df):
    """Sort DataFrame by High price in descending order."""
    return df.sort_values(by='High', ascending=False)
