from django.conf.urls import url
from . import views



urlpatterns = [
#User detail
	url(r'^(?P<id>\d+)/$',
		views.UserDetailView.as_view(),
		name="detail"),
#User list
	url(r'^',
		views.UsersListView.as_view(),
		name="list"),


]