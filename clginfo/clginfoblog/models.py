from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255,default="CIRS")
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	body = models.TextField()

	def __str__(self):
		return self.title + ' | ' + str(self.author) 

class College(models.Model):

	clg_name = models.CharField(max_length = 255)
	course_id = models.IntegerField()
	course = models.TextField(max_length=255)
	region = models.TextField(max_length=6)
	fees = models.IntegerField()
	clg_type = models.TextField(max_length=255)
	
class Contact(models.Model):
	name = models.CharField(max_length=15) 
	contact = models.EmailField()
	query = models.TextField()

