from django.urls import path

from . import views  # imported by recipes

app_name = 'recipes'

urlpatterns = [
    # function inside recipes app to show home page
    path('', views.home, name="home"),
    # to show one recipe
    path('recipes/<int:id>/', views.recipe, name="recipe")

]
