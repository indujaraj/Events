from django.urls import path

from awsapp import views

urlpatterns=[
    path('home',views.CreateEvent.as_view(),name='create')
]