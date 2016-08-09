from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	user_name = models.CharField(max_length=25)
	email_add = models.CharField(max_length=25)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.user_name
		# return "%s %s" % (self.first_name, self.last_name)