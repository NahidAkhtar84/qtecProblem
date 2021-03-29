
from django.contrib import admin
from django.urls import path, include
from .views import Index
from users.views import Login, SignUp, logout
from historydetails.views import historyDetails
from middleware.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login', Login.as_view(), name="login"),
    path('signup', SignUp.as_view(), name="signup"),
    path('search', auth_middleware(Index.as_view()), name="search"),
    path('logout', logout , name="logout"),
    path('allhistory', historyDetails.as_view() , name="allhistory"),
]