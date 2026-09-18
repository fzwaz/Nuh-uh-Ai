import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient()


def search_claim(claim: str) -> list[dict]:
    response = client.search(
        query=claim,
        max_results=3
    )

    return [
    {
        "title": result["title"],
        "url": result["url"],
        "content": (result.get("content") or "")[:300],
        "score": result.get("score")
    }
    for result in response["results"]
]