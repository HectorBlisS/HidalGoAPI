from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^(?P<id>\d+)/$', views.Revisar.as_view(), name="editar"),
	url(r'^listado/$',views.Lista.as_view(), name="lista"),
	url(r'^todos/$',views.Todos.as_view(),name="todos"),
	url(r'^$', views.Alta.as_view(),name="alta"),
]