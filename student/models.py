from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Queries(models.Model):
	studentID = models.CharField(max_length=100)
	courseID = models.CharField(max_length=100)
	query = models.CharField(max_length=1000)
	date = models.DateField(("Date"), default=datetime.date.today)

	def __str__(self):
		return self.studentID+"||"+self.courseID+"||"+self.date