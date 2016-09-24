from rest_framework import generics
from ..models import Alumno
from .serializers import AlumnoSerializer

class Listado(generics.ListCreateAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer