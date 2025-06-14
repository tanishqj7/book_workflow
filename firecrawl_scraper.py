# # import requests

# # FIRECRAWL_API_KEY = "fc-f36a1fb1bfb748958deac871096bc72b"

# # def scrape_firecrawl_text(url):
# #     endpoint = "https://api.firecrawl.dev/v1/scrape"
# #     headers = {
# #         "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
# #         "Content-Type": "application/json"
# #     }
# #     data = {
# #         "url": url,
# #         "mode": "scrape",
# #         "extract": {
# #             "text": True,
# #             "html": False
# #         }
# #     }

# #     response = requests.post(endpoint, headers=headers, json=data)
# #     response.raise_for_status()

# #     result = response.json()
# #     print(response.status_code)
# #     print(response.text)
# #     return result.get("text", "No text found.")
# from playwright.sync_api import sync_playwright

# def scrape_with_playwright(url):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         page.goto(url)

#         # Optionally wait for article or main content to load
#         page.wait_for_timeout(2000)

#         # Try scraping from article tag or full body as fallback
#         try:
#             content = page.locator("article").inner_text()
#         except:
#             content = page.content()

#         # Save screenshot
#         page.screenshot(path="screenshot.png")

#         browser.close()
#         return content
import requests
from bs4 import BeautifulSoup

def scrape_with_bs4(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find("div", {"class": "mw-parser-output"})
    if not article:
        return "Could not find article content."

    paragraphs = article.find_all("p")
    content = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())

    return content
