from django.shortcuts import render, get_object_or_404
from . import models


def tv_shows_list(request):
    if request.method == 'GET':
        tvshows = models.TVShow.objects.all()
        return render(request, 'tv_shows/tv_shows_list.html',
                      {'tvshows':tvshows})


def tv_shows_detail(request, id):
    if request.method == 'GET':
        tvshow_id = get_object_or_404(models.TVShow, id=id)
        return render(request, 'tv_shows/tv_shows_detail.html',
                      {'tvshow_id':tvshow_id})
