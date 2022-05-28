import imp
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .forms import CompForm
from .models import Comp

# Create your views here.
def complist(request):
    comps = Comp.objects.all()
    return render(request, 'almox/comp_list.html', {'comps': comps, 'case': 0})

def compview(request, id):
    comp = get_object_or_404(Comp, pk=id)
    return render(request, 'almox/comp.html', {'comp': comp})

def addcomp(request):
    if request.method == 'POST':
        form = CompForm(request.POST)

        if form.is_valid():
            comp = form.save(commit=False)
            comp.save()
            return redirect('/')
    
    else:
        form = CompForm()
        return render(request, 'almox/add.html', {'form': form})