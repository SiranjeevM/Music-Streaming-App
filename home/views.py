# imported our models
from django.core.paginator import Paginator
from . models import Song
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.shortcuts import render, redirect


def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)
def index1(request):
    template=loader.get_template("list.html")
    return HttpResponse(template.render())