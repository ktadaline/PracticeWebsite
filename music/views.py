
from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path
from . import views
from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
#from django.template import loader
from .models import Album, Song

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
    album = get_object_or_404(Album, pk=album_id)
    #try:
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})

   #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

# urlpatterns = [
#    path('', views.index, name = 'index'),
#
# ]


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
