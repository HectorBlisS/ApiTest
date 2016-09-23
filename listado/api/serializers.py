from rest_framework import serializers
from ..models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ('id','first_name','last_name','email','twitter')