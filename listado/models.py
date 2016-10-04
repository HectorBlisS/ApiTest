from django.db import models


class Alumno(models.Model):
	first_name=models.CharField(max_length=140,null=True,blank=True)
	last_name=models.CharField(max_length=140,null=True,blank=True)
	email=models.CharField(max_length=140,null=True,blank=True)
	twitter=models.CharField(max_length=140,null=True,blank=True)

	def __str__(self):
		if not self.first_name:
			return "Secured"
		return self.first_name
