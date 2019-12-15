from django.conf.urls import url, include
from . import views

urlpatterns = [
    #Pagina Informativa
    url(r'^$', views.mostrar_inicio),
    url(r'^quienes_somos/$', views.mostrar_quienes_somos, name = 'quienes_somos'),
    url(r'^habitaciones/$', views.mostrar_habitaciones, name = 'habitaciones'),
    url(r'^galeria/$', views.mostrar_galeria, name = 'galeria'),
    url(r'^contactos/$', views.mostrar_contactos, name = 'contactos'),
    # url(r'^detalle_simple/$', views.mostrar_detallesimple, name = 'detalle_simple'),
    # url(r'^detalle_doble/$', views.mostrar_detalledoble, name = 'detalle_doble'),
    # url(r'^detalle_triple/$', views.mostrar_detalletriple, name = 'detalle_triple'),
    url(r'^registrarse/$', views.registrarse, name = 'registrarse'),
    
   

    # urls administration
    url(r'^administracion/$', views.mostrar_administracion, name = 'administracion'),
    url(r'^administracion/lista_usuarios/$', views.listar_usuarios, name = 'lista_usuarios'),
    url(r'^administracion/lista_clientes/$', views.listar_clientes, name = 'lista_clientes'),
    url(r'^administracion/lista_habitaciones/$', views.listar_habitaciones, name = 'lista_habitaciones'),
    url(r'^administracion/lista_tipohabitaciones/$', views.listar_tipohabitaciones, name = 'lista_tipohabitaciones'),
    url(r'^administracion/lista_servicios/$', views.listar_servicios, name = 'lista_servicios'),
    url(r'^administracion/lista_reservas/$', views.listar_reservas, name = 'lista_reservas'),
    url(r'^administracion/lista_facturas/$', views.listar_facturas, name = 'lista_facturas'),
    url(r'^administracion/configuracion/$', views.listar_galeria, name = 'configuracion'),
    url(r'^administracion/crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),
    # url(r'^administracion/crear_cliente/$', views.crear_cliente, name = 'crear_cliente'),
    url(r'^administracion/crear_habitacion/$', views.crear_habitacion, name = 'crear_habitacion'),
    url(r'^administracion/crear_tipohabitacion/$', views.crear_tipohabitacion, name = 'crear_tipohabitacion'),
    url(r'^administracion/crear_servicio/$', views.crear_servicio, name = 'crear_servicio'),
    url(r'^administracion/crear_reserva_admin/$', views.crear_reserva_admin, name = 'crear_reserva'),
    url(r'^administracion/crear_factura/$', views.crear_factura, name = 'crear_factura'),
    url(r'^administracion/modificar_cliente/$', views.modificar_cliente, name = 'modificar_cliente'),
    url(r'^administracion/modificar_usuario/$', views.modificar_usuario, name = 'modificar_usuario'),
    url(r'^administracion/modificar_servicio/$', views.modificar_servicio, name = 'modificar_servicio'),
    url(r'^administracion/modificar_habitacion/$', views.modificar_habitacion, name = 'modificar_habitacion'),
    url(r'^administracion/modificar_tipohabitacion/$', views.modificar_tipohabitacion, name = 'modificar_tipohabitacion'),
    url(r'^administracion/disponibilidad_admin/$', views.mostrar_disponibilidad_admin, name = 'disponibilidad_admin'),
    url(r'^administracion/registrar_reserva_admin/$', views.registrar_reserva_admin, name = 'registrar_reserva_admin'),
    url(r'^administracion/registrar_factura/$', views.registrar_factura, name = 'registrar_factura'),
    url(r'^administracion/detalle_reserva/(?P<pk>\d+)$', views.detalle_reserva, name = 'detalle_reserva'),
    url(r'^administracion/levantar_factura/(?P<pk>\d+)$', views.levantar_factura, name = 'levantar'),
    url(r'^administracion/pdf/(?P<pk>\d+)$', views.generar_pdf, name = 'pdf'),
    url(r'^administracion/obtener_cliente/(?P<pk>\d+)$', views.obtener_cliente, name = 'obtener_cliente'),
    url(r'^administracion/obtener_usuario/(?P<pk>\d+)$', views.obtener_usuario, name = 'obtener_usuario'),
    url(r'^administracion/obtener_servicio/(?P<pk>\d+)$', views.obtener_servicio, name = 'obtener_servicio'),
    url(r'^administracion/obtener_habitacion/(?P<pk>\d+)$', views.obtener_habitacion, name = 'obtener_habitacion'),
    url(r'^administracion/obtener_tipohabitacion/(?P<pk>\d+)$', views.obtener_tipohabitacion, name = 'obtener_tipohabitacion'), 
   
    # urls reservacion
    url(r'^disponibilidad/$', views.mostrar_disponibilidad, name = 'disponibilidad'),
    url(r'^mensaje/$', views.registrar_reserva, name = 'mensaje'),
    url(r'^habitacion/$', views.elegir_habitacion, name = 'habitacion'),
    url(r'^registrar_reserva/$', views.registrar_reserva, name = 'registrar_reserva'),
    # url(r'^message/$', views.message, name = 'message'),


]

