from claim_extractor import extract_claims

result = extract_claims(
    "The Earth is flat, and humans only use 10% of their brains."
)

print(result)
print(result.claims)