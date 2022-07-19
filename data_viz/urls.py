from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('login/data_fetch/', views.data_fetch),
    path('login/', views.login_page)
]
