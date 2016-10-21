from django.conf.urls import url
from . import views

# Django views
from django.contrib.auth import views as djangoViews



urlpatterns = [
#User detail
	# url(r'^(?P<id>\d+)/$',
	# 	views.UserDetailView.as_view(),
	# 	name="detail"),
#User list
	# url(r'^',
	# 	views.UsersListView.as_view(),
	# 	name="list"),
	url(r'^profile/$',
		views.GetProfile.as_view(),
		name="get_profile"),
	
	url(r'^save/$',
		views.SaveProfile.as_view(),
		name="save_profile"),

	url(r'^login/$',
		djangoViews.login,
		name="login"),

	url(r'^logout/$',
		djangoViews.logout,
		name="logout"),

	url(r'^$',
		views.Dashboard.as_view(),
		name="dashboard")


]