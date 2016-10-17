from django.shortcuts import render, redirect
from django.views.generic import View
from projects.forms import ProjectForm
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class Alta(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'capturista/home.html'
		form = ProjectForm();
		context = {
			'section':'alta',
			'form':form
		}
		return render(request,template_name,context)

	def post(self,request):
		form = ProjectForm(request.POST,request.FILES)
		template_name = 'capturista/home.html'
		if form.is_valid():
			pro = form.save(commit=False)
			pro.user = request.user
			pro.save()
			
		else:
			context = {
			'section':'alta',
			'form':form
			}
			return render(request,template_name,context)
		messages.success(request,"Proyecto guardado con éxito")
		return redirect('captura:alta')
