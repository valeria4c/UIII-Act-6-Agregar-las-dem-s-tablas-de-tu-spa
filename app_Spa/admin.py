# app_Spa/admin.py
from django.contrib import admin
from .models import Usuarios, Categorias, Empleados, Productos, Servicios, Pedidos, Detalles_pedido, Reseñas, Detalle_servicio

admin.site.register(Usuarios)
admin.site.register(Categorias)
admin.site.register(Empleados)
admin.site.register(Productos)
admin.site.register(Servicios)
admin.site.register(Pedidos)
admin.site.register(Detalles_pedido)
admin.site.register(Reseñas)
admin.site.register(Detalle_servicio)