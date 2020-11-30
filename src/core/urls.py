from django.urls import path

from .views import (
    HomeView,
    PostView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostView.as_view(), name='my_posts'),
]
