from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_world),
    path('auth/github',views.github_auth),
    path('accounts/github/login/callback/', views.github_auth_callback),
    path('user', views.user),
]