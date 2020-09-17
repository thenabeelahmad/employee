from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^cremp/$',views.cremp,name='create'),
    url(r'^cremp2/$',views.cremp2,name='create2'),
	url(r'^listemp/$',views.listemp,name='list'),
	url(r'^update/(?P<pk>[\d]+)',views.update,name='update'),
	url(r'^update/done/(?P<pk>[\d]+)',views.update2,name='update2'),
	url(r'^confdel/(?P<pk>[\d]+)',views.confdel,name='confdel'),
	url(r'^delete/(?P<pk>[\d]+)',views.delete,name='delete'),
 ]   
