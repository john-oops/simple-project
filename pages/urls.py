from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'), # подключение страницы home
    path('about/', views.AboutPageView.as_view(), name='about'),  # подключение страницы about
]
