import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Base URL to scrape (Using a public quotes website for demo)
BASE_URL = "http://quotes.toscrape.com/page/{}/"

# List to store scraped data
scraped_data = []

# Rate Limiting configuration (delay in seconds between requests)
DELAY_SECONDS = 2

# Number of pages to scrape
TOTAL_PAGES = 3

print("Starting Web Scraping process...\n")

for page in range(1, TOTAL_PAGES + 1):
    url = BASE_URL.format(page)
    print(f"Scraping page: {url}")

    # Set custom User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # 1. HTML Parsing
        soup = BeautifulSoup(response.text, "html.parser")

        # 2. Data Extraction
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()

            scraped_data.append({"Quote": text, "Author": author})

        print(f"Page {page} scraped successfully.")
    else:
        print(
            f"Failed to load page {page}. Status Code: {response.status_code}"
        )

    # 3. Rate Limiting: Delay execution to prevent server overloading
    print(f"Waiting for {DELAY_SECONDS} seconds...\n")
    time.sleep(DELAY_SECONDS)

# 4. CSV Export: Saving extracted data into a CSV file
df = pd.DataFrame(scraped_data)
csv_filename = "scraped_quotes.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"Scraping completed! Data saved to '{csv_filename}'.")
