from django.contrib import admin
from .models import Profile

from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin


class ProfileAdmin(ImportExportActionModelAdmin, ImportExportMixin, admin.ModelAdmin):
	# prepopulated_fields = {'slug':('title',)}
	list_display = ['id','name','edad','email']
	list_filter = ['edad']
	search_fields = ['id','name','email']


admin.site.register(Profile, ProfileAdmin)