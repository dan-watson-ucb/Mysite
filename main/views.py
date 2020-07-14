from django.shortcuts import render # renders templates
from django.http import HttpResponse
from .models import Article, Players
# Create your views here.

def homepage(request):
    #return HttpResponse('Works')
    return render(request = request,
                  #template being filled
                  template_name = "main/home.html",
                  #context is the information passed to template
                  context = {"articles": Article.objects.all,
                             "players": Players.objects.using('nba').all})