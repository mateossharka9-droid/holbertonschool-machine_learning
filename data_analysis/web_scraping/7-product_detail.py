#!/usr/bin/env python3
"""Scrape product details using Selenium."""

import time

from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Extract product title, price, description, and rating."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        title = driver.find_elements(
            "css selector", ".caption h4"
        )[1].text

        price = driver.find_element(
            "css selector", "h4.price"
        ).text

        description = driver.find_element(
            "css selector", "p.description"
        ).text

        rating = int(driver.find_element(
            "css selector", ".ratings p[data-rating]"
        ).get_attribute("data-rating"))

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }

    finally:
        driver.quit()
