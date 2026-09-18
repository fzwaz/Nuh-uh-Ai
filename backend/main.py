import os
from dotenv import load_dotenv
from google import genai
from fastapi import FastAPI
from pydantic import BaseModel
from claim_extractor import extract_claims
from search import search_claim
from evidence_extractor import extract_page
from evidence_classifier import classify_evidence

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found")

client = genai.Client(api_key=api_key)

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Nuh Uh AI backend is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    extracted = extract_claims(request.message)

    results = []

    for claim in extracted.claims:
        search_results = search_claim(claim)

        for result in search_results:
            page = extract_page(result["url"])

            result["evidence"] = {
                "text": page["text"]
            }

            classification = classify_evidence(
                claim,
                page["text"]
            )

            result["classification"] = {
                "label": classification.classification,
                "explanation": classification.explanation
            }
        results.append({
            "claim": claim,
            "search_results": search_results
        })

    return {"results": results}