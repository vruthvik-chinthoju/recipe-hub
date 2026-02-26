from groq import Groq
import os

def ai_recipe_agent(ingredients: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are a professional chef AI.

Return ONLY valid JSON.
Never wrap JSON in markdown.
Do NOT include explanations or extra text.

Write 5–7 clear, detailed cooking steps.
Each step should be informative but concise.
Avoid unnecessary long storytelling.

JSON format:
{{
  "name": "Recipe name",
  "ingredients": ["item1", "item2"],
  "steps": ["step 1 detailed...", "step 2 detailed..."]
}}

Ingredients available:
{ingredients}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=900,
        response_format={"type": "json_object"}
    )

    # ✅ THIS WAS MISSING
    return response.choices[0].message.content.strip()