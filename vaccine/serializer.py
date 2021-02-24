from rest_framework import serializers
from .models import VaccineType,Vaccine
from hospital.serializer import HospitalSerializer


class VaccineTypeSerializer(serializers.ModelSerializer):
	vaccines  		=		serializers.HyperlinkedIdentityField(view_name="vaccine:vaccines",lookup_field="id")
	class Meta:
		model 	=	VaccineType
		fields 	=	"__all__"



class VaccineSerializer(serializers.ModelSerializer):
	vaccine_name    =		VaccineTypeSerializer()
	hospital 		=		HospitalSerializer()
	class Meta:
		model 	=	Vaccine
		fields 	=	"__all__"