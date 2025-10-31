import sys
import time
from urllib.parse import quote
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_movie_url(code):
    target_url = f"https://home-player.netlify.app/fetcher.html?code={quote(code)}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(target_url)

        time.sleep(10)  # wait for JS redirect

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]

    if len(links) > 2:
        return f"player.html?movieUrl={quote(links[2])}"
    return "ERROR: Less than 3 links found"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing code")
        sys.exit(1)

    print(fetch_movie_url(sys.argv[1]))
