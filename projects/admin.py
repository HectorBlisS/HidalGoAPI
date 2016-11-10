from django.contrib import admin
from .models import Project,Comment,Category, Conclusion

# import export
from import_export import resources
# from import_export.admin import ImportExportModelAdmin

# from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin


class ProjectAdmin(ImportExportActionModelAdmin, ImportExportMixin, admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ['id','title']
	list_filter = ['cerrado']
	search_fields = ['id','title','autor']

class ProjectResource(resources.ModelResource):
	class Meta:
		model = Project

class ConclusionResource(resources.ModelResource):
	class Meta:
		model = Conclusion

# class ProjectAdmin(ImportExportModelAdmin):
# 	# resource_class = ProjectResource
# 	pass



admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Conclusion)

