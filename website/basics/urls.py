from django.urls import path
from . import views, interest_view

urlpatterns = [
    path('welcome/',views.welcome),
    path('topics/',views.topics),
    path('lp/',views.send_topic),
    #note first argument's name is up to you it need not be send_topic as in above line  !!!!!
    path('wish/',views.wish),
    path('interest/',interest_view.interest),
    path('interest_p/',interest_view.interest_post)
]
