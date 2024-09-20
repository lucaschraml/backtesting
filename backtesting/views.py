from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.core import serializers
from django.apps import apps
# Create your views here.
from .models import Tradable

def index(request):
    template = loader.get_template("backtesting/index.html")
    return HttpResponse(template.render({},request))

def chart(request, tradable_id):
    tradable = get_object_or_404(Tradable, pk=tradable_id)
    template = loader.get_template("backtesting/charts.html")
    #TODO
    return HttpResponse(template.render({"tradable": tradable},request))

def coinflip(request):
    template = loader.get_template("backtesting/coinflip.html")
    return HttpResponse(template.render({},request))