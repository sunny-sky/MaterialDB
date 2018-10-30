from django.urls import path

from . import views

urlpatterns = [
    # ex: /website/
    path('', views.index, name='index'),
]
