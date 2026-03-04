from django.shortcuts import render, redirect, get_object_or_404
from .models import RecipeData, Like, SavedRecipe, Comment
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
import requests
import random
from django.http import JsonResponse


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("home")   # your homepage
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


def signin_view(request):
    if request.method == "POST":
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
    else:
        form = SignInForm()

    return render(request, "signin.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("signin")

@login_required(login_url="signin")
def home(request):
    if request.method == "POST":
        try:
            image = request.FILES.get('recipe_image')
            RecipeData.objects.create(
                user=request.user,
                recipe_name=request.POST.get('recipe_name', ''),
                recipe_description=request.POST.get('recipe_description', ''),
                rating=request.POST.get('rating', ''),
                image=image
            )
            messages.success(request, "Recipe added successfully.")
        except Exception as e:
            print("Upload Error:", e)  # will appear in Render logs
            messages.error(request, "Error uploading recipe. Please try again.")
        return redirect('home')

    return render(request, 'home.html')

def view(request):

    query = request.GET.get("q", "").strip()

    recipe_datas = RecipeData.objects.all()
    external_recipes = []

    # 🔎 If searching
    if query:

        # Filter original recipes
        recipe_datas = recipe_datas.filter(
            Q(recipe_name__icontains=query) |
            Q(recipe_description__icontains=query)
        )

        # Search external API
        try:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
            response = requests.get(url, timeout=5)
            data = response.json()
            external_recipes = data.get("meals", []) or []
        except:
            external_recipes = []

    else:
        # Load random external recipes only when not searching
        seen_ids = set()

        try:
            while len(external_recipes) < 6:
                r = requests.get(
                    "https://www.themealdb.com/api/json/v1/1/random.php",
                    timeout=5
                )
                meal = r.json().get("meals")

                if meal:
                    meal = meal[0]
                    if meal["idMeal"] not in seen_ids:
                        seen_ids.add(meal["idMeal"])
                        external_recipes.append(meal)
        except:
            external_recipes = []

    return render(request, "view.html", {
        "recipe_datas": recipe_datas,
        "external_recipes": external_recipes,
        "search_query": query
    })


def view_1(request, sid):
    data = get_object_or_404(RecipeData, recipe_id=sid)
    return render(request, 'view_1.html', {'data': data})

@login_required(login_url="signin")
def update(request,rec_id):
    if request.method=='POST':
        #objectname.proertyname = newname
        rec = get_object_or_404(
        RecipeData,
        recipe_id=rec_id,
        user=request.user  
        )
        rec.recipe_name = request.POST.get('recipe_name','')
        rec.recipe_description = request.POST.get('recipe_description','')
        rec.rating = request.POST.get('rating','')
        if request.FILES.get('image',''):
            rec.image = request.FILES.get('image','')
        rec.save()
        messages.success(request, "Recipe details updated.")
        return redirect(request.META.get('HTTP_REFERER', 'view'))
    data = RecipeData.objects.get(recipe_id=rec_id)
    return render(request,'update.html',{'data': data})

@login_required(login_url="signin")
def delete(request,rec_id):
    rec = get_object_or_404(
    RecipeData,
    recipe_id=rec_id,
    user=request.user  
    )
    rec.delete()
    messages.error(request, "Recipe deleted.")
    return redirect(request.META.get('HTTP_REFERER', 'view'))



def recipe_library(request):

    search_query = request.GET.get('q', '').strip()
    recipe_datas = RecipeData.objects.all()
    external_recipes = []
    if search_query:
        recipe_datas = recipe_datas.filter(
            Q(recipe_name__icontains=search_query) |
            Q(recipe_description__icontains=search_query)
        )
        try:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search_query}"
            response = requests.get(url, timeout=5)
            data = response.json()
            external_recipes = data.get("meals", []) or []
        except:
            external_recipes = []

    return render(request, "view.html", {
        "recipe_datas": recipe_datas,
        "external_recipes": external_recipes,
        "search_query": search_query
    })

@login_required(login_url="signin")
def like_recipe(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(RecipeData, recipe_id=recipe_id)
        Like.objects.get_or_create(
        user=request.user,
        recipe=recipe
        )
    return redirect(request.META.get('HTTP_REFERER', 'view'))

@login_required(login_url="signin")
def save_recipe(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(RecipeData, recipe_id=recipe_id)
        SavedRecipe.objects.get_or_create(
        user=request.user,
        recipe=recipe
        )
    return redirect(request.META.get('HTTP_REFERER', 'view'))


@login_required(login_url="signin")
def add_comment(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(RecipeData, recipe_id=recipe_id)
        text = request.POST.get("comment")

        if text:
            Comment.objects.create(
            user=request.user,
            recipe=recipe,
            text=text
            )

    return redirect(request.META.get('HTTP_REFERER', 'view'))

@login_required(login_url="signin")
def saved_recipes(request):
    saved_items = SavedRecipe.objects.filter(
        user=request.user
    ).select_related('recipe').order_by('-id')

    return render(request, 'saved_recipes.html', {
        'saved_items': saved_items
    })


def remove_saved(request, saved_id):
    if request.method == "POST":
        item = get_object_or_404(SavedRecipe, id=saved_id)
        item.delete()
    return redirect('saved_recipes')



def load_more_api_recipes(request):

    external_recipes = []
    seen_ids = set()

    try:
        while len(external_recipes) < 10:   # load 10 each click

            r = requests.get(
                "https://www.themealdb.com/api/json/v1/1/random.php",
                timeout=5
            )

            meal = r.json().get("meals")

            if meal:
                meal = meal[0]

                if meal["idMeal"] not in seen_ids:
                    seen_ids.add(meal["idMeal"])

                    external_recipes.append({
                        "id": meal["idMeal"],
                        "name": meal["strMeal"],
                        "image": meal["strMealThumb"],
                        "source": meal["strSource"],
                        "desc": meal["strInstructions"][:120]
                    })

    except:
        pass

    return JsonResponse({"recipes": external_recipes})