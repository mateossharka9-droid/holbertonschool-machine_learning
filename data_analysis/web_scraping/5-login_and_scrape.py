#!/usr/bin/env python3
"""Login to Quotes to Scrape and extract quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Login using a session and scrape quotes."""
    session = requests.Session()

    # Get login page and extract CSRF token
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, "html.parser")

    csrf_token = soup.find("input", {"name": "csrf_token"})["value"]

    # Submit login credentials
    data = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }

    session.post(login_url, data=data)

    # Access quotes page using the same session
    response = session.get("https://quotes.toscrape.com/")
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote.find_all("a", class_="tag")
        ]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes
