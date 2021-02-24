from django.urls import path
from .views import VaccineTypeListCreateAPIVIew,VaccinesOfHospitalsAPIView


app_name="vaccine"

urlpatterns=[
	path('vaccine-types/',VaccineTypeListCreateAPIVIew.as_view(),name='vaccine-types'),
	path('vaccines/<id>/',VaccinesOfHospitalsAPIView.as_view(),name='vaccines')

]