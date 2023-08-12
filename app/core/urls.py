"""
Mapping for core app.
"""
from django.urls import path

from core.views import *

urlpatterns = [
    path('',StudentListAPI.as_view()),
    path('<int:pk>/',StudentDetailAPI.as_view()),

    path('login/',CreateToken.as_view()),
]