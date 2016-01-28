"""FaceMashAnything URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from facemash.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^facemash/', include('facemash.urls')),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^logout/$', logout_page),
]
