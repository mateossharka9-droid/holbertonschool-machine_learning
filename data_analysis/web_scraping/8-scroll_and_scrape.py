#!/usr/bin/env python3
"""Scrape products from an infinite-scroll page using Selenium."""

import time

from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through the page and extract unique products."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(scroll_pause)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if new_height == last_height:
                break

            last_height = new_height

        products = []
        seen = set()

        items = driver.find_elements("css selector", "div.thumbnail")

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

            rating = len(item.find_elements(
                "css selector", ".ratings p.ws-icon.ws-icon-star"
            ))

            key = (title, price)

            if key not in seen:
                seen.add(key)

                products.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": rating
                })

        return products

    finally:
        driver.quit()
