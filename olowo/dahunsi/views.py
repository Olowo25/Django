from django.shortcuts import render
from django.urls import reverse
from .form2 import Albumss
from .models import Album
from .form2 import Songss
from .models import Song
from .functions import upload
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def song(request):
    if request.method == 'POST':
        songs = Songss(request.POST, request.FILES)
        if songs.is_valid():
            upload(request.FILES['song'])
            return HttpResponse("File uploaded successfully")
    else:
        songs = Songss()
    return render(request, "song.html", {'form1': songs})


def album(request):
    if request.method == 'POST':
        albums = Albumss(request.POST, request.FILES)
        if albums.is_valid():
            upload(request.FILES['album_logo'])
            return HttpResponse("File uploaded successfuly <a href='/dahunsi/song'>Click to see songs</a>")
    else:
        albums = Albumss()
    return render(request, "album.html", {'form2': albums})


def viewalbumlist(request):
    myalbum = Album.objects.all().values()
    template = loader.get_template('viewalbum.html')
    context = {
        'album': myalbum
    }
    return HttpResponse(template.render(context, request))


def viewsong(request):
    mysong = Song.objects.all().values()
    template = loader.get_template('viewsong.html')
    context = {
        'songs': mysong
    }
    return HttpResponse(template.render(context, request))


def addalbum(request):
    # if request.method == 'POST':
    #     albums = Albumss(request.POST, request.FILES)
    #     if albums.is_valid():
    #         upload(request.FILES['album_logo'])
    #
    # else:
    #     albums = Albumss()
    template = loader.get_template('addalbum.html')
    return HttpResponse(template.render({}, request))


def addsong(request):
    template = loader.get_template('addsong.html')
    return HttpResponse(template.render({}, request))


def addingsong(request):
    id = request.POST['id']
    artist = request.POST['artist']
    song_title = request.POST['song_title']
    genre = request.POST['genre']
    song = request.POST['song']
    songs = Song(artist=artist, song_title=song_title, genre=genre, song=song, album_id=id)
    songs.save()
    return HttpResponseRedirect(reverse('viewsong'))


def addingalbum(request):
    artist = request.POST['artist']
    album_title = request.POST['album_title']
    genre = request.POST['genre']
    album_logo = request.POST['album_logo']
    alb = Album(artist=artist, album_title=album_title, genre=genre, album_logo=album_logo)
    alb.save()
    return HttpResponseRedirect(reverse('viewalbum'))


def deletealbum(request, id):
    alb = Album.objects.get(id=id)
    template = loader.get_template('review.html')
    context = {
        'albums': alb
    }
    return HttpResponse(template.render(context, request))


def updatealbum(request, id):
    alb = Album.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'albums': alb
    }
    return HttpResponse(template.render(context, request))


def deletingalbum(request, id):
    alb = Album.objects.get(id=id)
    alb.delete()
    return HttpResponseRedirect(reverse('viewalbum'))


def updatingalbum(request, id):
    artist = request.POST['artist']
    album_title = request.POST['album_title']
    genre = request.POST['genre']
    album_logo = request.POST['album_logo']
    alb = Album.objects.get(id=id)
    alb.artist = artist
    alb.album_title = album_title
    alb.genre = genre
    alb.album_logo = album_logo
    alb.save()
    return HttpResponseRedirect(reverse('viewalbum'))


def updatesong(request, id):
    songz = Song.objects.get(id=id)
    context = {
        "songz": songz
    }
    template = loader.get_template('SongUpdate.html')
    return HttpResponse(template.render(context, request))

def updatingsong(request, id):
    artist = request.POST['artist']
    song_title = request.POST['song_title']
    genre = request.POST['genre']
    song = request.POST['song']
    alb = Song.objects.get(id=id)
    alb.artist = artist
    alb.song_title = song_title
    alb.genre = genre
    alb.song = song
    alb.save()
    return HttpResponseRedirect(reverse('viewsong'))