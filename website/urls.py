from django.urls import path
from django.conf.urls import url
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
    # 接收上传文件
    path('upload_cif', views.upload_cif, name='upload_cif'),
    # 相关文献页面 ex：/website/paper
    path('paper', views.paper, name='paper')
]
