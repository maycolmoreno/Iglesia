# -*- coding: utf-8 -*-

from django.shortcuts import render

# from .models import Cliente
# from .forms import ClienteForm
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
import datetime
from django.contrib.auth.models import User
from decimal import Decimal
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def mostrar_inicio(request):
	return render(request, 'villonaco/index.html', {})

def mostrar_quienes_somos(request):
	return render(request, 'villonaco/about.html', {})

def mostrar_habitaciones(request):
	tiposHabitaciones = TipoHabitacion.objects.all()
	return render(request, 'villonaco/rooms.html', {'lista':tiposHabitaciones})

def mostrar_galeria(request):
	imagenes = Galeria.objects.all()
	return render(request, 'villonaco/gallery.html', {'galeria':imagenes})

def mostrar_contactos(request):
	return render(request, 'villonaco/contact.html', {})

# def mostrar_detallesimple(request):
# 	tiposHabitaciones = TipoHabitacion.objects.all()
# 	return render(request, 'villonaco/detalle_simple.html', {'lista':tiposHabitaciones})

# def mostrar_detalledoble(request):
# 	return render(request, 'villonaco/detalle_doble.html', {})
	
# def mostrar_detalletriple(request):
# 	return render(request, 'villonaco/detalle_triple.html', {})

@login_required	
def mostrar_disponibilidad(request):
	return render(request, 'villonaco/booking.html', {})



def registrarse(request):
	form = PersonaForm(request.POST or None)
	user = UserForm(request.POST or None)

	context = {
		"form":form,
		"formu":user
		}

	if request.method == "POST":
		form = PersonaForm(request.POST or None, initial = {"id_persona" : "0"})
		formu = UserForm(request.POST or None, initial = {"id" : "0"})
		if form.is_valid() and formu.is_valid():
			print("lleuw aqui")

			user = formu.save()
			print("Guardo")
			#form.user = User.objects.last()
			user.set_password(user.password)
			user.save()
			persona = form.save(commit = False)
			print("Guardoe")
			persona.user = user
			print("Guardo12")
			persona.save()
			return redirect('auth_login')
	else:
		#form = PersonaForm()	
		return render(request, 'registration/register.html', context)

def inicio(request):
	titulo = "Bienvenidos."
	if request.user.is_authenticated():
		titulo = "Bienvenid@ %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
				"titulo": titulo,
				"el_form": form,
			}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "PERSONA"
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

		if not nombre:
			context = {
				"titulo": "Gracias %s!" %(email)
			}

	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Registrado.objects.all().order_by("-timestamp")
		context = {
			"queryset": queryset,
		}
	return render(request, "inicio.html", context)

def contact(request):
	titulo = "Contacto"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)

		# print email, mensaje, nombre
	context = {
		"form": form,
		"titulo": titulo,
	}
	return render(request, "villonaco/contact.html", context)


## Funciones del Panel de Administracion

@staff_member_required
def mostrar_administracion(request):
	return render(request, 'administration/dashboard.html', {})

@staff_member_required
def listar_clientes(request):
	persona = Persona.objects.all()
	return render(request, 'administration/lista_clientes.html', {'listaPer':persona})

@staff_member_required
def listar_usuarios(request):
	usuario = User.objects.filter(is_staff = True)
	return render(request, 'administration/lista_usuarios.html', {'listaUs':usuario})

@staff_member_required
def listar_habitaciones(request):
	habitacion = Habitacion.objects.all()
	return render(request, 'administration/lista_habitaciones.html', {'listaHab':habitacion})

@staff_member_required
def listar_tipohabitaciones(request):
	tipohabitacion = TipoHabitacion.objects.all()
	return render(request, 'administration/lista_tipoHab.html', {'listaTipo':tipohabitacion})

@staff_member_required
def listar_servicios(request):
	servicio = Servicio.objects.all()
	return render(request, 'administration/lista_servicios.html', {'listaServicios':servicio})

@staff_member_required
def listar_reservas(request):
	reserva = Reserva.objects.filter(estado=1)
	#detalle = DetalleReserva.objects.all()
	return render(request, 'administration/lista_reservas.html', {
		'listareserva':reserva
		})

@staff_member_required
def listar_facturas(request):
	factura = Factura.objects.all()
	return render(request, 'administration/lista_facturas.html', { 'listafactura':factura, })

@staff_member_required
def listar_galeria(request):
	galeria = Galeria.objects.all()
	return render(request, 'administration/lista_galeria.html', { 'listagaleria':galeria, })

@staff_member_required
def crear_usuario(request):
	if request.method == "POST":
		clienteexiste = Persona.objects.get(cedula=request.POST["cedula"])
		if clienteexiste:
			messages.error(request, 'Cedula Repetida.')
		else:
			cliente = Persona.objects.create(
			cedula = request.POST["cedula"],
			nombre = request.POST["nombres"],
			telefono = request.POST["telefono"],
			barrio= request.POST["barrio"],
			direccion = request.POST["direccion"],
			e_civil = request.POST["Estado Civil"],
			f_nac = request.POST["Fecha de nacieminto"],
			estado = request.POST["Activo o Inactivo"],
   			genero = request.POST["M o F"],
			email = request.POST["email"],
			)
			cliente.save()

	return render(request, 'administration/crear_cliente.html', {})

# @staff_member_required
# def crear_cliente(request):
# 	if request.method == "POST":
# 		usuario = Persona.objects.create(
# 			first_name = request.POST["nombres"], 
# 			last_name = request.POST["apellidos"],
# 			email = request.POST["correo"],
# 			username = request.POST["usuario"],
# 			password = request.POST["contra"],
# 			is_superuser = False,
# 			is_staff = True,
# 			is_active = True,
# 			)
# 		usuario.save()

# 	return render(request, 'administration/crear_usuario.html', {})

@staff_member_required
def crear_habitacion(request):
	tipos = TipoHabitacion.objects.all()
	if request.method == "POST":
		Numero = request.POST["numero"]
		Piso = request.POST["piso"]
		tipohab = TipoHabitacion.objects.get(id_tipohabitacion=request.POST["tiposHabitaciones"]);	
		habitacion = Habitacion.objects.create(
			#id_habitacion = int(request.POST["idvalor"]),
			numero_habitacion = int(Numero),
			piso_habitacion = int(Piso),
			estado_habitacion = request.POST["hosting"], 
			tipohabitacion = tipohab,

			)
		habitacion.save()

	return render(request, 'administration/crear_habitacion.html', {'lista':tipos})

@staff_member_required
def crear_tipohabitacion(request):
	if request.method == "POST":
		tipo = TipoHabitacion.objects.create(
			imagen = request.FILES.get('imagen'),
			nombre_tipo = request.POST["nombre"],
			precio_tipo = request.POST["precio"],
			nro_personas = request.POST["personas"],

			)
		tipo.save()

	return render(request, 'administration/crear_tipohabitacion.html')

@staff_member_required
def crear_servicio(request):
	if request.method == 'POST':
		servicio = Servicio.objects.create(
			nombre = request.POST["nombre"],
			precio = request.POST["precio"],
			estado = int("1")

			)
		servicio.save()
	return render(request, 'administration/crear_servicio.html', {})

@staff_member_required
def modificar_cliente(request):
	if request.method == "POST":
		cliente = Persona.objects.get(id_persona=request.POST["id_persona"])
				
		cliente.nombre = request.POST["nombres"]
		cliente.apellido = request.POST["apellidos"]
		cliente.nacionalidad = request.POST["nacional"]
		cliente.direccion = request.POST["direccion"]
		cliente.telefono = request.POST["telefono"]
		
		cliente.save()

	return render(request, 'administration/lista_clientes.html', {"listaPer":Persona.objects.all()})

@staff_member_required
def modificar_usuario(request):
	if request.method == "POST":
		usuario = User.objects.get(id=request.POST["id"])

		usuario.first_name = request.POST["nombres"]
		usuario.last_name = request.POST["apellidos"]
		usuario.email = request.POST["correo"]
		usuario.username = request.POST["usuario"]
		usuario.password = request.POST["contra"]
		usuario.is_superuser = False
		usuario.is_staff = True
		usuario.is_active = True
			
		usuario.save()

	return render(request, 'administration/lista_usuarios.html', {"listaUs":User.objects.all()})

@staff_member_required
def modificar_servicio(request):
	if request.method == 'POST':
		servicio = Servicio.objects.get(id_servicio=request.POST["id_servicio"])

		servicio.nombre = request.POST["nombre"]
		servicio.precio = request.POST["precio"]
		servicio.estado = int("1")

		servicio.save()
	return render(request, 'administration/lista_servicios.html', {'listaServicios':Servicio.objects.all()})

@staff_member_required
def modificar_habitacion(request):
	tipos = TipoHabitacion.objects.all()
	if request.method == "POST":
		
		tipohab = TipoHabitacion.objects.get(id_tipohabitacion=request.POST["tiposHabitaciones"]);	
		habitacion = Habitacion.objects.get(id_habitacion=request.POST["id_habitacion"])
		habitacion.numero_habitacion = request.POST["numero"],
		habitacion.piso_habitacion = request.POST["piso"],
		habitacion.estado_habitacion = request.POST["hosting"], 
		habitacion.tipohabitacion = tipohab,

		habitacion.save()

	return render(request, 'administration/lista_habitaciones.html', {
		'listaHab':Habitacion.objects.all(),
		'lista':tipos})


@staff_member_required
def modificar_tipohabitacion(request):
	if request.method == "POST":
		tipo = TipoHabitacion.objects.get(id_habitacion=request.POST["id_tipohabitacion"])
		tipo.imagen = request.FILES.get('imagen'),
		tipo.nombre_tipo = request.POST["nombre"],
		tipo.precio_tipo = request.POST["precio"],
		tipo.nro_personas = request.POST["personas"],

		tipo.save()

	return render(request, 'administration/lista_tipoHab.html')

@staff_member_required
def mostrar_disponibilidad_admin(request):
	return render(request, 'administration/crear_reserva.html', {})


@staff_member_required
def crear_reserva_admin(request):
	if request.method == "POST":
		fechaEntrada = datetime.datetime.strptime(request.POST["check-in"], "%Y-%m-%d").date()
		fechaSalida = datetime.datetime.strptime(request.POST["check-out"], "%Y-%m-%d").date()
		lista = TipoHabitacion.objects.all()
		dias = request.POST["duration"]
		tipos = []
		#nros = []
		i = 0
		for obj in lista:
			listaReserva = Reserva.objects.filter(estado=1).filter(fecha_entrada__range = [fechaEntrada,fechaSalida]).filter(fecha_salida__range = [fechaEntrada,fechaSalida])
			for objRes in listaReserva:
				detalle = DetalleReserva.objects.get(reserva=objRes)
				if detalle.id_tipohabitacion == obj.id_tipohabitacion:
					i = i+1
			##aux0 = DetalleReserva.objects.filter(id_tipohabitacion = )
			#aux = Reserva.objects.filter(fecha_entrada__range = [fechaEntrada,fechaSalida]).filter(estado=1).count()
			#aux2 = Reserva.objects.filter(fecha_salida__range = [fechaEntrada,fechaSalida]).filter(estado=1).count()
			
			nro = Habitacion.objects.filter(tipohabitacion=obj).count()
			nro = nro-i
			#nros.append(nro)
			tipos.append((obj, nro, range(1, (obj.nro_personas+1)), range(0,obj.nro_personas+1)))
			i = 0
			#tipo = TipoHabitacion.objects.get(nombre_tipo=obj.nombre_tipo)
					
			#tiposimple = TipoHabitacion.objects.get(nombre_tipo="Simple")
			#nroSimple = Habitacion.objects.filter(tipohabitacion=tiposimple).count()
		return render(request, 'administration/registrar_reserva.html', {
				"tipos" : tipos,
				"fechaEntrada" : request.POST["check-in"],
				"fechaSalida" : request.POST["check-out"],
				"listaPersona" : Persona.objects.all(),
				"duracion" : dias })

@staff_member_required
def registrar_reserva_admin(request):
	if request.method == "POST":
		fechaEntrada = datetime.datetime.strptime(request.POST["inicio"], "%Y-%m-%d").date()
		fechaSalida = datetime.datetime.strptime(request.POST["fin"], "%Y-%m-%d").date()
		itemsString = request.POST["reserve"]
		itemsData = itemsString.split(';')
		
		print(itemsString)		
		persona = Persona.objects.get(id_persona=request.POST["persona"])
		#usuario = User.objects.get(persona.user.id)
		reserva = Reserva.objects.create(
			fecha_entrada = fechaEntrada, 
			fecha_salida = fechaSalida, 
			dias = int(request.POST["duracion"]), 
			estado = int("1"), 
			abono = False,
			persona = persona,
			total = float(request.POST["total"]))
		
		
		
		reserva.save()
		mensaje = "Se ha hecho tu reserva para " + request.POST["duracion"] + " dia(s), su reserva va desde el dia " + request.POST["inicio"] + " hasta " + request.POST["fin"]
		for data in itemsData:

			itemsItems = data.split(':')
			print(itemsItems[0]+" df")
			if len(itemsItems) > 1:
				nombre = itemsItems[1]
				print(nombre)
				tipoHab = TipoHabitacion.objects.get(nombre_tipo=nombre)
				detalleReserva = DetalleReserva.objects.create(
					cantidad = int(itemsItems[0]),
					descripcion = itemsItems[1],
					precio_uni = float(itemsItems[4]),
					precio_total = float(itemsItems[4]),
					reserva = reserva,
					cant_adultos = int(itemsItems[2]),
					cant_ninos = int(itemsItems[3]),
					id_tipohabitacion = tipoHab.id_tipohabitacion
					)
		form_email = ""
		form_mensaje = mensaje
		form_nombre = "Hotel villonaco"
		asunto = 'Reserva Realizada'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, persona.user.email]
		email_mensaje = mensaje
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)				

	return render(request, 'villonaco/message.html', {})


@staff_member_required
def crear_factura(request):
	return render(request, 'administration/crear_factura.html', {})


@staff_member_required
def detalle_reserva(request, pk):
	
	reserva = Reserva.objects.get(id_reserva=pk)
	detalle = DetalleReserva.objects.filter(reserva=reserva)
	tipoSimple = TipoHabitacion.objects.get(nombre_tipo="Simple")
	tipoDoble = TipoHabitacion.objects.get(nombre_tipo="Doble")
	tipoTriple = TipoHabitacion.objects.get(nombre_tipo="Triple")
	simple = Habitacion.objects.filter(estado_habitacion="DISPONIBLE",tipohabitacion=tipoSimple)
	doble = Habitacion.objects.filter(estado_habitacion="DISPONIBLE",tipohabitacion=tipoDoble)
	triple = Habitacion.objects.filter(estado_habitacion="DISPONIBLE",tipohabitacion=tipoTriple)
	persona = Persona.objects.get(id_persona=reserva.persona.id_persona)
	return render(request, 'administration/detalle_reserva.html', {'listadetalle':detalle, 
		'simple':simple, 'doble':doble, 'triple':triple, 'persona':persona, 'reserva':reserva})
	
@staff_member_required	
def registrar_factura(request):
	if request.method == "POST":
		now = datetime.datetime.now()
		fecha = datetime.datetime.strptime(now.strftime('%Y-%m-%d'), "%Y-%m-%d").date()
		#fechaSalida = datetime.datetime.strptime(request.POST["fin"], "%Y-%m-%d").date()
		itemsString = request.POST["datas"]
		itemsData = itemsString.split(';')
		usuario = User.objects.get(id=request.user.id)
		id_reserva = int(request.POST["idreserva"])
		reserva = Reserva.objects.get(id_reserva=id_reserva)
		subtotal = float(request.POST["subtotal"])
		total = float(request.POST["total"])
		iva = float(request.POST["iva"])
		descuento = 0.0;
		#estado_factura = True
		id_persona = reserva.persona.id_persona
		nroFact = "001-001-000000"+str(Factura.objects.count())
		dias = reserva.dias
		print(str(len(itemsData)))
		
		#estado_habitacion="DISPONIBLE"
		#persona = Persona.objects.get(user=usuario)
		#dias = dias,
		factura = Factura.objects.create(
			fecha = fecha, 
			id_reserva = id_reserva, 
			subtotal = subtotal,
			iva = iva,
			descuento = descuento,
			dias = dias,			
			total = total,
			numero_factura = nroFact,
			estado_factura = True,
			id_persona = id_persona	)
		
		factura.save()
		
		for data in itemsData:

			itemsItems = data.split(':')
			print(data+" xx----****")
			if len(itemsItems) > 1:
				print(itemsItems[0]+" ****")
				print(itemsItems[6]+" ****")
				print(itemsItems[4]+" ****----")
				habitacion = Habitacion.objects.get(id_habitacion=int(itemsItems[6]))
				detalleFactura = DetalleFactura.objects.create(
					cantidad = int(itemsItems[0]),
					precio_uni = float(itemsItems[4]),
					precio_total = float(itemsItems[5]),
					cant_adultos = int(itemsItems[2]),
					cant_ninos = int(itemsItems[3]),
					habitacion = habitacion,
					factura = factura)
				habitacion.estado_habitacion="OCUPADA"
				habitacion.save()
		reserva.estado = 2

		reserva.save()		
	factura = Factura.objects.all()
	#detalleFac = DetalleFactura.objects.all()
	return render(request, 'administration/lista_facturas.html', {'listafactura':factura})

@staff_member_required	
def levantar_factura(request, pk):
	factura = Factura.objects.get(id_factura=pk)
	print(factura.subtotal)
	detalleFacturas = DetalleFactura.objects.filter(factura=factura)
	for obj in detalleFacturas:
		print("xxxxx")
		habitacion = Habitacion.objects.get(id_habitacion=obj.habitacion.id_habitacion)
		habitacion.estado_habitacion = "DISPONIBLE"
		habitacion.save()
	factura.estado_factura = False
	factura.save()
	print ("fghjkk")
	facturas = Factura.objects.all()
	return render(request, 'administration/lista_facturas.html', { 'listafactura':facturas, })

@staff_member_required	
def obtener_cliente(request, pk):
	return render(request, 'administration/modificar_cliente.html', {"persona":Persona.objects.get(id_persona=pk)})

@staff_member_required	
def obtener_usuario(request, pk):
	return render(request, 'administration/modificar_usuario.html', {"usuario":User.objects.get(id=pk)})

@staff_member_required	
def obtener_servicio(request, pk):
	return render(request, 'administration/modificar_servicio.html', {"servicio":Servicio.objects.get(id_servicio=pk)})

@staff_member_required	
def obtener_habitacion(request, pk):
	return render(request, 'administration/modificar_habitacion.html', {"habitacion":Habitacion.objects.get(id_habitacion=pk)})

@staff_member_required	
def obtener_tipohabitacion(request, pk):
	return render(request, 'administration/modificar_tipohabitacion.html', {"tipohabitacion":TipoHabitacion.objects.get(id_tipohabitacion=pk)})

##Reservaciones

#Crea una nueva reserva por vistas de cliente

def registrar_reserva(request):
	if request.method == "POST":
		fechaEntrada = datetime.datetime.strptime(request.POST["inicio"], "%Y-%m-%d").date()
		fechaSalida = datetime.datetime.strptime(request.POST["fin"], "%Y-%m-%d").date()
		itemsString = request.POST["reserve"]
		itemsData = itemsString.split(';')
		usuario = User.objects.get(id=request.user.id)
		print(itemsString)
		
		persona = Persona.objects.get(user=usuario)
		
		reserva = Reserva.objects.create(
			fecha_entrada = fechaEntrada, 
			fecha_salida = fechaSalida, 
			dias = int(request.POST["duracion"]), 
			estado = int("1"), 
			abono = False,
			persona = persona,
			total = float(request.POST["total"]))
		
		
		
		reserva.save()
		
		for data in itemsData:

			itemsItems = data.split(':')
			print(itemsItems[0]+" df")
			if len(itemsItems) > 1:
				nombre = itemsItems[1]
				print(nombre)
				tipoHab = TipoHabitacion.objects.get(nombre_tipo=nombre)
				detalleReserva = DetalleReserva.objects.create(
					cantidad = int(itemsItems[0]),
					descripcion = itemsItems[1],
					precio_uni = float(itemsItems[4]),
					precio_total = float(itemsItems[4]),
					reserva = reserva,
					cant_adultos = int(itemsItems[2]),
					cant_ninos = int(itemsItems[3]),
					id_tipohabitacion = tipoHab.id_tipohabitacion
					)
		form_email = ""
		form_mensaje = "Datos de la reserva"
		form_nombre = "Hotel villonaco"
		asunto = 'Reserva Realizada'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, usuario.email]
		email_mensaje = "<div>Hola</br><h1>xxx</h1></div>"
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)			

		return render(request, 'villonaco/message.html')	
		#form = PersonaForm(request.POST or None, request.FILES or None)

#Elige la habitacion a reservar por el cliente
def elegir_habitacion(request):
	if request.method == "POST":
		fechaEntrada = datetime.datetime.strptime(request.POST["check-in"], "%Y-%m-%d").date()
		fechaSalida = datetime.datetime.strptime(request.POST["check-out"], "%Y-%m-%d").date()
		lista = TipoHabitacion.objects.all()
		dias = request.POST["duration"]
		tipos = []
		#nros = []
		i = 0
		for obj in lista:
			listaReserva = Reserva.objects.filter(estado=1).filter(fecha_entrada__range = [fechaEntrada,fechaSalida]).filter(fecha_salida__range = [fechaEntrada,fechaSalida])
			for objRes in listaReserva:
				detalle = DetalleReserva.objects.get(reserva=objRes)
				if detalle.id_tipohabitacion == obj.id_tipohabitacion:
					i = i+1
			##aux0 = DetalleReserva.objects.filter(id_tipohabitacion = )
			#aux = Reserva.objects.filter(fecha_entrada__range = [fechaEntrada,fechaSalida]).filter(estado=1).count()
			#aux2 = Reserva.objects.filter(fecha_salida__range = [fechaEntrada,fechaSalida]).filter(estado=1).count()
			
			nro = Habitacion.objects.filter(tipohabitacion=obj).count()
			nro = nro-i
			#nros.append(nro)
			tipos.append((obj, nro, range(1, (obj.nro_personas+1)), range(0,obj.nro_personas+1)))
			i = 0
			#tipo = TipoHabitacion.objects.get(nombre_tipo=obj.nombre_tipo)
				
		#tiposimple = TipoHabitacion.objects.get(nombre_tipo="Simple")
		#nroSimple = Habitacion.objects.filter(tipohabitacion=tiposimple).count()
		return render(request, 'villonaco/booking-1.html', {
			"tipos" : tipos,
			"fechaEntrada" : request.POST["check-in"],
			"fechaSalida" : request.POST["check-out"],
			"duracion" : dias })

#ESTA FUNCION ES PARA IMPRIMIR REPORTE
# -*- coding: utf-8 -*-
from io import BytesIO

from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

class IndexView(ListView):
    template_name = "index.html"
    model = Persona
    model = Factura
    context_object_name = "c"

@staff_member_required
def generar_pdf(request, pk):
	
    print "Genero el PDF"
    factura = Factura.objects.get(id_factura=pk)
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()

    ps = ParagraphStyle(
            name='Total',
            fontSize=12,
            fontName='Helvetica-BoldOblique',
            textColor=colors.darkblue,
            spaceBefore=0.5 * cm,
            alignment=TA_CENTER,
            spaceAfter=0.5 * cm)

    header = Paragraph("Factura", ps)
    blanco = Paragraph(" ", ps)

    aux = Persona.objects.get(id_persona=factura.id_persona)

	   
    clientes.append(header)
    
    cedula = Paragraph("Cedula: "+aux.cedula, styles['Heading5'])
    clientes.append(cedula)

    nombre = Paragraph("Cliente: "+aux.apellido+" "+aux.nombre, styles['Heading5'])
    clientes.append(nombre)
        

    direccion = Paragraph("Direccion: "+aux.direccion, styles['Heading5'])
    clientes.append(direccion)

    telefono = Paragraph("Telefono: "+aux.telefono, styles['Heading5'])
    clientes.append(telefono)

    clientes.append(blanco)

    headings = ('Cant', 'Descripcion', 'P/U', 'P/T')
    detalle = [(p.cantidad, p.habitacion.tipohabitacion.nombre_tipo, p.precio_uni, p.precio_total) for p in DetalleFactura.objects.filter(factura=factura)]
    #print detalle

    t = Table([headings] + detalle,colWidths=[2 * cm, 10 * cm, 2 * cm, 2 * cm])
    t.setStyle(TableStyle(
    [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
     ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
     ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
     ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))


    clientes.append(t)

    data = [
    ["","","Subtotal:",str(factura.subtotal)],
    ["","","Iva:",str(factura.iva)],
    ["","","Total:",str(factura.total)]
    ]
    t1 = Table(data,colWidths=[2 * cm, 10 * cm, 2 * cm, 2 * cm])
    #t1.setStyle(TableStyle(
    #[('INNERGRID', (0, 2), (-2, -3), 0.25, colors.black),
    # ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
    # ('VALIGN', (0, 0), (-1, 0), 'MIDDLE')]))
    clientes.append(t1)

    doc.build(clientes)
    response.write(buff.getvalue())
    telefono = Paragraph("Telefono: "+aux.telefono, styles['Heading5'])
    clientes.append(telefono)
    buff.close()

    return response