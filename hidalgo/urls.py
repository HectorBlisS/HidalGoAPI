from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
# My apps
from projects import urls as projectsURL
from account import urls as accURL
from capturista import urls as capturaUrls

urlpatterns = [
	url(r'^projects/',include(projectsURL,namespace="projects")),
	url(r'^account/',include(accURL)),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$',
        	serve, {
        		'document_root': settings.MEDIA_ROOT}),
    url(r'^',include(capturaUrls,namespace="captura")),
]
