import json
from pymatgen.core.structure import Structure

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from MaterialDB.settings import BASE_DIR


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
        f.close()
        to_json_file(file_obj.name)
        print('保存cif成功')
        return HttpResponse('OK')
    return render(request, 'website/upload.html')


# 读cif文件产生json文件
def to_json_file(file_obj_name):
    cif_name = BASE_DIR+"/static/cif/"+file_obj_name
    structure = Structure.from_file(cif_name)
    json_name = BASE_DIR+"/static/json/"+file_obj_name.split(".")[0]+".json"
    structure.to(filename=json_name)
    # var = Structure.from_file("../static/cif/test.cif")
    # print(var)
    # var.to(filename="../static/json/test.json")






