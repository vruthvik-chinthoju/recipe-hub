from django.urls import path
from ai_recipe import views


urlpatterns = [
    path("ai-recipe/", views.recipe_agent_view, name="ai_recipe"),

]
