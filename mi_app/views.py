from django.shortcuts import render

# Create your views here.

def lista_empleados(request):
    empleados = ['Carlos Pérez','María Gómez','luis Soto','Ana Torres']
    return render(request,'empleados/lista_empleados.html', {'empleados':empleados})