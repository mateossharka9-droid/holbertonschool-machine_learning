# !/usr/bin/env python3
"""Find the home planets of sentient Star Wars species using SWAPI."""

import requests


def sentientPlanets():
    """Return the names of the home planets of all sentient species."""
    homeworld_ids = set()
    url = "https://swapi.dev/api/species/"

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            if classification == "sentient" or designation == "sentient":
                homeworld = species.get("homeworld")
                if homeworld:
                    homeworld_ids.add(homeworld.rstrip("/").split("/")[-1])

        url = data.get("next")

    planets = []
    url = "https://swapi.dev/api/planets/"

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for planet in data.get("results", []):
            planet_id = planet["url"].rstrip("/").split("/")[-1]
            if planet_id in homeworld_ids:
                planets.append(planet["name"])

        url = data.get("next")

    return planets
