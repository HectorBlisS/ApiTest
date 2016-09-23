from django.conf.urls import url, include
from django.contrib import admin
from listado.api import urls as listadoURLs


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(listadoURLs)),
]
