from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^alumnos/',views.Listado.as_view(),name="list"),
]