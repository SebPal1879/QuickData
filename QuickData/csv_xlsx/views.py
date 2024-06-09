from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse

from django.core.files.storage import FileSystemStorage

import time
import pandas as pd
from .conversor import archivo_a_xlsx

from .forms import archivo_formulario
from .models import archivo

import os

# Create your views here.
def csv_xlsx(request):
    if request.method == 'POST':
        form = archivo_formulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            nombre = request.POST.get('nombre','')
            print(f" nombre {nombre}")
            obj = archivo.objects.latest('id')
            obj.save()
            print("Si se subió")
            ruta = f'\\archivos_csv\\{nombre}.csv'
            print(ruta)
            time.sleep(3)
            archivo_a_xlsx(nombre)
            return redirect('archivo_ver')
        else:
            print("No se subió")
            print(form.errors)
            
    else: 
        form = archivo_formulario()
        
        
    return render(request,'csv_xlsx.html',{'form':form})

def archivo_ver(request):
    obj = archivo.objects.latest('id')
    print(f"obj {obj.nombre}")
    return render (request, 'descarga_xlsx.html',{'obj':obj})

def descargar_xlsx(request,nombre):
    archivoD = archivo.objects.get(nombre=nombre)
    ruta_actual = os.path.dirname(__file__)
    ruta_archivo_xlsx = os.path.join(ruta_actual,'archivos_xlsx\\', nombre+".xlsx")
    print(ruta_archivo_xlsx)
    response = FileResponse(open(ruta_archivo_xlsx, 'rb'))
    response['Content-Type'] ='application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{nombre}.xlsx"'
    return response