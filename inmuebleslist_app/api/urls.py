from django.urls import path
''''
#from inmuebleslist_app.api.views import inmueble_list,inmueble_detalle
urlpatterns = [
    path('list/',inmueble_list, name='inmueble-list'), #invocan funciones def
   path('<int:pk>',inmueble_detalle, name='inmueble-detalle'),
]
'''
from inmuebleslist_app.api.views import InmuebleListAV,InmuebleDetalleAV
urlpatterns = [
    path('list/',InmuebleListAV.as_view(), name='inmueble-list'), #invocan funciones def
   path('<int:pk>',InmuebleDetalleAV.as_view(), name='inmueble-detalle'),
]