from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/712/
    path('<int:album_id>/', views.detail, name='detail'),

   # path('<int:album_id>', views.detail),



]