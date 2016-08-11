from django.db import models
from userprofile.models import User


class Post(models.Model):
	user_name = models.ForeignKey('userprofile.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=140) 
	body = models.TextField()
	date = models.DateTimeField()
	def __str__(self):
		# return self.user_name
		return self.title
	# class Meta:
	# 	ordering = ('title')
