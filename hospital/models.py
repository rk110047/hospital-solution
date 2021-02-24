from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class Hospital(models.Model):
	user 			=		models.ForeignKey(User,on_delete=models.CASCADE)
	name 			=		models.CharField(max_length=120)
	description 	=		models.TextField(max_length=1000)
	address 		=		models.CharField(max_length=200)
	timming 		=		models.CharField(max_length=120)


	def __str__(self):
		return self.name
