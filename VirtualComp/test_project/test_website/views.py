from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import cat_pic
from django.views.generic.edit import FormView
from .forms import ImageFieldForm

def cats(request):
    data = cat_pic.objects.all()
    context = {
        'data' : data
    }
    return render(request,"cats.html", context)
