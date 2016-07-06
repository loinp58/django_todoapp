from django.conf.urls import url

from . import views

app_name="todo"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create', views.create, name="create"),
    url(r'^store', views.store, name="store"),
    url(r'^destroy', views.destroy, name="destroy"),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name="edit"),
    url(r'^update/(?P<id>[0-9]+)/$', views.update, name="update"),
]