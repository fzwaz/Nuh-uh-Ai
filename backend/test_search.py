from search import search_claim

results = search_claim("The Earth is flat.")

for result in results:
    print(result["title"])
    print(result["url"])
    print(result["content"])
    print()