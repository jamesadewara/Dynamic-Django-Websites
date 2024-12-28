from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import ProductForm, CustomUserCreationForm, SignUpForm, LoginForm
from .models import Product, Banner

class HomePageView(ListView):
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)
        
        # Add the banners to the context
        context['banners'] = Banner.objects.all()  
        
        return context


# Logout View (using Django's built-in LogoutView)
class UserLogoutView(LogoutView):
    next_page = '/'


# Alternative Function-Based Views for SignUp and Login

# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('home')  # Redirect to the home page or any other page
    else:
        form = SignUpForm()

    return render(request, 'core/auth/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or dashboard
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'core/auth/login.html', {'form': form})
