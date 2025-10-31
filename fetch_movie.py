import os, json, time
from requests_html import HTMLSession

def extract_link(code: str) -> str:
    session = HTMLSession()

    # ✅ Use code argument properly
    target_url = f"https://home-player.netlify.app/fetcher.html?code={code}"
    print("Fetching:", target_url)

    r = session.get(target_url)

    # ✅ Let redirect + JS run fully
    time.sleep(10)
    r.html.render(timeout=20, sleep=5)

    # ✅ Scrape all anchor links
    links = [
        link.attrs.get("href")
        for link in r.html.find("a")
        if link.attrs.get("href")
    ]

    print("Links found:", links)

    # ✅ Pick index 2 if exists
    if len(links) > 2:
        return links[2]
    return ""

def update_status(url: str):
    status = {"running": False, "url": url}
    with open("run_status.json", "w") as f:
        json.dump(status, f)

def main():
    code = os.getenv("CODE")  # ✅ Action input passed here
    if not code:
        raise Exception("No CODE argument supplied!")

    final_url = extract_link(code)
    update_status(final_url)
    print("✅ Final URL:", final_url)

if __name__ == "__main__":
    main()
