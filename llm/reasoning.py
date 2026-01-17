import os
import json
import re
from groq import Groq

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("Please set the GROQ_API_KEY environment variable!")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

REQUIRED_KEYS = {
    "image_quality_score",
    "issues_detected",
    "detected_objects",
    "text_detected",
    "llm_reasoning_summary",
    "final_verdict",
    "confidence"
}


def extract_json_safely(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

    if not REQUIRED_KEYS.issubset(data.keys()):
        return None
    return data


def reason(features: dict):
    prompt = f"""
You are a strict JSON generator.

Rules:
- Output ONLY valid JSON
- No markdown
- No explanations
- No extra keys

Required format:
{{
  "image_quality_score": number between 0 and 1,
  "issues_detected": list of strings,
  "detected_objects": list of strings,
  "text_detected": list of strings,
  "llm_reasoning_summary": string,
  "final_verdict": string,
  "confidence": number between 0 and 1
}}

Input image signals:
{json.dumps(features, indent=2)}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  
        messages=[
            {"role": "system", "content": "You output only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=400
    )

    raw_output = response.choices[0].message.content

    parsed = extract_json_safely(raw_output)
    if parsed is None:
        print("RAW MODEL OUTPUT:\n", raw_output)
        raise ValueError("Model did not return valid JSON")

    return parsed
