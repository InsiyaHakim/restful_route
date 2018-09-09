from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^user$', views.index,name="index"),
    url(r'^user/new$', views.new,name="new"),
    url(r'^user/create$', views.create,name="create"),
    url(r'^user/(?P<user_id>\d+)/$', views.show,name="show"),
    url(r'^user/(?P<user_id>\d+)/destroy/$', views.delete,name="delete"),
    url(r'^user/(?P<user_id>\d+)/edit/$', views.edit,name="edit"),
    url(r'^user/(?P<user_id>\d+)/update/$', views.update,name="update"),
]