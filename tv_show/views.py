from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def tv_shows_list(request):
    if request.method == 'GET':
        tvshows = models.TVShow.objects.all()
        return render(request, 'tv_shows/tv_shows_list.html',
                      {'tvshows':tvshows})


def tv_show_detail(request, id):
    if request.method == 'GET':
        tvshow_id = get_object_or_404(models.TVShow, id=id)
        return render(request, 'tv_shows/tv_show_detail.html',
                      {'tvshow_id': tvshow_id})


# Add
def tv_show_create_view(request):
    if request.method == 'POST':
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully added <a href="/">Main page</a> ')
    else:
        form = forms.TVShowForm()
    return render(request, 'tv_shows/crud/create_tvshow.html',
                  {'form': form})


def tv_show_delete_view(request, id):
    tvshow_id = get_object_or_404(models.TVShow, id=id)
    tvshow_id.delete()
    return HttpResponse('Successfully deleted <a href="/">Main page</a>')


def tv_show_edit_view(request, id):
    tvshow_id = get_object_or_404(models.TVShow, id=id)
    if request.method == 'POST':
        form = forms.TVShowForm(instance=tvshow_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully changed <a href="/">Main page</a>')
    else:
        form = forms.TVShowForm(instance=tvshow_id)
        return render(request, 'tv_shows/crud/edit_tvshow.html',
                  {'form': form, 'tvshow_id': tvshow_id})

