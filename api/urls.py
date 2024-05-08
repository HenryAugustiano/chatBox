from django.urls import path
from . import views
from . import ai

urlpatterns = [
    path('',views.hello_world),
    path('auth/github',views.github_auth),
    path('accounts/github/login/callback/', views.github_auth_callback),
    path('user', views.user),
    path('getResponse', ai.chat)
]