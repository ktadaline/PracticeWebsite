
from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path
from . import views
from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from .models import Album

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

    #return HttpResponse(template.render(context, request))

    #html = ''
    #for album in all_albums:
    #    url = '/music/' + str(album.id)
    #   html += '<a href = "' + url + '">'+ album.album_title +'</a><br>'
    #return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

# urlpatterns = [
#    path('', views.index, name = 'index'),
#
# ]
