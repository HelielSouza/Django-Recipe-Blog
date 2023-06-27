from django.urls import path

from recipes.views import home  # imported by recipes

urlpatterns = [
    path('', home),  # function inside recipes app
]
