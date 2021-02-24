from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializer import VaccineTypeSerializer,VaccineSerializer
from .models import VaccineType,Vaccine

# Create your views here.



class VaccineTypeListCreateAPIVIew(generics.ListCreateAPIView):
	authentication_classses 		=	[]
	permission_classes    			=	[]
	serializer_class 				=	VaccineTypeSerializer
	queryset 						=	VaccineType.objects.all()


class VaccinesOfHospitalsAPIView(generics.GenericAPIView):
	queryset           =		Vaccine.objects.all()
	def get(self,request,id=None):
		vaccine_name    =		VaccineType.objects.get(id=id)
		query  			=		Vaccine.objects.filter(vaccine_name=vaccine_name)
		serialize 		=		VaccineSerializer(query,context={'request': request},many=True)
		return Response(serialize.data)
