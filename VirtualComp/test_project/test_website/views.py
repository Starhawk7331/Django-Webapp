from django.http import HttpResponse
from django.template import loader
from .models import Family_members

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

    if request.method == 'post':

        username = request.post.get('username', None)
        password = request.post.get('password', None)

        if username in Family_members.objects.username():
            user = Family_members.objects.filter(username).values()
            
            if user.password == password:
                template = loader.get_template("home.html")
                return HttpResponse(template.render())
        else:
            template = loader.get_template("login.html")
            return HttpResponse(template.render()) 
    else: 
        template = loader.get_template("login.html")
        return HttpResponse(template.render())
    
    

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())