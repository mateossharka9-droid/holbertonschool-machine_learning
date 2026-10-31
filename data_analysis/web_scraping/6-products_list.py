#!/usr/bin/env python3
"""Scrape static products using Selenium."""

import time

from selenium import webdriver


def scrape_products(url):
    """Return a list of product dictionaries."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)

        products = []

        items = driver.find_elements(
            "css selector", "div.thumbnail"
        )

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


scrape_products_list = scrape_products
