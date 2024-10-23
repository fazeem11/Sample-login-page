from django.urls import  path
from .import views
urlpatterns=[
    path('jijimiss/',views.jijimiss,name='jijimiss')
]