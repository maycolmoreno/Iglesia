-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 03-11-2017 a las 16:54:38
-- Versión del servidor: 5.7.20-0ubuntu0.16.04.1
-- Versión de PHP: 7.0.22-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hotel`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add permission', 3, 'add_permission'),
(8, 'Can change permission', 3, 'change_permission'),
(9, 'Can delete permission', 3, 'delete_permission'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add registration profile', 7, 'add_registrationprofile'),
(20, 'Can change registration profile', 7, 'change_registrationprofile'),
(21, 'Can delete registration profile', 7, 'delete_registrationprofile'),
(22, 'Can add registrado', 8, 'add_registrado'),
(23, 'Can change registrado', 8, 'change_registrado'),
(24, 'Can delete registrado', 8, 'delete_registrado'),
(25, 'Can add detalle reserva', 9, 'add_detallereserva'),
(26, 'Can change detalle reserva', 9, 'change_detallereserva'),
(27, 'Can delete detalle reserva', 9, 'delete_detallereserva'),
(28, 'Can add servicio', 10, 'add_servicio'),
(29, 'Can change servicio', 10, 'change_servicio'),
(30, 'Can delete servicio', 10, 'delete_servicio'),
(31, 'Can add persona', 11, 'add_persona'),
(32, 'Can change persona', 11, 'change_persona'),
(33, 'Can delete persona', 11, 'delete_persona'),
(34, 'Can add detalle factura', 12, 'add_detallefactura'),
(35, 'Can change detalle factura', 12, 'change_detallefactura'),
(36, 'Can delete detalle factura', 12, 'delete_detallefactura'),
(37, 'Can add reserva', 13, 'add_reserva'),
(38, 'Can change reserva', 13, 'change_reserva'),
(39, 'Can delete reserva', 13, 'delete_reserva'),
(40, 'Can add galeria', 14, 'add_galeria'),
(41, 'Can change galeria', 14, 'change_galeria'),
(42, 'Can delete galeria', 14, 'delete_galeria'),
(43, 'Can add factura', 15, 'add_factura'),
(44, 'Can change factura', 15, 'change_factura'),
(45, 'Can delete factura', 15, 'delete_factura'),
(46, 'Can add tipo habitacion', 16, 'add_tipohabitacion'),
(47, 'Can change tipo habitacion', 16, 'change_tipohabitacion'),
(48, 'Can delete tipo habitacion', 16, 'delete_tipohabitacion'),
(49, 'Can add habitacion', 17, 'add_habitacion'),
(50, 'Can change habitacion', 17, 'change_habitacion'),
(51, 'Can delete habitacion', 17, 'delete_habitacion'),
(52, 'Can add usuario', 18, 'add_usuario'),
(53, 'Can change usuario', 18, 'change_usuario'),
(54, 'Can delete usuario', 18, 'delete_usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$36000$uiB0FdFQeEbs$aioP7RizHvjqMIVbnuFt9cVmqNegPRjPNkuoHM3bcy0=', '2017-11-03 21:50:08.834604', 1, 'administrador', '', '', 'lourdes.cueva96@gmail.com', 1, 1, '2017-11-03 21:48:53.610240');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2017-11-03 21:51:07.996594', '1', 'Doble', 1, '[{"added": {}}]', 16, 1),
(2, '2017-11-03 21:51:51.696607', '1', 'Instalaciones', 1, '[{"added": {}}]', 14, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'registration', 'registrationprofile'),
(12, 'reservaciones', 'detallefactura'),
(9, 'reservaciones', 'detallereserva'),
(15, 'reservaciones', 'factura'),
(14, 'reservaciones', 'galeria'),
(17, 'reservaciones', 'habitacion'),
(11, 'reservaciones', 'persona'),
(8, 'reservaciones', 'registrado'),
(13, 'reservaciones', 'reserva'),
(10, 'reservaciones', 'servicio'),
(16, 'reservaciones', 'tipohabitacion'),
(18, 'reservaciones', 'usuario'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2017-11-03 21:41:39.309239'),
(2, 'auth', '0001_initial', '2017-11-03 21:41:47.350813'),
(3, 'admin', '0001_initial', '2017-11-03 21:41:49.199069'),
(4, 'admin', '0002_logentry_remove_auto_add', '2017-11-03 21:41:49.334034'),
(5, 'contenttypes', '0002_remove_content_type_name', '2017-11-03 21:41:50.389905'),
(6, 'auth', '0002_alter_permission_name_max_length', '2017-11-03 21:41:50.503200'),
(7, 'auth', '0003_alter_user_email_max_length', '2017-11-03 21:41:50.915073'),
(8, 'auth', '0004_alter_user_username_opts', '2017-11-03 21:41:50.977414'),
(9, 'auth', '0005_alter_user_last_login_null', '2017-11-03 21:41:51.488094'),
(10, 'auth', '0006_require_contenttypes_0002', '2017-11-03 21:41:51.521811'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2017-11-03 21:41:51.573173'),
(12, 'auth', '0008_alter_user_username_max_length', '2017-11-03 21:41:51.913127'),
(13, 'registration', '0001_initial', '2017-11-03 21:41:53.001741'),
(14, 'reservaciones', '0001_initial', '2017-11-03 21:42:06.826339'),
(15, 'sessions', '0001_initial', '2017-11-03 21:42:07.333228');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('bs5rdyrm1a85kp437lxf2i4zheehe3bi', 'YTc2Y2U4ZTE1NzFjNTExNTdiZjA3NDFjMDE3ODkyMWY0OGJkZWVhZDp7Il9hdXRoX3VzZXJfaGFzaCI6ImZmZDA5ZTA4MWQzNGNlNzFhNzA1MDVjYmY0ZDI3OWFkZDdhOTZiYjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-11-17 21:50:08.947018');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registration_registrationprofile`
--

CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_detallefactura`
--

CREATE TABLE `reservaciones_detallefactura` (
  `id_detallefactura` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_uni` decimal(5,2) NOT NULL,
  `precio_total` decimal(7,2) NOT NULL,
  `cant_adultos` int(11) NOT NULL,
  `cant_ninos` int(11) NOT NULL,
  `factura_id` int(11) NOT NULL,
  `habitacion_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_detallereserva`
--

CREATE TABLE `reservaciones_detallereserva` (
  `id_detallereserva` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `descripcion` varchar(30) NOT NULL,
  `precio_uni` decimal(5,2) NOT NULL,
  `precio_total` decimal(7,2) NOT NULL,
  `cant_adultos` int(11) NOT NULL,
  `cant_ninos` int(11) NOT NULL,
  `id_tipohabitacion` int(11) NOT NULL,
  `reserva_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_factura`
--

CREATE TABLE `reservaciones_factura` (
  `id_factura` int(11) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `id_reserva` int(11) NOT NULL,
  `subtotal` decimal(7,2) NOT NULL,
  `iva` decimal(6,2) NOT NULL,
  `descuento` decimal(6,2) NOT NULL,
  `total` decimal(8,2) NOT NULL,
  `numero_factura` varchar(15) NOT NULL,
  `estado_factura` tinyint(1) NOT NULL,
  `id_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_galeria`
--

CREATE TABLE `reservaciones_galeria` (
  `id_galeria` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `nombre_imagen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `reservaciones_galeria`
--

INSERT INTO `reservaciones_galeria` (`id_galeria`, `imagen`, `nombre_imagen`) VALUES
(1, 'galeria/lobby2.jpg', 'Instalaciones');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_habitacion`
--

CREATE TABLE `reservaciones_habitacion` (
  `id_habitacion` int(11) NOT NULL,
  `numero_habitacion` int(11) NOT NULL,
  `piso_habitacion` int(11) NOT NULL,
  `estado_habitacion` varchar(50) NOT NULL,
  `tipohabitacion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_persona`
--

CREATE TABLE `reservaciones_persona` (
  `id_persona` int(11) NOT NULL,
  `cedula` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `nacionalidad` varchar(50) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_registrado`
--

CREATE TABLE `reservaciones_registrado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_reserva`
--

CREATE TABLE `reservaciones_reserva` (
  `id_reserva` int(11) NOT NULL,
  `fecha_reserva` date NOT NULL,
  `fecha_entrada` date NOT NULL,
  `fecha_salida` date NOT NULL,
  `dias` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  `abono` tinyint(1) NOT NULL,
  `total` decimal(8,2) NOT NULL,
  `persona_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_servicio`
--

CREATE TABLE `reservaciones_servicio` (
  `id_servicio` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `precio` decimal(7,2) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_tipohabitacion`
--

CREATE TABLE `reservaciones_tipohabitacion` (
  `id_tipohabitacion` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `nombre_tipo` varchar(100) NOT NULL,
  `precio_tipo` decimal(6,2) NOT NULL,
  `nro_personas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `reservaciones_tipohabitacion`
--

INSERT INTO `reservaciones_tipohabitacion` (`id_tipohabitacion`, `imagen`, `nombre_tipo`, `precio_tipo`, `nro_personas`) VALUES
(1, 'tiposHab/room.jpeg', 'Doble', '34.00', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_usuario`
--

CREATE TABLE `reservaciones_usuario` (
  `persona_ptr_id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `registration_registrationprofile`
--
ALTER TABLE `registration_registrationprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `reservaciones_detallefactura`
--
ALTER TABLE `reservaciones_detallefactura`
  ADD PRIMARY KEY (`id_detallefactura`),
  ADD KEY `reservaciones_detall_factura_id_110b31a9_fk_reservaci` (`factura_id`),
  ADD KEY `reservaciones_detall_habitacion_id_a4fd429c_fk_reservaci` (`habitacion_id`),
  ADD KEY `reservaciones_detall_servicio_id_8f475e27_fk_reservaci` (`servicio_id`);

--
-- Indices de la tabla `reservaciones_detallereserva`
--
ALTER TABLE `reservaciones_detallereserva`
  ADD PRIMARY KEY (`id_detallereserva`),
  ADD KEY `reservaciones_detall_reserva_id_fc80299c_fk_reservaci` (`reserva_id`);

--
-- Indices de la tabla `reservaciones_factura`
--
ALTER TABLE `reservaciones_factura`
  ADD PRIMARY KEY (`id_factura`);

--
-- Indices de la tabla `reservaciones_galeria`
--
ALTER TABLE `reservaciones_galeria`
  ADD PRIMARY KEY (`id_galeria`);

--
-- Indices de la tabla `reservaciones_habitacion`
--
ALTER TABLE `reservaciones_habitacion`
  ADD PRIMARY KEY (`id_habitacion`),
  ADD KEY `reservaciones_habita_tipohabitacion_id_2a80fbc9_fk_reservaci` (`tipohabitacion_id`);

--
-- Indices de la tabla `reservaciones_persona`
--
ALTER TABLE `reservaciones_persona`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indices de la tabla `reservaciones_registrado`
--
ALTER TABLE `reservaciones_registrado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `reservaciones_reserva`
--
ALTER TABLE `reservaciones_reserva`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `reservaciones_reserv_persona_id_7bf2de0c_fk_reservaci` (`persona_id`);

--
-- Indices de la tabla `reservaciones_servicio`
--
ALTER TABLE `reservaciones_servicio`
  ADD PRIMARY KEY (`id_servicio`);

--
-- Indices de la tabla `reservaciones_tipohabitacion`
--
ALTER TABLE `reservaciones_tipohabitacion`
  ADD PRIMARY KEY (`id_tipohabitacion`);

--
-- Indices de la tabla `reservaciones_usuario`
--
ALTER TABLE `reservaciones_usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `persona_ptr_id` (`persona_ptr_id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT de la tabla `registration_registrationprofile`
--
ALTER TABLE `registration_registrationprofile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_detallefactura`
--
ALTER TABLE `reservaciones_detallefactura`
  MODIFY `id_detallefactura` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_detallereserva`
--
ALTER TABLE `reservaciones_detallereserva`
  MODIFY `id_detallereserva` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_factura`
--
ALTER TABLE `reservaciones_factura`
  MODIFY `id_factura` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_galeria`
--
ALTER TABLE `reservaciones_galeria`
  MODIFY `id_galeria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `reservaciones_habitacion`
--
ALTER TABLE `reservaciones_habitacion`
  MODIFY `id_habitacion` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_persona`
--
ALTER TABLE `reservaciones_persona`
  MODIFY `id_persona` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_registrado`
--
ALTER TABLE `reservaciones_registrado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_reserva`
--
ALTER TABLE `reservaciones_reserva`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_servicio`
--
ALTER TABLE `reservaciones_servicio`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `reservaciones_tipohabitacion`
--
ALTER TABLE `reservaciones_tipohabitacion`
  MODIFY `id_tipohabitacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `reservaciones_usuario`
--
ALTER TABLE `reservaciones_usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `registration_registrationprofile`
--
ALTER TABLE `registration_registrationprofile`
  ADD CONSTRAINT `registration_registr_user_id_5fcbf725_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `reservaciones_detallefactura`
--
ALTER TABLE `reservaciones_detallefactura`
  ADD CONSTRAINT `reservaciones_detall_factura_id_110b31a9_fk_reservaci` FOREIGN KEY (`factura_id`) REFERENCES `reservaciones_factura` (`id_factura`),
  ADD CONSTRAINT `reservaciones_detall_habitacion_id_a4fd429c_fk_reservaci` FOREIGN KEY (`habitacion_id`) REFERENCES `reservaciones_habitacion` (`id_habitacion`),
  ADD CONSTRAINT `reservaciones_detall_servicio_id_8f475e27_fk_reservaci` FOREIGN KEY (`servicio_id`) REFERENCES `reservaciones_servicio` (`id_servicio`);

--
-- Filtros para la tabla `reservaciones_detallereserva`
--
ALTER TABLE `reservaciones_detallereserva`
  ADD CONSTRAINT `reservaciones_detall_reserva_id_fc80299c_fk_reservaci` FOREIGN KEY (`reserva_id`) REFERENCES `reservaciones_reserva` (`id_reserva`);

--
-- Filtros para la tabla `reservaciones_habitacion`
--
ALTER TABLE `reservaciones_habitacion`
  ADD CONSTRAINT `reservaciones_habita_tipohabitacion_id_2a80fbc9_fk_reservaci` FOREIGN KEY (`tipohabitacion_id`) REFERENCES `reservaciones_tipohabitacion` (`id_tipohabitacion`);

--
-- Filtros para la tabla `reservaciones_reserva`
--
ALTER TABLE `reservaciones_reserva`
  ADD CONSTRAINT `reservaciones_reserv_persona_id_7bf2de0c_fk_reservaci` FOREIGN KEY (`persona_id`) REFERENCES `reservaciones_persona` (`id_persona`);

--
-- Filtros para la tabla `reservaciones_usuario`
--
ALTER TABLE `reservaciones_usuario`
  ADD CONSTRAINT `reservaciones_usuari_persona_ptr_id_df84652b_fk_reservaci` FOREIGN KEY (`persona_ptr_id`) REFERENCES `reservaciones_persona` (`id_persona`),
  ADD CONSTRAINT `reservaciones_usuario_user_id_4cce1df9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
