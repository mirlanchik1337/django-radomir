from django.urls import path
from . import views


urlpatterns = [
    path('', views.tv_shows_list, name='tv_shows_list'),
    path('tv_shows_list/<int:id>/', views.tv_show_detail, name='tv_show_detail'),
    path('tv_shows_list/<int:id>/delete', views.tv_show_delete_view, name='delete_tvshow'),
    path('tv_shows_list/<int:id>/update', views.tv_show_edit_view, name='update_tvshow'),
    path('tv_shows_list/<int:id>/add_review', views.add_review_view, name='add_review'),
    path('create_tvshow/', views.tv_show_create_view, name='create_tvshow'),



]