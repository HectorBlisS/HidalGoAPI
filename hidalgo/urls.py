from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
# My apps
from projects import urls as projectsURL
from accounts import urls as accURL

urlpatterns = [
	url(r'^projects/',include(projectsURL,namespace="projects")),
	url(r'users/',include(accURL,namespace="users")),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$',
        	serve, {
        		'document_root': settings.MEDIA_ROOT})
]
