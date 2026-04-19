from google import genai

client = genai.Client(api_key="AIzaSyCnVYZFHrtM96fqsaHYlNZnmWR7klcr80U")

def get_llm_response(prompt):
    try:
        print("👉 CLIENT TYPE:", type(client))
        print("👉 AVAILABLE MODELS:")
        
        models = client.models.list()
        for m in models:
            print(m.name)

        response = client.models.generate_content(
            model="models/gemini-2.0-flash-lite",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print("LLM ERROR:", e)
        return "⚠️ Rate limit reached. Please try again in a few seconds."