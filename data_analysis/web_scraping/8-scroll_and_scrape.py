#!/usr/bin/env python3
"""Scrape infinite-scroll products using Selenium."""

import time

from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll and extract unique product details."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            end_time = time.monotonic() + scroll_pause
            new_height = last_height

            while time.monotonic() < end_time:
                time.sleep(0.1)

                new_height = driver.execute_script(
                    "return document.body.scrollHeight"
                )

                if new_height > last_height:
                    break

            if new_height <= last_height:
                break

            last_height = new_height

        products = []
        seen = set()

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

            rating = len(item.find_elements(
                "css selector",
                ".ratings p.ws-icon.ws-icon-star"
            ))

            key = (title, price)

            if key in seen:
                continue

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
