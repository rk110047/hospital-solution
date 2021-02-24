from django.urls import path
from .views import AppointMentCreateAPIView,AppointMentListAPIView

urlpatterns=[
	path('create/',AppointMentCreateAPIView.as_view(),name='appointment-create'),
	path('list/',AppointMentListAPIView.as_view(),name='appointment-list')
]