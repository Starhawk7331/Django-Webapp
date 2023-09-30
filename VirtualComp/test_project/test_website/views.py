from django.http import HttpResponse
from django.template import loader
from .models import Family_members

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


    # if request.method == 'GET':
    #     username = request.GET.get('username', None)
    #     password = request.GET.get('password', None)
        
    #     if username in Family_members.objects.all() and password in Family_members.objects.all():
    #         template = loader.get_template("home.html")
    #         return HttpResponse(template.render())
        
    #     else:
    #         return HttpResponse("debug1")
    #         #template = loader.get_template("login.html")
    #         #return HttpResponse(template.render()) 
    # else:
    #     return HttpResponse("debug2")
    #     #template = loader.get_template("login.html")
    #     #return HttpResponse(template.render())
    
    

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())