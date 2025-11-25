from django.shortcuts import render

def landing(request):
    return render(request, 'reviews/landing.html')

def review_page(request):
    return render(request, 'reviews/review.html')

def login(request):
    return render(request, 'reviews/login.html')

def register(request):
    return render(request, 'reviews/register.html')

def forgot_password(request):
    return render(request, 'reviews/forgot-password.html')