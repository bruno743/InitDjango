import imp
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Comp

# Create your views here.
class CompListView(ListView):
    model = Comp

class CompDetailView(DetailView):
    model = Comp