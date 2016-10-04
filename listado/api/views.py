from rest_framework import generics
from ..models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import authentication, permissions

class Listado(generics.ListCreateAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer
	authentication_classes = (authentication.TokenAuthentication,)