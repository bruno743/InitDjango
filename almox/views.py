import imp
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from .forms import CompForm
from .models import Comp

# Create your views here.
def complist(request):
    search = request.GET.get('search')

    if search:
        comps_list = Comp.objects.filter(comp_name__icontains=search)
        paginator = Paginator(comps_list, 5)
        page = request.GET.get('page')
        comps = paginator.get_page(page)
    else:
        comps_list = Comp.objects.all()
        paginator = Paginator(comps_list, 5)

        page =  request.GET.get('page')

        comps = paginator.get_page(page)

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

def editcomp(request, id):
    comp = get_object_or_404(Comp, pk=id)
    form = CompForm(instance=comp)

    if(request.method == 'POST'):
        form = CompForm(request.POST, instance=comp)

        if(form.is_valid()):
            comp.save()
            return redirect('/')
        else:
            return render(request, 'almox/editcomp.html', {'form': form, 'comp': comp})
    else:
        return render(request, 'almox/editcomp.html', {'form': form})

def deletecomp(request, id):
    comp = get_object_or_404(Comp, pk=id)

    comp.delete()
    return redirect('/')
