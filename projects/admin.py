from django.contrib import admin
from .models import Project,Comment,Category

# import export
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProjectAdmin(ImportExportModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ['id','title']

class ProjectResource(resources.ModelResource):
	class Meta:
		model = Project

# class ProjectAdmin(ImportExportModelAdmin):
# 	# resource_class = ProjectResource
# 	pass



admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Category)

