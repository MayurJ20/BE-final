from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('options/', views.options, name='options'),
    path('prediction/', views.prediction, name='prediction'),
    path('monitor/', views.monitor, name='monitor'),
    path('apple/', views.apple, name='apple'),
    path('upload/', views.im_upload, name='im_upload'),
]