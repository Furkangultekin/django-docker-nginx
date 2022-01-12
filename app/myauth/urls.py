from django.urls import path, include
from .views import RegisterView, LoginView,UserView,LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()), #regiter url; /register
    path('login', LoginView.as_view()), # login url; /login
    path('user', UserView.as_view()), #user url; /user
    path('logout', LogoutView.as_view()), #logout url; /logout
]