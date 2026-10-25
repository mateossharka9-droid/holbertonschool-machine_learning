#!/usr/bin/env python3
"""Scrape quotes from all pages using pagination."""

from bs4 import BeautifulSoup
import time
from urllib import parse

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape all quotes by following Next links."""
    quotes = []
    url = base_url

    while url:
        html = fetch_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        quotes.extend(scrape_basic(url))

        next_page = soup.select_one('li.next a')

        if next_page:
            url = parse.urljoin(url, next_page['href'])
            time.sleep(1)
        else:
            url = None

    return quotes
