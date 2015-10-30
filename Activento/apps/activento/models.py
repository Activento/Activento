from django.db import models


# Create your models here.



class Usuario(models.Model):
	nombre = models.CharField(max_length=50,primary_key=True)
	password = models.CharField(max_length=50)


	def __unicode__(self):
		return self.nombre

class Sigue(models.Model):
	seguir = models.ManyToManyField(Usuario)
	seguido = models.ManyToManyField(Usuario, related_name='seguido')

	def __unicode_(self):
		return self.seguir



class Categoria(models.Model):
	nombre = models.CharField(max_length=50,primary_key=True)
	descripcion = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre	


class Pertenece(models.Model):
	nombre_usu = models.ManyToManyField(Usuario)
	nombre_cate = models.ManyToManyField(Categoria)

	def __unicode__(self):
		return self.nombre_usu	
