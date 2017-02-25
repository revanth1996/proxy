from django.shortcuts import render
from .forms import UploadFileForm,ClassPhotoForm
from .models import Photos,StudentPhoto,ClassPhoto
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from supervisors.mixins import SupervisorDomainMixin
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here.

class UploadPhoto(View):
	template_name = 'upload.html'

	def get(self, request):
		print 'Upload a photo'
		form = UploadFileForm()
		return render(request,self.template_name,{'form' : form })

	def post(self, request, **kwargs):
		form = UploadFileForm(request.POST, request.FILES)
		user_name = "admin"
		if form.is_valid():
			print 'valid form'
			name = request.POST['title']
			image = request.FILES['image']
			instance = Photos(name = name, pic= image)
			instance.save()
			print "image saved"
			print instance.pic.url	
			response = cloudinary.uploader.upload(instance.pic.url)
			url = response['url']	
			instance = StudentPhoto(user_name = user_name,url=url)
			instance.save()
			# Account creation is successful. Now we need to add the first user
			# to this account. This user will also be the admin of the account.
			return HttpResponse("Added Successfully!")

		else:
			messages.errors = form.errors
			messages.error(request, 'Invalid fields')
			print messages.errors
			print "Invalid form"

			return HttpResponse("Invalid Form!")

		return redirect("/login/")

class UploadClassPhotos(View):

	template_name = "class_upload.html"

	def get(self, request):
		print 'Upload a class photo'
		form = ClassPhotoForm()
		return render(request,self.template_name,{'form' : form })

	def post(self, request, **kwargs):
		form = ClassPhotoForm(request.POST, request.FILES)
		course_name = "cs3300_2017"
		if form.is_valid():
			print 'valid form'
			course = request.POST['course']
			date = request.POST['date']
			image = request.FILES['image']
			# files = request.FILES.getlist('file_field')
			instance = Photos(name = course, pic= image)
			instance.save()
			print "image saved"
			print instance.pic.url	
			response = cloudinary.uploader.upload(instance.pic.url)
			url = response['url']

			instance = ClassPhoto(course = course,date = date, url = url)
			instance.save()	

			# Account creation is successful. Now we need to add the first user
			# to this account. This user will also be the admin of the account.
			return HttpResponse("Added Successfully!")

		else:
			messages.errors = form.errors
			messages.error(request, 'Invalid fields')
			print messages.errors
			print "Invalid form"

			return HttpResponse("Invalid Form!")

		return redirect("/login/")
