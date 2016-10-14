from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseBadRequest
from .models import Project,Comment,Category 
from django.core import serializers
from django.views.generic import View
from django.utils.text import slugify
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
from django.forms.models import model_to_dict

class ProjectListView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ProjectListView, self).dispatch(request, *args, **kwargs)


	def get(self, request):
		category = request.GET.get('category')
		# paginate = request.GET.get('paginate')
		user_id = request.GET.get('user_id')
		if(user_id):
			projects = Project.objects.filter(uid=user_id)
			data = serializers.serialize('json',projects,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)

			return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
		try:
			projects = Category.objects.get(name=category).projects.all()
		except:
			projects = Project.objects.all()
		# if paginate:
		# 	projects = projects[:int(paginate)]

		data = serializers.serialize('json',projects,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		print(category)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
	
	def post(self,request):
		try:
		# 	#convertimos los bytes que llegan de angular en diccionario
			test1 = request.body.decode("utf-8") 
			test2 = json.loads(test1)

			new_project = Project()
			new_project.title = test2['title']
			new_project.eje = test2['eje']
			# new_project.user = get_object_or_404(User,username="bliss")
			new_project.uid = test2['uid']
			new_project.save()
		except:
			return HttpResponseBadRequest('No se guardo')
		return HttpResponse('Guardado con Exito')


class ProjectDetailView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ProjectDetailView, self).dispatch(request, *args, **kwargs)


	def get(self,request,id):
		# id=request.GET.get('id')
		print('estas en detail')
		try:
			project = get_object_or_404(Project,pk=id)
		except:
			return HttpResponse('No encontrado')
		# cosa = list(Category.objects.all())+[project]
		data = serializers.serialize('json',[project],indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		print(data)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')



	def put(self,request,id):
		try:
			test1 = request.body.decode("utf-8") 
			test2 = json.loads(test1)

			project = get_object_or_404(Project,pk=id)

			# project.title = test2['title']
			# project.uid = test2['uid']
			# project.eje = test2['eje']
			# project.slug = slugify(project.title)
			# # project.img = test2['img']
			project.objetivo_general = test2['objetivo_general']
			# project.indicador = test2['indicador']
			# project.planteamiento = test2['planteamiento']
			# project.problematica = test2['problematica']
			# project.municipio = test2['municipio']
			# # project.votes = test2['votes']
			# # project.categories = test2['categories']
			# # project.anexo = test2['anexo']
			project.save()
			

			return HttpResponse('Guarado con éxito!')
		except:
			return HttpResponse('No Guardado')


class ProjectCreateView(View):
	def post(self,request):
		title = request.POST.get('title')
		try:
			Project.objects.create(
				title=title,
				slug = slugify(title),
				# user = request.POST.get('title'),
				# img = request.POST.get('title'),
				# desc = request.POST.get('title'),
				# votes = request.POST.get('title'),
				# categories = request.POST.get('title')
				)
		except:
			response =HttpResponseBadRequest("No se pudo guardar")
		return HttpResponse(response)


class CategoryListView(View):
	def get(self,request):
		categories = Category.objects.all()

		data = serializers.serialize('json',categories,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		print(data)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')

class Reviews(View):
	def get(self,request,id):
		try:
			project = get_object_or_404(Project,pk=id)
		except:
			return HttpResponseBadRequest("No encontrado")
		reviews = project.reviews.all()
		data = serializers.serialize('json',reviews,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		print(data)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
		














def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d









