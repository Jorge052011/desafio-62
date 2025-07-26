

from .views import lista_empleados
from django.urls import path

urlpatterns = [
    path("", lista_empleados, name='lista_empleados'),
]