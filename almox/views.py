import imp
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from .forms import CompForm, LocForm, ModForm
from .models import Comp, Mod, Loc

# Create your views here.
def complist(request):
    search = request.GET.get('search')
    searchEst = request.GET.get('search-est')
    searchStat = request.GET.get('search-stat')
    searchMod = request.GET.get('search-mod')
    searchLoc = request.GET.get('search-loc')

    flag = False
    if not searchEst: searchEst = ''
    else: flag = True
    if not searchStat: searchStat = ''
    else: flag = True
    if not searchLoc: searchLoc = ''
    else: flag = True

    comps_list = Comp.objects.all()
    
    if search:
        comps_list = Comp.objects.filter(comp_name__icontains=search)
    elif flag:
        loc = Loc.objects.filter(loc_name__icontains=searchLoc)
        loc = loc[0]
        comps_list = Comp.objects.filter(comp_estado__icontains=searchEst)
        comps_list = comps_list.filter(comp_status__icontains=searchStat)
        if loc:
            comps_list = comps_list.filter(comp_loc=loc.id)

    paginator = Paginator(comps_list, 5)
    page =  request.GET.get('page')
    comps = paginator.get_page(page)

    return render(request, 'almox/comp_list.html', {'comps': comps})

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

def addmod(request):
    if request.method == 'POST':
        form = ModForm(request.POST)

        if form.is_valid():
            mod = form.save(commit=False)
            mod.save()
            return redirect('/addcomp/')
    
    else:
        form = ModForm()
        return render(request, 'almox/addmod.html', {'form': form})

def addloc(request):
    if request.method == 'POST':
        form = LocForm(request.POST)

        if form.is_valid():
            mod = form.save(commit=False)
            mod.save()
            return redirect('/')
    
    else:
        form = LocForm()
        return render(request, 'almox/addloc.html', {'form': form})
