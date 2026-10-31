#!/usr/bin/env python3
"""Scrape static product listings using Selenium."""

import time

from selenium import webdriver


def scrape_products_list(url):
    """Extract product details from a static category page."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)

        products = []

        items = driver.find_elements("css selector", ".thumbnail")

        for item in items:
            title = item.find_element(
                "css selector", "a.title"
            ).get_attribute("title")

            price = item.find_element(
                "css selector", "h4.price"
            ).text

            description = item.find_element(
                "css selector", "p.description"
            ).text

            rating = int(item.find_element(
                "css selector", ".ratings p[data-rating]"
            ).get_attribute("data-rating"))

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })

        return products

    finally:
        driver.quit()
