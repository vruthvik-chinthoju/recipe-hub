from django.shortcuts import render
from .agent import ai_recipe_agent
import json
import re   # 👈 NEW

def recipe_agent_view(request):
    if "chat_history" not in request.session:
        request.session["chat_history"] = []

    error = None

    if request.method == "POST":
        user_ingredients = request.POST.get("ingredients")

        if user_ingredients:
            raw_response = None
            try:
                raw_response = ai_recipe_agent(user_ingredients)

                # ✅ CLEAN GROQ OUTPUT (remove ```json ``` if present)
                clean_response = re.sub(r"```json|```", "", raw_response).strip()

                recipe = json.loads(clean_response)

                # OPTIONAL: save history (recommended)
                request.session["chat_history"].append({
                            "recipe": recipe
                })
                request.session.modified = True

            except Exception as e:
                print("AI ERROR 👉", e)
                print("RAW RESPONSE 👉", raw_response)
                error = str(e)

    return render(
        request,
        "ai_recipe/recipe_agent.html",
        {
            "history": request.session.get("chat_history", []),
            "error": error
        }
    )


def ai_recipe(request):
    prefill = request.GET.get("q", "")
    return render(request, "ai_recipe/recipe_agent.html", {
        "prefill": prefill
    })