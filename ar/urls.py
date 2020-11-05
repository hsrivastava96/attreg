from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from ar import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^db_handle/$', views.db_handle, name='db_handle'),
]