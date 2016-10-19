from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.Alta.as_view(),name="alta")
]