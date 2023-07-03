from django.urls import path

from . import views  # imported by recipes

urlpatterns = [
    path('', views.home),  # function inside recipes app to show home page
    path('recipes/<id>/', views.recipe)  # to show one recipe
]
