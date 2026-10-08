#!/usr/bin/env python3
"""Set Timestamp as the DataFrame index."""


def index(df):
    """Set Timestamp as the DataFrame index."""
    return df.set_index('Timestamp')
