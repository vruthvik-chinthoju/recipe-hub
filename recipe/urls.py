from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_recipe/', views.view, name='view'),
    path('view_1/<str:sid>/', views.view_1, name='view_1'),
    path('update/<str:rec_id>/', views.update, name='update'),
    path('delete/<str:rec_id>/', views.delete, name='delete'),
    path('search/', views.recipe_library, name='search'),
    path("signup/", views.signup_view, name="signup"),
    path("signin/", views.signin_view, name="signin"),
    path("logout/", views.logout_view, name="logout"),
    path('like/<uuid:recipe_id>/', views.like_recipe, name='like_recipe'),
    path('save/<uuid:recipe_id>/', views.save_recipe, name='save_recipe'),
    path('comment/<uuid:recipe_id>/', views.add_comment, name='add_comment'),
    path('saved/', views.saved_recipes, name='saved_recipes'),
    path('remove-saved/<int:saved_id>/', views.remove_saved, name='remove_saved'),
    path("load-more-api/", views.load_more_api_recipes, name="load_more_api"),
]