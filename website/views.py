from django.shortcuts import render
from django.template import loader
import pymatgen as mg
import json
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'website/index.html')


def search_page(request):
    return render(request, 'website/searchPage.html')


def crystal(request):
    with open("static/json/jmol.json", 'r') as load_f:
        load_dict = json.load(load_f)
    return render(request, 'website/CrystalStructure.html', {'data':load_dict})


