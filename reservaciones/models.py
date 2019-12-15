from __future__ import unicode_literals
from django.conf import settings
from django.core.validators import MaxValueValidator

from django.db import models

# Create your models here.



class Persona(models.Model):
	"""docstring for Persona"""
	id_persona = models.AutoField(primary_key=True, )
	cedula = models.CharField(max_length = 15, unique=True)
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	nacionalidad = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 15)
	barrio = models.CharField(max_length = 15)
#	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	e_civil= models.CharField(max_length = 2000, blank = False, null= False, verbose_name= "Estado Civil")
	f_nac= models.DateField()
	estado = models.BooleanField()
	genero = models.BooleanField()
	email = models.EmailField()

	def __unicode__(self):
		return '%s %s %s' % (self.cedula, self.nombre, self.apellido)

class Reserva(models.Model):
	"""docstring for Reserva"""

	id_reserva = models.AutoField(primary_key=True)
	persona = models.ForeignKey('Persona')
	fecha_reserva = models.DateField(auto_now_add = True, auto_now = False)
	fecha_entrada = models.DateField()
	fecha_salida = models.DateField()
	dias = models.IntegerField()
	estado = models.IntegerField()
	abono = models.BooleanField() 
	total = models.DecimalField(max_digits=8, decimal_places=2)
	

	def __unicode__(self):	
		return str(self.abono)
		

class DetalleReserva(models.Model):
	"""docstring for Detalle"""

	id_detallereserva = models.AutoField(primary_key=True)
	cantidad = models.IntegerField()
	descripcion = models.CharField(max_length = 30)
	precio_uni = models.DecimalField(max_digits=5, decimal_places=2)
	precio_total = models.DecimalField(max_digits=7, decimal_places=2)
	reserva = models.ForeignKey('Reserva')
	cant_adultos = models.IntegerField()
	cant_ninos = models.IntegerField()
	id_tipohabitacion = models.IntegerField()

	def __unicode__(self):
		return str(self.cantidad)

class Factura(models.Model):
	"""docstring for Factura"""

	id_factura = models.AutoField(primary_key=True)
	fecha = models.DateTimeField()
	id_reserva = models.IntegerField() 
	subtotal = models.DecimalField(max_digits=7, decimal_places=2)
	iva =  models.DecimalField(max_digits=6, decimal_places=2)
	descuento = models.DecimalField(max_digits=6, decimal_places=2)
	total = models.DecimalField(max_digits=8, decimal_places=2)
	numero_factura = models.CharField(max_length = 15)
	estado_factura = models.BooleanField()
	dias = models.IntegerField()
	id_persona = models.IntegerField()

	def __unicode__(self):
		return '%s' % self.numero_factura

class DetalleFactura(models.Model):
	"""docstring for DetalleFactura"""
	id_detallefactura = models.AutoField(primary_key=True)
	cantidad = models.IntegerField()
	precio_uni = models.DecimalField(max_digits=5, decimal_places=2)
	precio_total = models.DecimalField(max_digits=7, decimal_places=2)
	cant_adultos = models.IntegerField()
	cant_ninos = models.IntegerField()
	habitacion = models.ForeignKey('Habitacion')
	servicio = models.ForeignKey('Servicio')
	factura = models.ForeignKey('Factura')


	def __unicode__(self, arg):
		return str(self.cantidad)		
		

class Servicio(models.Model):
 	"""docstring for Servicio"""
 	id_servicio = models.AutoField(primary_key=True)
 	nombre = models.CharField(max_length = 40)
 	precio = models.DecimalField(max_digits=7, decimal_places=2)
 	estado = models.BooleanField()

 	def __unicode__(self):
 		return '%s' % self.nombre
 		 		

class Habitacion(models.Model):
	"""docstring for Habitacion"""
	class Meta:
		 verbose_name_plural = "Habitaciones"

	id_habitacion = models.AutoField(primary_key=True)
	numero_habitacion= models.IntegerField()
	piso_habitacion = models.IntegerField()
	estado_habitacion = models.CharField(max_length= 50)
	tipohabitacion = models.ForeignKey('tipohabitacion')

	def __unicode__(self):
		return str(self.numero_habitacion)


class TipoHabitacion(models.Model):
	"""docstring for TipoHabitacion"""
	class Meta:
		 verbose_name_plural = "Tipo Habitaciones"

	id_tipohabitacion = models.AutoField(primary_key=True)
	imagen = models.ImageField(upload_to = 'tiposHab', null=False, blank=False)
	nombre_tipo = models.CharField(max_length = 100)
	precio_tipo = models.DecimalField(max_digits=6, decimal_places=2)
	nro_personas = models.IntegerField()

	def __unicode__(self):
		return '%s' % self.nombre_tipo	

class Registrado(models.Model):
	nombre = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self): #Python 2
		return self.email

class Galeria(models.Model):
	"""docstring for Galeria"""
	
	id_galeria = models.AutoField(primary_key=True)
	imagen = models.ImageField(upload_to = 'galeria', null=False, blank=False)
	nombre_imagen = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombre_imagen
