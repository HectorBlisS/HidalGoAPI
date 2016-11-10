from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.views.generic import View 
from projects.forms import ProjectForm, EditProyectForm
from projects.forms import ProfileForm, ConclusionForm
from django.contrib import messages
from projects.models import Project, Conclusion
from account.models import Profile

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import FilesForm

from django.contrib.admin.views.decorators import staff_member_required


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
		url = 'http://planestataldedesarrollo.hidalgo.gob.mx:8000'
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
		if not request.POST.get('titulo'):
			messages.error(request,"Debes poner un titulo al proyecto")
			return redirect('captura:alta')
		np.title = request.POST.get('titulo')
		np.objetivo_general = request.POST.get('objetivo')
		np.planteamiento = request.POST.get('planteamiento')
		np.indicador = request.POST.get('indicador')
		np.autor_name = request.POST.get('autor_name')
		np.autor_tel = request.POST.get('autor_tel')
		np.autor_correo = request.POST.get('autor_correo')
		np.agree = request.POST.get('agree')
		np.conclusiones = request.POST.get('conclusiones')

		if request.POST.get('indicador2'):
			np.indicador = request.POST.get('indicador2')
		np.save()
		form = FilesForm(request.POST,request.FILES,instance=np)
		form.save()
		if np.img:
			np.imagen = url+np.img.url
		if np.anexo:
			np.archivo = url+np.anexo.url
		np.save()
		# Checamos si es un eje nuevo
		if request.POST.get('justificacion_eje') or request.POST.get('justificacion_indicador'):
			np.justi_eje = request.POST.get('justificacion_eje')
			np.justi_indicador = request.POST.get('justificacion_indicador')
			np.save()
		if request.POST.get('publicar'):
			np.cerrado = True
			np.save()

		context = {
			'section':'alta',
			'num_projects':projects.count(),
			'guardado':True,
			'np_id':np.id
		}
		return render(request,template_name,context)





class Revisar(View):
	@method_decorator(staff_member_required)
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
			if request.POST.get('cerrado'):
				pro.cerrado = True
				pro.save()
			if request.POST.get('abierto'):
				pro.cerrado = False
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

class Todos(View):
	def get(self,request):
		projects = Project.objects.all()
		ejes = {
		'1':'Gobierno Honesto, Cercano y Moderno',
		'2':'Hidalgo Próspero y Dinámico',
		'3':'Hidalgo Humano e Igualitario',
		'4':'Un Hidalgo Seguro con Justicia y en Paz',
		'5':'Un Hidalgo Con Desarrollo Sustentable'
		}
		foros = {
			'1':'No',
			'2':'Huejutla',
			'3':'Pachuca',
			'4':'Tulancingo',
			'5':'Ixmiquilpan',
			'6':'Tula'
		}
		cuenta_ejes = {
		'ghcm':Project.objects.all().filter(eje=ejes['1']).count(),
		'hpd':Project.objects.all().filter(eje=ejes['2']).count(),
		'hhi':Project.objects.all().filter(eje=ejes['3']).count(),
		'hsjp':Project.objects.all().filter(eje=ejes['4']).count(),
		'hds':Project.objects.all().filter(eje=ejes['5']).count()
		}
		cuenta_foros = {
		'Online':Project.objects.all().filter(foro="").count(),
		'Huejutla':Project.objects.all().filter(foro=foros['2']).count(),
		'Pachuca':Project.objects.all().filter(foro=foros['3']).count(),
		'Tulancingo':Project.objects.all().filter(foro=foros['4']).count(),
		'Ixmiquilpan':Project.objects.all().filter(foro=foros['5']).count(),
		'Tula':Project.objects.all().filter(foro=foros['6']).count()
		}
		template_name = "capturista/todos.html"
		context = {
		'projects':projects,
		'published':Project.objects.all().filter(cerrado=True).count(),
		'incomplete':Project.objects.all().filter(cerrado=False).count(),
		'totalp':Project.objects.all().count(),
		'ejes':cuenta_ejes,
		'foros':cuenta_foros
		}
		return render(request,template_name,context)

	def post(self, request):
		perfiles = Profile.objects.all()
		proyectos = Project.objects.all()
		for proyecto in proyectos:
			for perfil in perfiles:
				if proyecto.uid == perfil.uid:
					proyecto.autor_name = perfil.name
					proyecto.autor_correo = perfil.email
					proyecto.autor_tel = perfil.telefono
					proyecto.save()
		return HttpResponse('Terminé')

from django.contrib.admin.views.decorators import staff_member_required
class Borrar(View):
	@method_decorator(staff_member_required)
	def get(self,request,id):
		project = get_object_or_404(Project,id=id)
		project.delete()
		return redirect('dashboard')

from projects.admin import ProjectResource
# from import_export.instance_loaders import ModelInstanceLoader
class Exportar(View):
	def get(self,request,id):
		# project = get_object_or_404(Project,id=id)
		dataset = ProjectResource().export()
		# ejemplo = ModelInstanceLoader(project,dataset="xlsx")
		response = HttpResponse(dataset.csv,content_type='application/csv')
		# response = HttpResponse(ejemplo,content_type='application/xlsx')
		response['Content-Disposition'] = 'attachment; filename=proyectos.csv'
		return response


class Conclusiones(View):
	def get(self,request):
		form  = ConclusionForm()
		conc = Conclusion.objects.all()
		template_name = 'capturista/conclusion.html'
		context = {
			'form':form,
			'conclusiones':conc
		}
		return render(request,template_name,context)

	def post(self,request):
		form = ConclusionForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Tu conclusión se ha guardado con éxito. GRACIAS.')
			return redirect('captura:conclusiones')

from projects.admin import ConclusionResource
class ConcExport(View):
	def get(self,request):
		#Exportar el modelo
		dataset = ConclusionResource().export()
		response = HttpResponse(dataset.csv,content_type='application/csv')
		response['Content-Disposition'] = 'attachment; filename=conclusiones.csv'
		return response








		