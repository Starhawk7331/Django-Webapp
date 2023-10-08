from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader


def home(request):
    Username = request.post.get('username', None)
    Password = request.post.get('password', None)
    user = authenticate(Username,Password)
    if user is not None:
        template = loader.get_template("home.html")
        return HttpResponse(template.render())
    else:
        login(request)
    

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())