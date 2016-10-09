from django.conf.urls import url
from . import views


urlpatterns = [

#Detail Project
	url(r'^(?P<id>\d+)$',
		views.ProjectDetailView.as_view(),
			name="detail"),
#Listing		
	url(r'^',
		views.ProjectListView.as_view(),
			name="list"),

]