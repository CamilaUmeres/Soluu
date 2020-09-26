from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Producto, Proveedor, Categoria, Localizacion, DetallePedido, Pedido, Usuario,Colaborador, Cliente

# Create your views here.
def home(request):
    return HttpResponse("Hola mundo.")

#esto es una vista que gestiona qué se le respondera al usuario
#Http es como se comunica el internet
#Solo le aparecerá hola mundo

class ProductListView(ListView):
    model = Producto

class ProductDetailView(DetailView):
    model = Producto 

class ProveedorListView(ListView):
    model = Proveedor

class ProveedorDetailView(DetailView):
    model = Proveedor

class CategoriaListView(ListView):
    model = Categoria

class CategoriaDetailView(DetailView):
    model = Categoria

class LocalizacionListView(ListView):
    model = Localizacion

class LocalizacionDetailView(DetailView):
    model = Localizacion

class DetallePedidoListView(ListView):
    model = DetallePedido

class DetallePedidoDetailView(DetailView):
    model = DetallePedido

class PedidoListView(ListView):
    model = Pedido

class PedidoDetailView(DetailView):
    model = Pedido

class UsuarioListView(ListView):
    model = Usuario

class UsuarioDetailView(DetailView):
    model = Usuario

class ColaboradorListView(ListView):
    model = Colaborador

class ColaboradorDetailView(DetailView):
    model = Colaborador

class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente


