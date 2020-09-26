# -*- coding: utf-8 -*-

from django.urls import path

from . import views
# el punto significa la carpeta

urlpatterns = [
    path('', views.home, name='home'),
    path('productos', views.ProductListView.as_view(), name='product-list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('proveedores', views.ProveedorListView.as_view(), name='proveedor-list'),
    #path('proveedores/<int:pk>', views.ProveedorDetailView.as_view(),name='proveedor-detail'),
    
    path('categorias', views.CategoriaListView.as_view(), name='categoria-list'),
    #path('categorias/<int:pk>', views.CategoriaDetailView.as_view(),name='categoria-detail'),
    
    path('localizaciones', views.LocalizacionListView.as_view(), name='localizacion-list'),
    #path('localizaciones/<int:pk>', views.LocalizacionDetailView.as_view(),name='localizacion-detail'),
    
    path('detallepedido', views.DetallePedidoListView.as_view(), name='detallepedido-list'),
    #path('detallepedido/<int:pk>', views.DetallePedidoDetailView.as_view(),name='detallepedido-detail'),
    
    path('pedidos', views.PedidoListView.as_view(), name='pedido-list'),
    #path('pedidos/<int:pk>', views.PedidoDetailView.as_view(),name='pedido-detail'),
    
    path('usuarios', views.UsuarioListView.as_view(), name='usuario-list'),
    #path('usuarios/<int:pk>', views.UsuarioDetailView.as_view(),name='usuario-detail'),
    
    path('clientes', views.ClienteListView.as_view(), name='cliente-list'),
    #path('clientes/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-detail'),
    
    path('colaboradores', views.ColaboradorListView.as_view(), name='colaborador-list'),
    #path('colaboradores/<int:pk>', views.ColaboradorDetailView.as_view(), name='colaborador-detail'),

]
#permite definir patrones de url (links) 
#home es una función creada en views
