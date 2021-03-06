from django import forms
from models import *
import datetime

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadProfilePicFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))

class ClassPhotoForm(forms.Form):
	#course = forms.CharField(max_length=50)
	#date = forms.DateField(initial=datetime.date.today)
	image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))