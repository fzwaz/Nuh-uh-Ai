import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("Tavily API key not found")

client = TavilyClient(api_key=api_key)

response = client.search(
    query="What is the Earth's shape?",
    max_results=3
)

for result in response["results"]:
    print(result["title"])
    print(result["url"])
    print(result["content"])
    print()