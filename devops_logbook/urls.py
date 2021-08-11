from django.urls import path
from .views import main, user_login


urlpatterns = [
    path('', main, name='list'),
    path('login', user_login, name='login')
]