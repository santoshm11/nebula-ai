# reviews/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # When user visits root (''), call the index view
    path('', landing, name='landing'),
    path('review/', review_page, name='review_page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forgot-password/', forgot_password, name='forgot_password'),
]