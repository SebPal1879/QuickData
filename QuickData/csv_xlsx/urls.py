from django.urls import path
from . import views

urlpatterns = [
    path("",views.csv_xlsx,name="csv_xlsx"),
    path("descargar/",views.archivo_ver,name="archivo_ver"),
    path("descargar/<str:nombre>",views.descargar_xlsx,name="descargar_xlsx"),
    path("si",views.si,name="si")
]