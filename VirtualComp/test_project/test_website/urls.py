from django.views.generic.base import TemplateView
from django.urls import path,include
from . import views


urlpatterns =[
    path("", TemplateView.as_view(template_name="home.html"), name="home"), 
    #path("cats", TemplateView.as_view(template_name="cats.html"), name="cats"), 
    path("cats", views.cats, name="cats"), 

]