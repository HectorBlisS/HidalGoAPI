from django.shortcuts import render, redirect
from django.views.generic import View 
from projects.forms import ProjectForm
from projects.forms import ProfileForm
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class Alta(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'capturista/home.html'
		projects = request.user.projects.all()
		form = ProjectForm();
		form2 = ProfileForm();
		context = {
			'section':'alta',
			'form':form,
			'form2':form2,
			'num_projects':projects.count()

		}
		return render(request,template_name,context)

	def post(self,request):
		var = '';
		form = ProjectForm(request.POST,request.FILES)
		form2 = ProfileForm(request.POST, request.FILES)
		projects = request.user.projects.all()
		template_name = 'capturista/home.html'
		if form.is_valid():
			pro = form.save(commit=False)
			pro.user = request.user
			pro.imagen = "http://hidalgo.fixter.org"+pro.img.url
			pro.save()
			messages.success(request,"Proyecto guardado con éxito")
			context = {
				'section':'alta',
				'num_projects':projects.count()
			}
			
			
		else:
			context = {
			'section':'alta',
			'form':form,
			'form2':form2,
			'num_projects':projects.count()
			}
			return render(request,template_name,context)

		if form2.is_valid():
			perf = form2.save(commit=False)
			perf.uid = pro.uid
			perf.save()
			return redirect('projects:detail',id=pro.id)

		
