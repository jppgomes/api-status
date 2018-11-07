from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('status/', views.api_tipos, name='api_tipos'),
]
