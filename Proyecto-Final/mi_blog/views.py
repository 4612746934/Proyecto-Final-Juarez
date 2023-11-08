from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Familiares, Amigos, Viajes
from .forms import FamiliaresForm, AmigosForm, ViajesForm,BusquedaForm

def lista_familiares(request):
    familiares = Familiares.objects.all()
    return render(request, 'mi_blog/lista_familiares.html', {'familiares': familiares})


def lista_amigos(request):
    amigos = Amigos.objects.all()
    return render(request, 'mi_blog/lista_amigos.html', {'amigos': amigos})

def lista_viajes(request):
    viajes = Viajes.objects.all()
    return render(request, 'mi_blog/lista_viajes.html', {'viajes': viajes})

def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliaresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_blog:crear_familiar')
    else:
        form = FamiliaresForm()
    return render(request, 'mi_blog/crear_familiar.html', {'form': form})

def crear_amigo(request):
    if request.method == 'POST':
        form = AmigosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_blog:lista_amigos')
    else:
        form = AmigosForm()
    return render(request, 'mi_blog/crear_amigo.html', {'form': form})

def crear_viaje(request):
    if request.method == 'POST':
        form = ViajesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_blog:lista_viajes')
    else:
        form = ViajesForm()
    return render(request, 'mi_blog/crear_viaje.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        # Realiza una búsqueda en la base de datos
        term = request.POST.get('termino_busqueda')
        resultados_familiares = Familiares.objects.filter(nombre__icontains=term)
        resultados_amigos = Amigos.objects.filter(nombre__icontains=term)
        resultados_viajes = Viajes.objects.filter(destino__icontains=term)
        return render(request, 'mi_blog/resultados_busqueda.html', {
            'resultados_familiares': resultados_familiares,
            'resultados_amigos': resultados_amigos,
            'resultados_viajes': resultados_viajes
        })
    else:
        form = BusquedaForm()
        return render(request,'mi_blog/buscar.html',{'form':form})
    
