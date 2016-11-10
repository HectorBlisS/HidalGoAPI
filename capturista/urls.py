from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^conclusiones/$',views.Conclusiones.as_view(),name="conclusiones"),
	url(r'^conclusiones/export/$', views.ConcExport.as_view(),name="export_conclusiones"),
	url(r'^(?P<id>\d+)/$', views.Revisar.as_view(), name="editar"),
	url(r'^listado/$',views.Lista.as_view(), name="lista"),
	url(r'^todos/$',views.Todos.as_view(),name="todos"),
	url(r'^borrar/(?P<id>\d+)/$',views.Borrar.as_view(),name="delete"),
	url(r'^export/(?P<id>\d+)/$', views.Exportar.as_view(),name="export"),
	url(r'^$', views.Alta.as_view(),name="alta"),
]