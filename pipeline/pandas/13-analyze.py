#!/usr/bin/env python3
"""Compute descriptive statistics excluding Timestamp."""
import pandas as pd


def analyze(df):
    """Compute descriptive statistics excluding Timestamp."""
    return df.drop(columns=['Timestamp']).describe()
