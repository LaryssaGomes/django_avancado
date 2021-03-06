"""django_avancado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from stock.views import entries_list, entries_create, entries_new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stock_entries/$', entries_list, name='entries_list'),
    url(r'^stock_entries/new/$', entries_new, name='entries_new'),
    url(r'^stock_entries/create/$', entries_create, name='entries_create')
]