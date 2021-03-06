from rest_framework import serializers
from .models import Appointment
from authentication.serializer import SubUserSerializer
from vaccine.serializer import VaccineSerializer


class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model 				=		Appointment
		fields 				=		"__all__"
		read_only_fields 	=		['appointment_id']


class AppointmentListSerializer(serializers.ModelSerializer):
	patient 		=		SubUserSerializer()
	vaccine 		=		VaccineSerializer()
	class Meta:
		model 				=		Appointment
		fields 				=		"__all__"