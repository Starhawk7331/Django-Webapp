from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import loader
from .models import Family_members

@csrf_protect
def home(request):

    if request.method == 'post':

        Username = request.post.get('username', None)
        Password = request.post.get('password', None)

        user = Family_members.objects.get(username=Username)

        if user.password == Password:
            
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