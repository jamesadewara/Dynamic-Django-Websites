from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'original_price', 'current_price', 'sale', 'stock_quantity', 'category', 'is_active']

    # Optional: You can add custom widgets for styling the form fields
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        'original_price': forms.NumberInput(attrs={'class': 'form-control'}),
        'current_price': forms.NumberInput(attrs={'class': 'form-control'}),
        'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'sale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

# User Registration Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User Sign Up Form
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
