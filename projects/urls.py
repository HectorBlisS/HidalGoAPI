from django.conf.urls import url
from . import views


urlpatterns = [
#Niños
	url(r'^ninos/$',
		views.Ninos.as_view(),
		name="ninos"),
#niños detalle

#listing the count of totals

	url(r'^totales/$',
		views.Cuentas.as_view(),
		name="totales"),

#Listing adn Create Category
	url(r'^categories/$',
		views.CategoryListView.as_view(),
			name="category_list"),

#Detail Project
	url(r'^(?P<id>\d+)/$',
		views.ProjectDetailView.as_view(),
			name="detail"),
#Listing and Create
	url(r'^filtro/(?P<id>\d+)/$',
		views.FiltroView.as_view(),
		name="filtro"),

	url(r'^$',
		views.ProjectListView.as_view(),
			name="list"),

#Listing adn Create Category
	url(r'^(?P<id>\d+)/reviews/$',
		views.Reviews.as_view(),
			name="reviews_list"),



]