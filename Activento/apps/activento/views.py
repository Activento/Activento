from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,ListView
from django.template import RequestContext, loader
from .models import Usuario,Categoria,Sigue,Pertenece
from django.core.urlresolvers import reverse_lazy


# Create your views here.


class index(CreateView):
	template_name = 'activento/index.html'
	model = Usuario
	fields = ['nombre','password']
"""
	def post(self, request, *args, **kwargs):
		nombre_empresa = request.POST['nombre']
		password = request.POST['password']

		if Usuario.objects.filter(nombre=nombre_empresa):
			usu = Usuario.objects.get(nombre=nombre_empresa)
			if usu.password==password:
				salida="Bienvenido "+nombre_empresa
				request.session["usuario"] = nombre_empresa
			else:
				salida="Error al introducir usuario o contrasenia"

		else:
			salida="Error al introducir usuario o contrasenia"


		return render(request,'activento/index.html',{'salida':salida})
"""
class user(ListView):
	template_name = 'activento/user.html'
	model = Usuario
	#fields = ['nombre','calificacion']
	success_url = reverse_lazy('inicio')

	def post(self, request, *args, **kwargs):
		nombre_empresa = request.POST['nombre']
		password = request.POST['password']


		if Usuario.objects.filter(nombre=nombre_empresa):
			usu = Usuario.objects.get(nombre=nombre_empresa)
			if usu.password==password:
				salida="Bienvenido "+nombre_empresa
				request.session["usuario"] = nombre_empresa
			else:
				salida="Error al introducir usuario o contrasenia"

		else:
			salida="Error al introducir usuario o contrasenia"


		return render(request,'activento/user.html',{'salida':salida})



class registrarse(CreateView):
	template_name = 'activento/registrarse.html'
	model = Usuario
	fields = ['nombre','password']
	#success_url = reverse_lazy('inicio')

	def post(self, request, *args, **kwargs):
		nombre_usuario = request.POST['nombre']
		password = request.POST['password']
		password2 = request.POST['password2']

		if Usuario.objects.filter(nombre=nombre_usuario) :
			salida= "Error al introducir usuario o las contrasenias no coinciden"

		else:
			if password == password2 and len(password)>5:
				usu = Usuario(nombre=nombre_usuario,password=password)
				usu.save()
				salida= "Registrado"
			else:
				salida= "Error al introducir usuario o las contrasenas no coinciden"



		return render(request,'activento/registrarse.html',{'salida':salida})





class crearCategoria(CreateView):
	template_name = 'activento/crearCategoria.html'
	model = Categoria
	fields = ['nombre','descripcion']
	#success_url = reverse_lazy('inicio')

	def post(self, request, *args, **kwargs):
		nombre = request.POST['nombre']
		descripcion = request.POST['descripcion']

		if Categoria.objects.filter(nombre=nombre) :
			salida= "La categoria "+nombre+" ya existe."

		else:
			cat = Categoria(nombre=nombre,descripcion=descripcion)
			cat.save()
			salida= "Categoria "+nombre+" creada."



		return render(request,'activento/registrarse.html',{'salida':salida})



class listarCategorias(ListView):
	template_name = 'activento/listarCategorias.html'
	model = Categoria

	def get(self, request, *args, **kwargs):
		usuario_activo=request.session["usuario"]
		usus = Categoria.objects.all()

		return render(request,'activento/listarCategorias.html',{'usuario_activo':usuario_activo,'usuarios':usus})



class listarUsuario(ListView):
	template_name = 'activento/listarUsuario.html'
	model = Usuario


	def get(self, request, *args, **kwargs):
		usuario_activo=request.session["usuario"]
		usus = Usuario.objects.exclude(nombre=usuario_activo)


		return render(request,'activento/listarUsuario.html',{'usuario_activo':usuario_activo,'usuarios':usus})


def siguiendo(request):
	context = RequestContext(request, {'duplicado':True,})
	template = loader.get_template('activento/siguiendo.html')
	if request.method=="POST":
		if request.POST.get('usu_seg'):
			usuario_activo=request.session["usuario"]
			nombre=request.POST.get('usu_seg')
			if Sigue.objects.filter(seguir=str(usuario_activo),seguido=str(nombre)):
				return HttpResponse(template.render(context))
			else:
				usuario1=Usuario.objects.get(nombre=str(usuario_activo))

				usuario2=Usuario.objects.get(nombre=str(nombre))
				sigue=Sigue(seguir=usuario1,seguido=usuario2)
				sigue.save()
				template = loader.get_template('activento/siguiendo.html')
	        	context = RequestContext(request, {'usuario': str(sigue.seguir),'seguido': str(sigue.seguido),})
	return HttpResponse(template.render(context))






def listarSiguiendo(request):
	template = loader.get_template('activento/listarSiguiendo.html')
	if request.method=="GET":
		lista_seguidores=Sigue.objects.filter(seguir=request.session["usuario"])
		context = RequestContext(request, {'lista_seguidores':lista_seguidores})
		return HttpResponse(template.render(context))
	if request.method=="POST":
		usuario_seguido=Usuario.objects.get(nombre=str(request.POST.get('dseg')))
		Sigue.objects.get(seguido=usuario_seguido).delete()
		lista_seguidores=Sigue.objects.filter(seguir=request.session["usuario"])
		context = RequestContext(request, {'lista_seguidores':lista_seguidores})
		return HttpResponse(template.render(context))
