from __future__ import unicode_literals


import datetime

from django.db import models




class Person(models.Model):
	CATEGORIES = (  
    ('Female', 'Female'),
    ('Male', 'Male')
)
	username=models.CharField(max_length=120,unique=True)
	First_name=models.CharField(max_length=120,default='')
	Last_name=models.CharField(max_length=120,default='')
	sex=models.CharField(max_length=10,choices=CATEGORIES)
	birthdate=models.DateField(null=True,blank=True)
	profilepic=models.ImageField(blank=True,null=True)
	coverpic=models.ImageField(blank=True,null=True,default='')
	


	def __str__(self):
		return str(self.username)



class Post(models.Model):
	person =models.CharField(max_length=120)
	post=models.TextField(default='',null=True,blank=True)
	image=models.FileField(null=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True ,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False ,auto_now=True)
	like=models.IntegerField(default=0)

	def __str__(self):
		return str(self.timestamp)



class Addrequest(models.Model):
	person=models.CharField(max_length=120)
	requests=models.CharField(max_length=120)

	def __str__(self):
		return self.requests

	

class Connection(models.Model):
	user=models.CharField(max_length=120)
	friend=models.CharField(max_length=120)


	def __str__(self):
		return str(self.friend)



class LikePost(models.Model):
	post_id=models.PositiveIntegerField()
	person=models.CharField(max_length=120,null=True)
	

	def __str__(self):
		return str(self.post_id)

class CommentPost(models.Model):
	post_id=models.PositiveIntegerField(default=0)
	person=models.CharField(max_length=120,null=False)
	person_id=models.PositiveIntegerField(default=0)
	comment=models.TextField()

	def __str__(self):
		return self.comment


class LoginDetail(models.Model):
	person=models.CharField(max_length=120)
	lastlogin=models.DateTimeField(auto_now_add=False,auto_now=True)
	ipaddress=models.CharField(max_length=19)

	def __str__(self):
		return self.ipaddress

