from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Project,Comment,Category 
from django.core import serializers
from django.views.generic import View




class ProjectListView(View):
	def get(self, request):
		category = request.GET.get('category')
		paginate = request.GET.get('paginate')
		try:
			projects = Category.objects.get(name=category).projects.all()
		except:
			projects = Project.objects.all()
		if paginate:
			projects = projects[:int(paginate)]

		data = serializers.serialize('json',projects)
		print(category)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')


class ProjectDetailView(View):
	def get(self,request,id):
		id=request.GET.get('id')
		print('estas en detail')
		try:
			project = get_object_or_404(Project,pk=id)
		except:
			return HttpResponse('No encontrado')
		data = serializers.serialize('json',[project])
		print(data)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
