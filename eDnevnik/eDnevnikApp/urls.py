from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('professorLogin', views.professorLogin, name='professorLogin'),
    path('studentPage/<studentOIB>', views.studentPage, name='studentPage'),
    path('professorPage/<professorOIB>', views.professorPage, name='professorPage'),
]