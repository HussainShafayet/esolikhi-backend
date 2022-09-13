from django.urls import path
from . import views

urlpatterns = [
    path('esolikhi.login',views.handleLogin, name='esolikhi.login'),
    path('esolikhi.registration',views.handleRegistration, name='esolikhi.registration'),
]
