"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about,name='about'),
    url(r'^$',views.home,name='home'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^service/',views.service,name='service'),
    url(r'^information/',include('information.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^post/',include('post.urls')),
    
	
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)