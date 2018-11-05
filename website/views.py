from django.shortcuts import render
import json
from MaterialDB.settings import BASE_DIR
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View


def index(request):
    return render(request, 'website/index.html')


def search_page(request):
    return render(request, 'website/searchPage.html')


def crystal(request):
    with open("static/json/jmol.json", 'r') as load_f:
        load_dict = json.load(load_f)
    return render(request, 'website/CrystalStructure.html', {'data': load_dict})


def electron(request):

    return render(request, 'website/ElectronicStructure.html')


def upload(request):
    return render(request, 'website/upload.html')


def upload_cif(request):
    print('进入文件保存方法')
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        import os
        f = open(os.path.join(BASE_DIR, 'static', 'cif', file_obj.name), 'wb')
        print(file_obj, type(file_obj))
        for chunk in file_obj.chunks():
            f.write(chunk)
            # print(json.load(chunk))
        f.close()
        print('保存cif成功')
        return HttpResponse('OK')
    return render(request, 'website/upload.html')





