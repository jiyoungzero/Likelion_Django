from django.urls import path
from .views import *
from . import views

app_name = "users"
urlpatterns = [
    path('<int:id>/mypage/', mypage, name="mypage"),
    path('<int:id>/follow/', views.follow, name="follow"),
]