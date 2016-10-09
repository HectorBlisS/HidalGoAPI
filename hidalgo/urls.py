from django.conf.urls import url,include
from django.contrib import admin
from projects import urls as projectsURL
from django.conf import settings
from django.views.static import serve


urlpatterns = [
	url(r'^projects/',include(projectsURL,namespace="projects")),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$',
        	serve, {
        		'document_root': settings.MEDIA_ROOT})
]
