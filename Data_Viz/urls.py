from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('afterform/', views.afterform, name='afterform')
]
