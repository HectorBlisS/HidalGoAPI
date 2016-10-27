import json
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponseBadRequest
from django.core import serializers
from django.views.generic import View
# from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Profile
from projects.models import Project
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
# from .forms import LoginForm


class Dashboard(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'account/home.html'
		projects_all = Project.objects.all().count()
		projects = request.user.projects.all()
		context = {
			'section':'dashboard',
			'projects':projects,
			'num_projects':projects.count(),
			'num_projects_all':projects_all
		}
		return render(request,template_name,context)



class SaveProfile(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(SaveProfile, self).dispatch(request, *args, **kwargs)

	def post(self,request):
		try:
			uid = request.POST.get('uid')
			profile = get_object_or_404(Profile,uid=uid)
			form = ProfileForm(request.POST,instance=profile)
			if form.is_valid():
				form.save()
				return HttpResponse('Guardado')
		except:
			form = ProfileForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse('Creado')


class GetProfile(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(GetProfile, self).dispatch(request, *args, **kwargs)

	def post(self,request):
		try:
			uid = request.POST.get('uid')
			profile = get_object_or_404(Profile,uid=uid)
			data = serializers.serialize('json',[profile],indent=2,
				use_natural_foreign_keys=True, use_natural_primary_keys=False)
			return HttpResponse(data,content_type = 'application/javascript; charset=utf8')
		except:
			return HttpResponseBadRequest('No se encontró')



from django.contrib.auth import logout
from django.contrib.auth.models import User
class ChangePass(View):
	def get(self, request):
		return render(request,'account/cambio.html')

	def post(self,request):
		pass1 = request.POST.get('pass1')
		pass2 = request.POST.get('pass2')
		user = get_object_or_404(User,id=request.user.id)
		print(user)
		if pass1 == pass2:
			try:
				user.set_password(pass2)
				user.save()
				logout(request)
				return redirect('captura:alta')
			except:
				return render(request,'account/cambio.html',{'error':True})
		else:
			return render(request,'account/cambio.html',{'error':True})




















class UsersListView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(UsersListView, self).dispatch(request, *args, **kwargs)

	def get(self,request):
		users = User.objects.all()
		# cosa = list(Category.objects.all())+[project]
		data = serializers.serialize('json',users,indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		print(data)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')

	def post(self,request):
		try:
		# 	#convertimos los bytes que llegan de angular en diccionario
			test1 = request.body.decode("utf-8") 
			test2 = json.loads(test1)
			print(test2['username'])
			new_user = User.objects.create_user(test2['username'], test2['email'], test2['password'])
			print(new_user)
			new_user.save()
			new_profile = Profile()
			new_profile.user = new_user
			new_profile.save()
		except:
			return HttpResponseBadRequest('No se guardo')
		return HttpResponse('Usuario Creado con Exito')


class UserDetailView(View):
	def get(self,request,id):

		try:
			isProfile = request.GET.get('isProfile')
			if isProfile:
				user = get_object_or_404(User,id=id)
				data = serializers.serialize('json',[user.profile],indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
				print(data)
				return HttpResponse(data,content_type = 'application/javascript; charset=utf8')

		except:
			pass

		try:
			user = get_object_or_404(User,id=id)
		except:
			return HttpResponseBadRequest('No encontrado U_U')
		data = serializers.serialize('json',[user],indent=2,
			use_natural_foreign_keys=True, use_natural_primary_keys=False)
		print(data)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8')




