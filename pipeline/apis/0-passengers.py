#!/usr/bin/env python3
"""Retrieve starships based on passenger capacity using SWAPI."""

import requests


def availableShips(passengerCount):
    """Return names of ships that can carry at least passengerCount."""
    ships = []
    url = "https://swapi.dev/api/starships/"

    while url is not None:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "unknown")
            passengers = passengers.replace(",", "")

            if passengers.isdigit():
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])

        url = data.get("next")

    return ships
