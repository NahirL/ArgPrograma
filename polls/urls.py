from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("productos", views.consultar, name="consultar"),
    path("productos/guardar", views.guardar, name="guardar"),
    path("productos/eliminar/<int:id>", views.eliminar, name="eliminar"),
    path("productos/detalle/<int:id>", views.detalle, name="detalle"),
    path("productos/editar/<int:id>", views.editar, name="editar"),
]