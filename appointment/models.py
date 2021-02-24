from django.db import models
from authentication.models import SubUser
from vaccine.models import Vaccine
from django.contrib.auth import get_user_model
# Create your models here.


User 	=	get_user_model()


class Appointment(models.Model):
	user 				=		models.ForeignKey(User,on_delete=models.CASCADE)
	patient  			=		models.ForeignKey(SubUser,on_delete=models.CASCADE)
	vaccine 			=		models.ForeignKey(Vaccine,on_delete=models.CASCADE)
	appoitment_date 	=		models.DateField()

	def __str__(self):
		return F'{self.patient}'


