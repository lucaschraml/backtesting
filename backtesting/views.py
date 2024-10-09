from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from django.core import serializers
from django.apps import apps
# Create your views here.
from .models import Tradable
from .forms import StrategyForm, StyledFrom

def index(request):

    if request.method == 'POST':
        form =  StyledFrom(request.POST or None, request.FILES or None)
        if form.is_valid():
            #obj = form.save(commit=False)
            # obj.user = request.user
           # obj.save()
            print("Test")
            return redirect('/')
    template = loader.get_template("backtesting/index.html")
    form = StyledFrom
    context = {}
    context['form'] = form
    return HttpResponse(template.render(context,request))

def chart(request, tradable_id):
    tradable = get_object_or_404(Tradable, pk=tradable_id)
    template = loader.get_template("backtesting/charts.html")
    #TODO
    return HttpResponse(template.render({"tradable": tradable},request))

def coinflip(request):
    template = loader.get_template("backtesting/coinflip.html")
    return HttpResponse(template.render({},request))


def futures_trading(request):
    if request.method == 'POST':
        form = StyledFrom(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'success.html')
    else:
        form = StrategyForm()
    
    return render(request, 'backtesting/futures_form.html', {'form': form})