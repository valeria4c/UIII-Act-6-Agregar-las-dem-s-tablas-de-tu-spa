# app_Spa/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios, Categorias, Empleados, Productos, Servicios, Pedidos, Detalles_pedido, Reseñas, Detalle_servicio
from django.db.models import Sum

# ==========================================
# VISTAS GENERALES
# ==========================================
def inicio_spa(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA USUARIOS
# ==========================================
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        # foto_usuario es opcional
        Usuarios.objects.create(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, direccion=direccion)
        return redirect('ver_usuarios')
    return render(request, 'usuarios/agregar_usuario.html')

def ver_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/ver_usuarios.html', {'usuarios': usuarios})

def actualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuarios, pk=id_usuario)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.correo = request.POST['correo']
        usuario.telefono = request.POST['telefono']
        usuario.direccion = request.POST['direccion']
        # La foto_usuario se manejaría aquí si se subieran archivos
        usuario.save()
        return redirect('ver_usuarios')
    return render(request, 'usuarios/actualizar_usuario.html', {'usuario': usuario})

def borrar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuarios, pk=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('ver_usuarios')
    return render(request, 'usuarios/borrar_usuario.html', {'usuario': usuario})


# ==========================================
# VISTAS PARA CATEGORIAS
# (EJEMPLO - REPLICAR PARA LOS DEMÁS MODELOS)
# ==========================================
def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        activa = request.POST.get('activa', False) == 'on' # Para checkboxes
        Categorias.objects.create(nombre=nombre, descripcion=descripcion, activa=activa)
        return redirect('ver_categorias')
    return render(request, 'categorias/agregar_categoria.html')

def ver_categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'categorias/ver_categorias.html', {'categorias': categorias})

def actualizar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categorias, pk=id_categoria)
    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.descripcion = request.POST['descripcion']
        categoria.activa = request.POST.get('activa', False) == 'on'
        categoria.save()
        return redirect('ver_categorias')
    return render(request, 'categorias/actualizar_categoria.html', {'categoria': categoria})

def borrar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categorias, pk=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categorias/borrar_categoria.html', {'categoria': categoria})


# ==========================================
# VISTAS PARA EMPLEADOS
# ==========================================
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        fecha_contratacion = request.POST['fecha_contratacion'] # Considerar un campo DateInput en HTML
        salario = request.POST['salario']
        horario = request.POST['horario']
        activo = request.POST.get('activo', False) == 'on'
        puesto = request.POST['puesto']
        Empleados.objects.create(
            nombre=nombre, apellido=apellido, correo=correo, telefono=telefono,
            direccion=direccion, fecha_contratacion=fecha_contratacion,
            salario=salario, horario=horario, activo=activo, puesto=puesto
            
        )
        return redirect('ver_empleados')
    return render(request, 'empleados/agregar_empleado.html')

def ver_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleados, pk=id_empleado)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.correo = request.POST['correo']
        empleado.telefono = request.POST['telefono']
        empleado.direccion = request.POST['direccion']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.horario = request.POST['horario']
        empleado.activo = request.POST.get('activo', False) == 'on'
        empleado.puesto = request.POST['puesto']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleados/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleados, pk=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})


# ==========================================
# VISTAS PARA PRODUCTOS
# ==========================================
def agregar_producto(request):
    categorias = Categorias.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        categoria_id = request.POST['categoria']
        categoria = get_object_or_404(Categorias, pk=categoria_id)

        Productos.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
        )
        return redirect('ver_productos')

    return render(request, 'productos/agregar_producto.html', {'categorias': categorias})


def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/ver_productos.html', {'productos': productos})

def actualizar_producto(request, id_producto):
    producto = get_object_or_404(Productos, pk=id_producto)
    categorias = Categorias.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        categoria_id = request.POST['categoria']
        producto.categoria = get_object_or_404(Categorias, pk=categoria_id)
        producto.save()
        return redirect('ver_productos')

    return render(request, 'productos/actualizar_producto.html', {
        'producto': producto,
        'categorias': categorias
    })


def borrar_producto(request, id_producto):
    producto = get_object_or_404(Productos, pk=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'productos/borrar_producto.html', {'producto': producto})

# ==========================================
# VISTAS PARA SERVICIOS
# ==========================================
def agregar_servicio(request):
    categorias = Categorias.objects.all()
    empleados = Empleados.objects.all()
    if request.method == 'POST':
        nombre_servicio = request.POST['nombre_servicio']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        duracion = request.POST['duracion']
        categoria = get_object_or_404(Categorias, pk=request.POST['categoria'])
        productos_utilizados = request.POST.get('productos_utilizados', '')
        empleado_asignado = None
        if request.POST['empleado_asignado']:
            empleado_asignado = get_object_or_404(Empleados, pk=request.POST['empleado_asignado'])
        activo = request.POST.get('activo', False) == 'on'
        Servicios.objects.create(
            nombre_servicio=nombre_servicio, descripcion=descripcion, precio=precio,
            duracion=duracion, categoria=categoria, productos_utilizados=productos_utilizados,
            empleado_asignado=empleado_asignado, activo=activo
        )
        return redirect('ver_servicios')
    return render(request, 'servicios/agregar_servicio.html', {'categorias': categorias, 'empleados': empleados})

def ver_servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/ver_servicios.html', {'servicios': servicios})

def actualizar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicios, pk=id_servicio)
    categorias = Categorias.objects.all()
    empleados = Empleados.objects.all()
    if request.method == 'POST':
        servicio.nombre_servicio = request.POST['nombre_servicio']
        servicio.descripcion = request.POST['descripcion']
        servicio.precio = request.POST['precio']
        servicio.duracion = request.POST['duracion']
        servicio.categoria = get_object_or_404(Categorias, pk=request.POST['categoria'])
        servicio.productos_utilizados = request.POST.get('productos_utilizados', '')
        if request.POST['empleado_asignado']:
            servicio.empleado_asignado = get_object_or_404(Empleados, pk=request.POST['empleado_asignado'])
        else:
            servicio.empleado_asignado = None
        servicio.activo = request.POST.get('activo', False) == 'on'
        servicio.save()
        return redirect('ver_servicios')
    return render(request, 'servicios/actualizar_servicio.html', {'servicio': servicio, 'categorias': categorias, 'empleados': empleados})

def borrar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicios, pk=id_servicio)
    if request.method == 'POST':
        servicio.delete()
        return redirect('ver_servicios')
    return render(request, 'servicios/borrar_servicio.html', {'servicio': servicio})


# ==========================================
# VISTAS PARA PEDIDOS
# ==========================================
def agregar_pedido(request):
    usuarios = Usuarios.objects.all()
    productos = Productos.objects.all()

    if request.method == 'POST':
        # Obtener el usuario y estado del pedido
        usuario = get_object_or_404(Usuarios, pk=request.POST['usuario'])
        estado_pedido = request.POST['estado_pedido']

        # Obtener producto y cantidad
        producto = get_object_or_404(Productos, pk=request.POST['producto'])
        cantidad = int(request.POST['cantidad'])
        precio_unitario = producto.precio
        subtotal = precio_unitario * cantidad

        # Crear el pedido con total calculado automáticamente
        pedido = Pedidos.objects.create(
            usuario=usuario,
            estado_pedido=estado_pedido,
            total_pedido=subtotal
        )

        # Crear el detalle del pedido
        Detalles_pedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            subtotal=subtotal
        )

        return redirect('ver_pedidos')

    return render(request, 'pedidos/agregar_pedido.html', {
        'usuarios': usuarios,
        'productos': productos
    })



def ver_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/ver_pedidos.html', {'pedidos': pedidos})

def actualizar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedidos, pk=id_pedido)
    usuarios = Usuarios.objects.all()
    servicios = Servicios.objects.all()
    if request.method == 'POST':
        pedido.usuario = get_object_or_404(Usuarios, pk=request.POST['usuario'])
        pedido.estado_pedido = request.POST['estado_pedido']
        pedido.total_pedido = request.POST['total_pedido']
        if request.POST['servicio']:
            pedido.servicio = get_object_or_404(Servicios, pk=request.POST['servicio'])
        else:
            pedido.servicio = None
        pedido.save()
        return redirect('ver_pedidos')
    return render(request, 'pedidos/actualizar_pedido.html', {'pedido': pedido, 'usuarios': usuarios, 'servicios': servicios})

def borrar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedidos, pk=id_pedido)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedidos/borrar_pedido.html', {'pedido': pedido})


# ==========================================
# VISTAS PARA DETALLES_PEDIDO
# ==========================================
def agregar_detalle_pedido(request):
    pedidos = Pedidos.objects.all()
    productos = Productos.objects.all()
    if request.method == 'POST':
        pedido = get_object_or_404(Pedidos, pk=request.POST['pedido'])
        producto = get_object_or_404(Productos, pk=request.POST['producto'])
        cantidad = request.POST['cantidad']
        precio_unitario = request.POST['precio_unitario']
        subtotal = float(cantidad) * float(precio_unitario) # Cálculo simple
        notas_item=request.POST.get('notas_item')
        Detalles_pedido.objects.create(
            pedido=pedido, producto=producto, cantidad=cantidad,
            precio_unitario=precio_unitario, subtotal=subtotal, notas_item=notas_item
        )
        return redirect('ver_detalles_pedido')
    return render(request, 'detalles_pedido/agregar_detalle_pedido.html', {'pedidos': pedidos, 'productos': productos})

def ver_detalles_pedido(request):
    detalles_pedido = Detalles_pedido.objects.all()
    return render(request, 'detalles_pedido/ver_detalles_pedido.html', {'detalles_pedido': detalles_pedido})

def actualizar_detalle_pedido(request, id_detalle):
    detalle = get_object_or_404(Detalles_pedido, pk=id_detalle)
    pedidos = Pedidos.objects.all()
    productos = Productos.objects.all()
    if request.method == 'POST':
        detalle.pedido = get_object_or_404(Pedidos, pk=request.POST['pedido'])
        detalle.producto = get_object_or_404(Productos, pk=request.POST['producto'])
        detalle.cantidad = request.POST['cantidad']
        detalle.precio_unitario = request.POST['precio_unitario']
        detalle.subtotal = float(detalle.cantidad) * float(detalle.precio_unitario)
        notas_item=request.POST.get('notas_item')
        detalle.save()
        return redirect('ver_detalles_pedido')
    return render(request, 'detalles_pedido/actualizar_detalle_pedido.html', {'detalle': detalle, 'pedidos': pedidos, 'productos': productos})

def borrar_detalle_pedido(request, id_detalle):
    detalle = get_object_or_404(Detalles_pedido, pk=id_detalle)
    if request.method == 'POST':
        detalle.delete()
        return redirect('ver_detalles_pedido')
    return render(request, 'detalles_pedido/borrar_detalle_pedido.html', {'detalle': detalle})


# ==========================================
# VISTAS PARA RESEÑAS
# ==========================================
def agregar_reseña(request):
    productos = Productos.objects.all()
    usuarios = Usuarios.objects.all()
    servicios = Servicios.objects.all()
    if request.method == 'POST':
        producto = get_object_or_404(Productos, pk=request.POST['producto'])
        usuario = get_object_or_404(Usuarios, pk=request.POST['usuario'])
        servicio = None
        if request.POST['servicio']:
            servicio = get_object_or_404(Servicios, pk=request.POST['servicio'])
        calificacion = request.POST['calificacion']
        comentario = request.POST['comentario']
        aprobada = request.POST.get('aprobada', False) == 'on'
        Reseñas.objects.create(
            producto=producto, usuario=usuario, servicio=servicio,
            calificacion=calificacion, comentario=comentario, aprobada=aprobada
        )
        return redirect('ver_reseñas')
    return render(request, 'reseñas/agregar_reseña.html', {'productos': productos, 'usuarios': usuarios, 'servicios': servicios})

def ver_reseñas(request):
    reseñas = Reseñas.objects.all()
    return render(request, 'reseñas/ver_reseñas.html', {'reseñas': reseñas})

def actualizar_reseña(request, id_reseña):
    reseña = get_object_or_404(Reseñas, pk=id_reseña)
    productos = Productos.objects.all()
    usuarios = Usuarios.objects.all()
    servicios = Servicios.objects.all()
    if request.method == 'POST':
        reseña.producto = get_object_or_404(Productos, pk=request.POST['producto'])
        reseña.usuario = get_object_or_404(Usuarios, pk=request.POST['usuario'])
        if request.POST['servicio']:
            reseña.servicio = get_object_or_404(Servicios, pk=request.POST['servicio'])
        else:
            reseña.servicio = None
        reseña.calificacion = request.POST['calificacion']
        reseña.comentario = request.POST['comentario']
        reseña.aprobada = request.POST.get('aprobada', False) == 'on'
        reseña.save()
        return redirect('ver_reseñas')
    return render(request, 'reseñas/actualizar_reseña.html', {'reseña': reseña, 'productos': productos, 'usuarios': usuarios, 'servicios': servicios})

def borrar_reseña(request, id_reseña):
    reseña = get_object_or_404(Reseñas, pk=id_reseña)
    if request.method == 'POST':
        reseña.delete()
        return redirect('ver_reseñas')
    return render(request, 'reseñas/borrar_reseña.html', {'reseña': reseña})


# ==========================================
# VISTAS PARA DETALLE_SERVICIO
# ==========================================
def agregar_detalle_servicio(request):
    servicios = Servicios.objects.all()
    productos = Productos.objects.all()
    if request.method == 'POST':
        servicio = get_object_or_404(Servicios, pk=request.POST['servicio'])
        producto = get_object_or_404(Productos, pk=request.POST['producto'])
        cantidad_usada = request.POST['cantidad_usada']
        Detalle_servicio.objects.create(
            servicio=servicio, producto=producto, cantidad_usada=cantidad_usada
        )
        return redirect('ver_detalles_servicio')
    return render(request, 'detalles_servicio/agregar_detalle_servicio.html', {'servicios': servicios, 'productos': productos})

def ver_detalles_servicio(request):
    detalles_servicio = Detalle_servicio.objects.all()
    return render(request, 'detalles_servicio/ver_detalles_servicio.html', {'detalles_servicio': detalles_servicio})

def actualizar_detalle_servicio(request, id_detalle_servicio):
    detalle = get_object_or_404(Detalle_servicio, pk=id_detalle_servicio)
    servicios = Servicios.objects.all()
    productos = Productos.objects.all()
    if request.method == 'POST':
        detalle.servicio = get_object_or_404(Servicios, pk=request.POST['servicio'])
        detalle.producto = get_object_or_404(Productos, pk=request.POST['producto'])
        detalle.cantidad_usada = request.POST['cantidad_usada']
        detalle.save()
        return redirect('ver_detalles_servicio')
    return render(request, 'detalles_servicio/actualizar_detalle_servicio.html', {'detalle': detalle, 'servicios': servicios, 'productos': productos})

def borrar_detalle_servicio(request, id_detalle_servicio):
    detalle = get_object_or_404(Detalle_servicio, pk=id_detalle_servicio)
    if request.method == 'POST':
        detalle.delete()
        return redirect('ver_detalles_servicio')
    return render(request, 'detalles_servicio/borrar_detalle_servicio.html', {'detalle': detalle})