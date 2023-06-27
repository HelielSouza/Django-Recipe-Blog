
from django.urls import path

from recipes.views import contato, home, sobre  # imported by recipes

urlpatterns = [
    path('', home),  # function inside recipes app
    path('contato/', contato),
    path('sobre/', sobre)
]
