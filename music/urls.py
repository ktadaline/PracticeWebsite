from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/<album_id>/
    path('<int:album_id>/', views.detail, name='detail'),

   # path('<int:album_id>', views.detail),

    # /music/<album_id>/favorite/
   #path('<int:album_id>/favorite/', name='favorite'),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),


]