#!/usr/bin/env python3
"""Compute descriptive statistics excluding Timestamp."""


def analyze(df):
    """Compute descriptive statistics excluding Timestamp."""
    return df.drop(columns=['Timestamp']).describe()
