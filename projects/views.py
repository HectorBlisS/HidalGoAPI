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


from .forms import ProjectForm

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

			form = ProjectForm(request.POST)
			if form.is_valid():
				form.save()

		# 	#convertimos los bytes que llegan de angular en diccionario
			# test1 = request.body.decode("utf-8") 
			# test2 = json.loads(test1)

			# new_project = Project()
			# new_project.title = test2['title']
			# new_project.eje = test2['eje']
			# # new_project.user = get_object_or_404(User,username="bliss")
			# new_project.uid = test2['uid']
			# new_project.save()
			return HttpResponse('Guardado con Exito')
		except:
			return HttpResponseBadRequest('No se guardo')


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



	def post(self,request,id):

		form = ProjectForm(request.POST,request.FILES)

		if form.is_valid():
			form.save()

		try:
			# form = ProjectForm(request.POST, request.FILES)
			# # cd = form.cleaned_data
			# print(form)
			# form.save()

		# # test1 = request.body.decode("utf-8") 
		# # data = json.loads(test1)
		# # print(test2['objetivo_general'])
		# print(request.POST.get('objetivo_general'))
		# print(request.POST.get('file'))
		# print(request.FILES)
		# # print(request.POST)
		# try:


		# 	project = get_object_or_404(Project,pk=id)

		# 	# project.title = test2['title']
		# 	# project.uid = test2['uid']
		# 	# project.eje = test2['eje']
		# 	# project.slug = slugify(project.title)
		# 	# # project.img = test2['img']
		# 	# project.objetivo_general = test2['objetivo_general']
			
		# 	project.objetivo_general = request.POST.get('objetivo_general')

		# 	project.indicador = request.POST.get('indicador')
		# 	project.planteamiento = request.POST.get('planteamiento')
		# 	project.problematica = request.POST.get('problematica')
		# 	project.municipio = request.POST.get('municipio')
		# 	# project.img = request.FILES
		# 	# print(request.FILES)

		# 	# project.votes = request.POST.get('votes')
		# 	# project.categories = request.POST.get('categories')
		# 	# project.anexo = test2['anexo']
		# 	project.save()


			return HttpResponse('Guarado con éxito!')
		except:
			return HttpResponseBadRequest('No Guardado')


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









