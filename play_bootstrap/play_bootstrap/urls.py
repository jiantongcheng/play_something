"""play_bootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app1 import views as app1_views

urlpatterns = [
    url(r'^$', app1_views.django),
    
    url(r'^play_bootstrap$', app1_views.bootstrap),
    url(r'^play_vue$', app1_views.vue),
    url(r'^play_django$', app1_views.django),

    url(r'^admin/', admin.site.urls),

    url(r'^t_url/(\d+)/(\d+)/$', app1_views.tt_url, name='test_url'),
    url(r'^play_django/get_test$', app1_views.get_test),
]
