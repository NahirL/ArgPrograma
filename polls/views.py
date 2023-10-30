from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def consultar(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {'productos' : productos})


def guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
    producto.save()
    messages.success(request, '¡Producto agregado!')
    return redirect('consultar')


def eliminar(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('consultar')


def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    messages.success(request, '¡Producto editado!')
    return render(request, "productoEditar.html", {'producto' : producto})


def editar(request, id):
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    descripcion = request.POST['descripcion']
    id = request.POST['id']
    Producto.objects.filter(pk=id).update(id=id, nombre=nombre, precio=precio, descripcion=descripcion)
    messages.success(request, '¡Producto actualizado!')
    return redirect('consultar')


