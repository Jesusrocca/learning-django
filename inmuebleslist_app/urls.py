
'''
from django.urls import path
from inmuebleslist_app.views import inmueble_list,inmueble_detalle
urlpatterns = [
    path('list/',inmueble_list, name='inmueble-list'), #Devuelve lista
   #inmueble_list es la funcion def que procesa el request se crea en view.py
   #Path que captura para el busqueda por ID
   path('<int:pk>',inmueble_detalle, name='inmueble-detalle'),
]


'''