from django.urls import path

from . import views

urlpatterns = [
    # ex: /website/
    path('', views.index, name='index'),
    # ex: /website/search
    path('searchPage', views.search_page, name='searchPage'),
    # ex: /website/crystal
    path('crystal', views.crystal, name='crystal'),
    # ex: /website/electron
    path('electron', views.electron, name='electron'),
    # ex: /website/upload
    path('upload', views.upload, name='upload'),
]
