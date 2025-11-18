# app_Spa/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs Generales
    path('', views.inicio_spa, name='inicio_spa'),

    # URLs para Usuarios
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('usuarios/actualizar/<int:id_usuario>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/borrar/<int:id_usuario>/', views.borrar_usuario, name='borrar_usuario'),

    # URLs para Categorias
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/', views.ver_categorias, name='ver_categorias'),
    path('categorias/actualizar/<int:id_categoria>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categorias/borrar/<int:id_categoria>/', views.borrar_categoria, name='borrar_categoria'),

    # URLs para Empleados
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id_empleado>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleado, name='borrar_empleado'),

    # URLs para Productos
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/actualizar/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),

    # URLs para Servicios
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/', views.ver_servicios, name='ver_servicios'),
    path('servicios/actualizar/<int:id_servicio>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/borrar/<int:id_servicio>/', views.borrar_servicio, name='borrar_servicio'),

    # URLs para Pedidos
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/actualizar/<int:id_pedido>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/borrar/<int:id_pedido>/', views.borrar_pedido, name='borrar_pedido'),

    # URLs para Detalles de Pedido
    path('detalles-pedido/agregar/', views.agregar_detalle_pedido, name='agregar_detalle_pedido'),
    path('detalles-pedido/', views.ver_detalles_pedido, name='ver_detalles_pedido'),
    path('detalles-pedido/actualizar/<int:id_detalle>/', views.actualizar_detalle_pedido, name='actualizar_detalle_pedido'),
    path('detalles-pedido/borrar/<int:id_detalle>/', views.borrar_detalle_pedido, name='borrar_detalle_pedido'),

    # URLs para Reseñas
    path('reseñas/agregar/', views.agregar_reseña, name='agregar_reseña'),
    path('reseñas/', views.ver_reseñas, name='ver_reseñas'),
    path('reseñas/actualizar/<int:id_reseña>/', views.actualizar_reseña, name='actualizar_reseña'),
    path('reseñas/borrar/<int:id_reseña>/', views.borrar_reseña, name='borrar_reseña'),

    # URLs para Detalles de Servicio
    path('detalles-servicio/agregar/', views.agregar_detalle_servicio, name='agregar_detalle_servicio'),
    path('detalles-servicio/', views.ver_detalles_servicio, name='ver_detalles_servicio'),
    path('detalles-servicio/actualizar/<int:id_detalle_servicio>/', views.actualizar_detalle_servicio, name='actualizar_detalle_servicio'),
    path('detalles-servicio/borrar/<int:id_detalle_servicio>/', views.borrar_detalle_servicio, name='borrar_detalle_servicio'),
]