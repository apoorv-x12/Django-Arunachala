from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome),
    path('topics/',views.topics),
]
