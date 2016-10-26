from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View 
from projects.forms import ProjectForm, EditProyectForm
from projects.forms import ProfileForm
from django.contrib import messages
from projects.models import Project

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import FilesForm


class Alta(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'capturista/home.html'
		projects = request.user.projects.all()
		form = FilesForm()
		context = {
			'section':'alta',
			'num_projects':projects.count(),
			'form':form
		}
		return render(request,template_name,context)

	def post(self,request):
		projects = request.user.projects.all()
		template_name = 'capturista/home.html'
		# Capturamos los datos
		np = Project()
		np.user = request.user
		np.foro = request.POST.get('foro')
		np.eje = request.POST.get('eje')
		if request.POST.get('eje2'):
			np.eje = request.POST.get('eje2')
		np.problematica = request.POST.get('problematica')
		np.alcance = request.POST.get('alcance')
		np.municipio = request.POST.get('municipio')
		np.title = request.POST.get('titulo')
		np.objetivo_general = request.POST.get('objetivo')
		np.planteamiento = request.POST.get('planteamiento')
		np.indicador = request.POST.get('indicador')
		if request.POST.get('indicador2'):
			np.indicador = request.POST.get('indicador2')
		np.save()
		form = FilesForm(request.POST,request.FILES,instance=np)
		form.save()
		if np.img:
			np.imagen = np.img.url
		if np.anexo:
			np.archivo = np.anexo.url
		np.save()

		context = {
			'section':'alta',
			'num_projects':projects.count(),
			'guardado':True,
			'np_id':np.id
		}
		return render(request,template_name,context)


class Revisar(View):
	def get(self,request,id):
		project = get_object_or_404(Project,id=id)
		form = EditProyectForm(instance=project)
		template_name="capturista/editar.html"
		context = {
			'project':project,
			'form':form
		}
		return render(request,template_name,context)

	def post(self,request,id):
		project = get_object_or_404(Project,id=id)
		form = EditProyectForm(request.POST,request.FILES,instance=project)
		if form.is_valid():
			pro = form.save(commit=False)
			if pro.img:
				pro.imagen = "http://planestataldedesarrollo.hidalgo.gob.mx"+pro.img.url 
			pro.save()
			messages.success(request,'Proyecto editado y guardado con éxito')
			return redirect('captura:editar',id=id)
		else:
			template_name="capturista/editar.html"
			context = {
				'form':form
			}
			return render(request,template_name,context)


class Lista(View):
	def get(self,request):
		projects = Project.objects.all()
		num_projects_all = projects.count()
		num_projects = request.user.projects.all()
		template_name = "capturista/lista.html"
		context = {
		'section':'lista',
		'projects':projects,
		'num_projects':num_projects.count(),
		'num_projects_all':num_projects_all
		}
		return render(request,template_name,context)
		