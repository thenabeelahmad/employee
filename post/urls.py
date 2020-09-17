from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addpost/',views.addpost,name="addp"),
    url(r'^allpost',views.allpost,name="alp"),
    url(r'^updatepost/(?P<pk1>[\d]+)',views.updatepost1,name='uppost1'),
	url(r'^updatepost/done/(?P<pk1>[\d]+)',views.updatepost2,name='uppost2'),
	url(r'^delconf/(?P<pk1>[\d]+)',views.delconf,name='delconf'),
	url(r'^deletepost/(?P<pk1>[\d]+)',views.deletepost,name='deletepost'),
	
]
