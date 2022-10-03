from django.urls import path
from . import views
from django.contrib import admin
app_name = 'homepage'
urlpatterns = [
    path('webtalk', views.initHome.as_view(), name="initHome"),
    path('webtalk/admin/', admin.site.urls),
    path('newpage', views.Newpage.as_view(), name="Newpage"),
    path('', views.tutorial_detail, name="tutorial_detail"),
    path('<slug:slug>', views.tutorial_detail, name="tutorial_detail"),
    path('<slug:slug>/', views.tutorial_detail, name="tutorial_detail"),
    path('accounts/profile', views.tutorial_detail, name="tutorial_detail"),

    #path('<int:year>/<int:month>/<int:day>/<slug:post>',
    #     views.tutorial_detail, name='tutorial_detail'),
    #path('tutorial_per_autore/<str:autore>',views.tutorial_to_author,name='tutorial_to_author'),
]
