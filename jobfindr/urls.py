from django.urls import path
from . import views

urlpatterns = [
    # Client routes
    path("", views.nextjs_index, name="index"),
    path("login", views.nextjs_login, name="login"),
    path("register", views.nextjs_register, name="register"),
    path("register/congratulations", views.nextjs_congratulations, name="congratulations"),
    path("logout", views.api_logout, name="logout"),
    path("profile", views.nextjs_profile, name="profile"),
    # API routes
    path("api/hello", views.api_hello, name="api_hello"),
    path("api/register", views.api_register, name="api_register"),
    path("api/login", views.api_login, name="api_login"),
    path("api/logout", views.api_logout, name="api_logout"),
    path("api/user", views.api_user, name="api_user"),
]
