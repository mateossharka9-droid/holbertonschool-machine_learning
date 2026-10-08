#!/usr/bin/env python3

def slice(df):
    """Select specific columns and every 60th row."""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']][::60]
