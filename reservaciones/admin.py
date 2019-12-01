# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Persona
from .models import Reserva
from .models import Galeria
from .models import DetalleReserva
from .models import Factura
from .models import DetalleFactura
from .models import Habitacion
from .models import TipoHabitacion
from .models import Servicio
from .models import Registrado
from .forms import RegModelForm

# Register your models here.

admin.site.register(Persona)
admin.site.register(Reserva)
admin.site.register(Galeria)
admin.site.register(DetalleReserva)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(Habitacion)
admin.site.register(TipoHabitacion)
admin.site.register(Servicio)


class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	form = RegModelForm
	# list_display_links = ["nombre"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email", "nombre"]
	# class Meta:
	# 	model = Registrado


admin.site.register(Registrado, AdminRegistrado)