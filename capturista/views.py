from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View 
from projects.forms import ProjectForm, EditProyectForm
from projects.forms import ProfileForm
from django.contrib import messages
from projects.models import Project

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class Alta(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'capturista/home.html'
		projects_all = Project.objects.all().count()
		projects = request.user.projects.all()
		form = ProjectForm();
		form2 = ProfileForm();
		context = {
			'section':'alta',
			'form':form,
			'form2':form2,
			'num_projects':projects.count(),
			'num_projects_all':projects_all

		}
		return render(request,template_name,context)

	def post(self,request):
		var = '';
		form = ProjectForm(request.POST,request.FILES)
		form2 = ProfileForm(request.POST, request.FILES)
		projects = request.user.projects.all()
		projects_all = Project.objects.all().count()
		template_name = 'capturista/home.html'
		if form.is_valid():
			pro = form.save(commit=False)
			pro.user = request.user
			if pro.img:
				pro.imagen = "http://planestataldedesarrollo.hidalgo.gob.mx"+pro.img.url
			pro.save()
			messages.success(request,"Proyecto guardado con éxito")
			context = {
				'section':'alta',
				'num_projects':projects.count(),
				'num_projects_all':projects_all
			}
			
			
		else:
			context = {
			'section':'alta',
			'form':form,
			'form2':form2,
			'num_projects':projects.count(),
			'num_projects_all':projects_all
			}
			return render(request,template_name,context)

		if form2.is_valid():
			perf = form2.save(commit=False)
			perf.uid = pro.uid
			perf.save()
			return redirect('captura:alta')


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
		
