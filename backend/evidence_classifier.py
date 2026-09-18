from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from typing import Literal


load_dotenv()

client = genai.Client()


class EvidenceClassification(BaseModel):
    classification: Literal[
        "SUPPORTS",
        "CONTRADICTS",
        "IRRELEVANT"
    ]
    explanation: str


def classify_evidence(claim: str, evidence: str) -> EvidenceClassification:
    prompt = f"""
    Determine the relationship between the claim and the evidence.

    Classification rules:
    - SUPPORTS: The evidence provides information that supports the claim.
    - CONTRADICTS: The evidence provides information that contradicts the claim.
    - IRRELEVANT: The evidence does not provide meaningful information
      about whether the claim is true or false.

    Claim:
    {claim}

    Evidence:
    {evidence}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": EvidenceClassification,
        },
    )

    if response.parsed is None:
        raise ValueError("Gemini did not return valid evidence classification")

    return response.parsed