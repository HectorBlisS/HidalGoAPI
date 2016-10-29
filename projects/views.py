from django.shortcuts import get_object_or_404, HttpResponse
from django.http import HttpResponseBadRequest
from .models import Project,Category
from django.core import serializers
from django.views.generic import View
from django.utils.text import slugify
# from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator

# from django.contrib.auth.decorators import login_required

import json
# from django.forms.models import model_to_dict


from .forms import ProjectForm

class ProjectListView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ProjectListView, self).dispatch(request, *args, **kwargs)

	@method_decorator(ensure_csrf_cookie)
	def get(self, request):
		# paginate = request.GET.get('paginate')
		user_id = request.GET.get('user_id')
		if(user_id):
			projects = Project.objects.filter(uid=user_id)
			data = serializers.serialize('json',projects,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)

			return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
		else:
			projects = Project.objects.all().filter(cerrado=True)
			# if paginate:
		# 	projects = projects[:int(paginate)]

		data = serializers.serialize('json',projects,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		# print(category)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
	
	def post(self,request):
		try:

			form = ProjectForm(request.POST,request.FILES)
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




class FiltroView(View):
	def get(self,request,id):
		ejes = {
		'1':'Gobierno Honesto, Cercano y Moderno',
		'2':'Hidalgo Próspero y Dinámico',
		'3':'Hidalgo Humano e Igualitario',
		'4':'Un Hidalgo Seguro con Justicia y en Paz',
		'5':'Un Hidalgo Con Desarrollo Sustentable'
		}
		try:
			projects = Project.objects.all().filter(eje=ejes[id],cerrado=True)
			data = serializers.serialize('json',projects,indent=2,
				use_natural_foreign_keys=True, use_natural_primary_keys=False)
			# print(category)
			return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
		except:
			return HttpResponseBadRequest('No encontrado')		




class ProjectDetailView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ProjectDetailView, self).dispatch(request, *args, **kwargs)

	def get(self,request,id):
		# id=request.GET.get('id')
		# template_name="projects/detail.html"
		# print('estas en detail')
		try:
			project = get_object_or_404(Project,pk=id)
		except:
			return HttpResponse('No encontrado')
		# cosa = list(Category.objects.all())+[project]
		data = serializers.serialize('json',[project],indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		# projects = request.user.projects.all()
		# form = ProjectForm(instance=project)
		# context = {
		# 'form':form,
		# 'num_projects':projects.count()

		# }
		# print(data)
		# return render(request,template_name,context)
		
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')

	def post(self,request,id):
		try:
			project = get_object_or_404(Project,id=id)
			form = ProjectForm(data=request.POST,files=request.FILES,instance=project)
			if form.is_valid():
				pro = form.save(commit=False)
				if pro.img:
					pro.imagen = 'http://planestataldedesarrollo.hidalgo.gob.mx:8000'+str(pro.img.url)
				if pro.anexo:
					pro.archivo = 'http://planestataldedesarrollo.hidalgo.gob.mx:8000'+str(pro.anexo.url)
				pro.save()
				# messages.success(request,"Proyecto guardado con éxito")
				return HttpResponse('Guardado con exito')
			return HttpResponseBadRequest('Formulario no valido, no se guardó')
		except:
			return HttpResponseBadRequest('Error, no se guardó')
			# pass
		# return redirect('projects:detail', id=id)



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
		










