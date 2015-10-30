from django.conf.urls import include, url
from .views import index,user,registrarse,crearCategoria,listarCategorias,listarUsuario,siguiendo,listarSiguiendo


urlpatterns = [
	url(r'^$', index.as_view(), name="inicio"),
	url(r'^user$', user.as_view(), name="user"),
	url(r'^registrarse$', registrarse.as_view(), name="registrarse"),
	url(r'^crearCategoria$', crearCategoria.as_view(), name="crearCategoria"),
	url(r'^crearCategoria$', crearCategoria.as_view(), name="crearCategoria"),
	url(r'^listarCategorias$', listarCategorias.as_view(), name="listarCategorias"),
	url(r'^listarUsuario$', listarUsuario.as_view(), name="listarUsuario"),
	url(r'^siguiendo$', siguiendo.as_view(), name="siguiendo"),
	url(r'^listarSiguiendo$', listarSiguiendo.as_view(), name="listarSiguiendo"),

]
