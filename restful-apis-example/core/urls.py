from django.urls import path

from . import views

urlpatterns = [
    path('', views.github, name='github'),
    path('status/', views.api_tipos, name='api_tipos'),
]
