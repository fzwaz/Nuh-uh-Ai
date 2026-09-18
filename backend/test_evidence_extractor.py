from evidence_extractor import extract_page

url = "https://example.com"

text = extract_page(url)

print("Text length:", len(text))
print("Preview:", text[:500])