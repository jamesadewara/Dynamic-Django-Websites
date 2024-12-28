from django.urls import path
from .views import HomePageView, signup, login_view, UserLogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
