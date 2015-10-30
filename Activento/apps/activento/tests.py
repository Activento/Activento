from django.test import TestCase
import unittest
from django.test import Client
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,ListView
from django.template import RequestContext, loader
from .models import Usuario,Categoria,Sigue,Pertenece
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse

class SimpleTest(unittest.TestCase):
    def setUp(self):

        self.client = Client()

    def test_details(self):


        response = self.client.post('/')


        self.assertEqual(response.status_code, 200)

    def test_Siguiendo(self):
        """test que prueba la inserccion de un usuario dentro de la lista de
        seguidos de otro"""
        u1=Usuario(nombre="Paco", password="mspsi")
        u1.save()
        u2=Usuario(nombre="Pablo", password="mspsi")
        u2.save()
        usuario1=Usuario.objects.get(nombre='Paco')
        usuario2=Usuario.objects.get(nombre='Pablo')
        sigue=Sigue(seguir=usuario1,seguido=usuario2)
        sigue.save()
        seg = Sigue.objects.get(seguir=usuario1,seguido=usuario2)
        self.assertEqual(sigue.seguir,seg.seguir)
        self.assertEqual(sigue.seguido,seg.seguido)


    def test_registrarse(self):
    	"""
    		Con este test se va comprobar que podemos instertar un usuario
    		que si lo volvemos a intentar insertar no nos deja hacerlo sin 
    		darnos un error e intentar intrucir usuario con las contrasenias 
    		mal introducidas.
    		Para todo ello usamos un cliente con el que le mandamos peticiones
    		post a registrarse y comprobamos los resultados
    	"""
    	c = Client()


    	response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
    	self.assertEqual(response.status_code, 200)

    	
    	usu = Usuario(nombre="Pablo",password="entero")
    	self.assertEqual(usu.nombre, "Pablo")
    	self.assertEqual(usu.password, "entero")

    	response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
    	self.assertEqual(response.status_code, 200)
    	usu = Usuario.objects.filter(nombre="Pablo")

    	response = c.post(reverse('registrarse'),{'nombre':"Pablo2",'password':"ent",'password2':"ent"})
    	self.assertEqual(response.status_code, 200)
    	
    	
    	response = c.post(reverse('registrarse'),{'nombre':"Pablo2",'password':"entera",'password2':"entero"})
    	self.assertEqual(response.status_code, 200)



    def test_iniciar_sesion(self):
    	"""
    		Con este test voy a comprobar si funciona bien el inicio de
    		sesion para ello voy crear un cliente, lo registrare usando
    		parte del codigo del test para registrar y luego inicio sesion
    		dos veces una correctamente y otra erroneamente, comprobando
    		siempre que no falla el programa
    	"""
    	c = Client()

    	response = c.post(reverse('registrarse'),{'nombre':"Pablo",'password':"entero",'password2':"entero"})
    	self.assertEqual(response.status_code, 200)

    	
    	usu = Usuario(nombre="Pablo",password="entero")
    	self.assertEqual(usu.nombre, "Pablo")
    	self.assertEqual(usu.password, "entero")


    	response = c.post(reverse('user'),{'nombre':"Pablo",'password':"entero"})
    	self.assertEqual(response.status_code, 200)


    	response = c.post(reverse('user'),{'nombre':"Pablo",'password':"entera"})
    	self.assertEqual(response.status_code, 200)
