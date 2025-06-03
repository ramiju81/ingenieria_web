from django.urls import path
from . import views

urlpatterns = [
    path('crear_pedidos/', views.crear_pedidos, name='crear_pedidos'),
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('ver_factura/', views.ver_factura, name='ver_factura')
]

#https://localhost:8000/restaurante/crear_pedidos/
#https://localhost:8000/restaurante/listas_pedidos/
#https://localhost:8000/restaurante/ver_factura/