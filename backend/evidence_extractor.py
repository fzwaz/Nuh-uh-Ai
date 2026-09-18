import requests
from bs4 import BeautifulSoup


def extract_page(url: str) -> dict:
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for element in soup(["script", "style", "nav", "header", "footer"]):
            element.decompose()

        title = soup.title.get_text(strip=True) if soup.title else ""

        text = soup.get_text(" ", strip=True)[:10000]

        return {
            "title": title,
            "url": url,
            "text": text
        }

    except requests.RequestException:
        return {
            "title": "",
            "url": url,
            "text": ""
        }