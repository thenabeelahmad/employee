from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^login/',views.Lin,name='login'),
	url(r'^logout/',views.Lout,name='Lout'),
	url(r'^signup/',views.Sup,name='signup'),
]   
