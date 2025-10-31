import os
import json
import time

def fetch_link(code: str) -> str:
    """
    🚧 Replace this with your actual scraping / HTTP logic
    Right now: Just return a dummy link using code part before '|'
    """
    video_id = code.split("|")[0]
    return f"https://example.com/video/{video_id}.mkv"

def update_status(url: str):
    status = {
        "running": False,
        "url": url
    }
    with open("run_status.json", "w") as f:
        json.dump(status, f)

def main():
    code = os.getenv("CODE", "")
    if not code:
        raise Exception("CODE input missing!")

    print("Processing Code:", code)
    time.sleep(3)  # Simulating work

    final_link = fetch_link(code)
    update_status(final_link)
    print("✅ Link generated:", final_link)

if __name__ == "__main__":
    main()
