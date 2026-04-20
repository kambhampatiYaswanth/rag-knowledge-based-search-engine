import os

from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_llm_response(prompt):
    try:
        response = client.models.generate_content(
            model="models/gemini-2.0-flash-lite",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print("LLM ERROR:", e)
        return "⚠️ Rate limit reached. Please try again in a few seconds."