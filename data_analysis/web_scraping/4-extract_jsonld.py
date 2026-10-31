#!/usr/bin/env python3
"""Extract quotes from JSON-LD embedded in HTML."""

import json

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quote data from JSON-LD script tags."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        data = json.loads(script.string)

        if data.get("@type") == "Quote":
            tags = data.get("keywords", [])

            if isinstance(tags, str):
                tags = [tag.strip() for tag in tags.split(",")]

            quotes.append({
                "text": data.get("text"),
                "author": data.get("author", {}).get("name"),
                "tags": tags
            })

    return quotes
