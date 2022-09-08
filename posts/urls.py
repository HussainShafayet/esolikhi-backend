
from django.urls import path, include
from . import views
urlpatterns = [
    path('createorgetpost',views.posts, name='createorgetpost'),
]
