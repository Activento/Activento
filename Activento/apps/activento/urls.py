from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import index,user,registrarse,crearCategoria,listarCategorias,listarUsuario


urlpatterns = [
	url(r'^$', index.as_view(), name="inicio"),
	url(r'^user$', user.as_view(), name="user"),
	url(r'^registrarse$', registrarse.as_view(), name="registrarse"),
	url(r'^crearCategoria$', crearCategoria.as_view(), name="crearCategoria"),
	url(r'^crearCategoria$', crearCategoria.as_view(), name="crearCategoria"),
	url(r'^listarCategorias$', listarCategorias.as_view(), name="listarCategorias"),
	url(r'^listarUsuario$', listarUsuario.as_view(), name="listarUsuario"),
	url(r'^siguiendo/$', views.siguiendo, name="siguiendo"),
	url(r'^listarSiguiendo/$', views.listarSiguiendo, name="listarSiguiendo"),

]
