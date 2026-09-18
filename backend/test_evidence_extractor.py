from evidence_extractor import extract_page

url = "https://science.nasa.gov/earth/facts/"

evidence = extract_page(url)

print("Title:", evidence["title"])
print("URL:", evidence["url"])
print("Text length:", len(evidence["text"]))
print("Preview:", evidence["text"][:500])