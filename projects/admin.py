from django.contrib import admin
from .models import Project,Comment,Category


class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ['id','title']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Category)

