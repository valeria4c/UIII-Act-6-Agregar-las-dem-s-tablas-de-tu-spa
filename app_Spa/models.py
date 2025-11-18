from django.db import models

# ==========================================
# MODELO: USUARIOS
# ==========================================
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(max_length=25, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: CATEGORIAS
# ==========================================
class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# ==========================================
# MODELO: EMPLEADOS
# ==========================================
class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=25)
    fecha_contratacion = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    horario = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"


# ==========================================
# MODELO: PRODUCTOS
# ==========================================
class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre


# ==========================================
# MODELO: SERVICIOS
# ==========================================
class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True, unique=True)
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.IntegerField()
    categoria = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE,
        related_name="servicios"
    )
    productos_utilizados = models.TextField(blank=True, null=True)
    empleado_asignado = models.ForeignKey(
        Empleados,
        on_delete=models.SET_NULL,
        related_name="servicios",
        null=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_servicio


# ==========================================
# MODELO: PEDIDOS
# ==========================================
class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.CASCADE,
        related_name="pedidos"
    )
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=50)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.usuario.nombre}"


# ==========================================
# MODELO: DETALLES_PEDIDO
# ==========================================
class Detalles_pedido(models.Model):
    id_detalle = models.AutoField(primary_key=True, unique=True)
    pedido = models.ForeignKey(
        Pedidos,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    notas_item = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Detalle {self.id_detalle} - {self.producto.nombre}"


# ==========================================
# MODELO: RESEÑAS
# ==========================================
class Reseñas(models.Model):
    id_reseña = models.AutoField(primary_key=True, unique=True)
    producto = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE,
        related_name="reseñas"
    )
    usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.CASCADE,
        related_name="reseñas"
    )
    servicio = models.ForeignKey(
        Servicios,
        on_delete=models.SET_NULL,
        related_name="reseñas",
        null=True
    )
    calificacion = models.IntegerField(default=5)
    comentario = models.TextField()
    fecha_reseña = models.DateTimeField(auto_now_add=True)
    aprobada = models.BooleanField(default=True)

    def __str__(self):
        return f"Reseña de {self.usuario} - {self.calificacion}⭐"


# ==========================================
# MODELO: DETALLE_SERVICIO
# ==========================================
class Detalle_servicio(models.Model):
    id_detalle_servicio = models.AutoField(primary_key=True, unique=True)
    servicio = models.ForeignKey(
        Servicios,
        on_delete=models.CASCADE,
        related_name="detalles_servicio"
    )
    producto = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE,
        related_name="detalles_servicio"
    )
    cantidad_usada = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} usado en {self.servicio.nombre_servicio}"
