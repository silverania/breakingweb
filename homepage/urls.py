from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.tutorial_detail, name="tutorial_detail"),
    path('<slug:slug>', views.tutorial_detail, name="tutorial_detail"),

    #path('<int:year>/<int:month>/<int:day>/<slug:post>',
    #     views.tutorial_detail, name='tutorial_detail'),
    #path('tutorial_per_autore/<str:autore>',views.tutorial_to_author,name='tutorial_to_author'),
]
