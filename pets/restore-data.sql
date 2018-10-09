--
-- DUMP DATOS
--

COPY public.cities_city (id, code, name, search_name, lat, lon, state_id) FROM stdin;
1	1	Pasto	pasto	1.23324319999999998	3.45345345000000004	1
\.


COPY public.cities_state (id, code, name, abbr) FROM stdin;
1	1	Nariño	NA
\.

COPY public.meupet_kind (id, kind, slug) FROM stdin;
1	Canino	canino
2	Felino	felino
\.

COPY public.meupet_statusgroup (id, slug, name) FROM stdin;
1	adopcion	Adopción
2	extravio	Extravío
3	otros	Otros
\.

COPY public.meupet_petstatus (id, code, description, final, group_id, next_status_id) FROM stdin;
1	Adoptada	Mascota adoptada	t	1	\N
2	Adopción	Mascota para adopción	f	1	1
3	Encontrada	Mascota encontrada	t	2	\N
4	Extraviada	Mascota Extraviada	t	1	3
\.

COPY public.users_fundacion (id, tipo_identificacion, num_identificacion, nombre_corto, razon_social, descripcion, fecha_fundacion, email, telefono, direccion, logo, facebook, twitter) FROM stdin;
1	NIT	901034058-1	PAZ ANIMAL	Paz animal tiene como objeto el albergue, rescate, rehabilitación y dar en adopción a animales de compañía de especies caninos, felinos y bovinos.	En Paz Animal podrás disfrutar el descubrir grandes amigos.	2015-10-04 18:17:08-05	pazanimal@gmail.com	312 233 23 23	Cra 23 #16A-88 Santiago	fundacion_profiles/Logo-fundacion-Final-02.jpg	\N	\N
\.

COPY public.users_ownerprofile (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, rol, tipo_identificacion, num_identificacion, is_information_confirmed, facebook, phone, direccion, firma, foto, fundacion) FROM stdin;
2	pbkdf2_sha256$100000$mbaInrzesFn5$Y74C1rIvmlpeF9jtdEDbfloS0I6JsUUAgbqG6ggXcGk=	2018-10-04 18:45:56.130612-05	f	snknft	Omar José	Lopez Trejo	omar@gmail.com	f	t	2018-10-04 18:27:30.521995-05	1	CC	1087987543	t	\N	3157627522	\N			1
\.