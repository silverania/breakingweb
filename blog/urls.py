from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('sendpost', views.newPost, name="newPost"),
    path('showposts', views.getPost, name="getPost"),
]
