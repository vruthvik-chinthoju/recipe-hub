from django.db import models
from django.contrib.auth.models import User
import uuid


class RecipeData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    recipe_name = models.CharField(max_length=150)
    recipe_description = models.TextField()
    rating = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.recipe_name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeData, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "recipe")



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeData, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SavedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeData, on_delete=models.CASCADE, related_name="saved")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "recipe")