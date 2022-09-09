
from django.urls import path
from . import views
urlpatterns = [
    path('createorgetpost',views.posts, name='createorgetpost'),
]
