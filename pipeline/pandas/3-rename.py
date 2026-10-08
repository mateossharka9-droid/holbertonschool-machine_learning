#!/usr/bin/env python3
"""Rename and convert the Timestamp column."""
import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime and convert it to datetime."""
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]
