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

def upload(request):
    return render(request,"upload.html")

class FileFieldFormView(FormView):
    form_class = ImageFieldForm
    template_name = "upload.html"  # Replace with your template.
    success_url = "..."  # Replace with your URL or reverse().

    def post(self, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["image_field"]
        for f in files:
            print("test")  # Do something with each file.
        return super().form_valid()