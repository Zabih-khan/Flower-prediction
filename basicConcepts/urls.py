from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome, name = 'Welcome'),
    path('user', views.user, name='User')
]