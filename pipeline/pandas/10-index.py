#!/usr/bin/env python3


def index(df):
    """Set Timestamp as the DataFrame index."""
    return df.set_index('Timestamp')
