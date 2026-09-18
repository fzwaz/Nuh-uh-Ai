from claim_extractor import extract_claims
from search import search_claim

message = "The Earth is flat, and humans only use 10% of their brains."

extracted = extract_claims(message)

for claim in extracted.claims:
    print(f"\nClaim: {claim}")

    results = search_claim(claim)

    for result in results:
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Snippet:", result["content"])