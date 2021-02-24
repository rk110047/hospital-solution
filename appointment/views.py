from django.shortcuts import render
from rest_framework.response import Response
from .serializer import AppointmentSerializer,AppointmentListSerializer
from .models import Appointment
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication

# Create your views here.


class AppointMentCreateAPIView(generics.CreateAPIView):
	queryset 			=		Appointment.objects.all()
	serializer_class 	=		AppointmentSerializer


	def perform_create(self,serializer):
		user 	=	self.request.user
		serializer.save(user=user)


class AppointMentListAPIView(generics.GenericAPIView):
	authentication_classses 		=	[SessionAuthentication,TokenAuthentication]
	permission_classes    			=	[]
	queryset 			=		Appointment.objects.all()
	serializer_class 	=		AppointmentListSerializer

	def get(self,request):
		user 		=		self.request.user
		query 		= 		Appointment.objects.filter(user=user)
		serialize   =		AppointmentListSerializer(query,many=True,context={'request': request})
		return Response(serialize.data)

