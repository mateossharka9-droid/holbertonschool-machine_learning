#!/usr/bin/env python3
"""Scrape quotes from the first page of a website."""

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Extract quote text, author, and tags from a webpage."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    quotes = []

    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').get_text(strip=True)
        author = quote.select_one('small.author').get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote.select('a.tag')
        ]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes
