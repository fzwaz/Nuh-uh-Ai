import requests
from bs4 import BeautifulSoup


def extract_page(url: str) -> str:
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

        return soup.get_text(" ", strip=True)

    except requests.RequestException:
        return ""