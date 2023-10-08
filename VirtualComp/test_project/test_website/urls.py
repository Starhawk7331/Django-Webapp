from django.views.generic.base import TemplateView
from django.urls import path,include
from . import views


urlpatterns =[
    path("", TemplateView.as_view(template_name="home.html"), name="home"), 
    path("cat-pics", TemplateView.as_view(template_name="cat-pics.html"), name="cat-pics"), 

]