from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schoolsPage/<int:pk>', views.schoolsPage, name='schoolsPage'),
    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('professorLogin', views.professorLogin, name='professorLogin'),
    path('studentPage/<studentOIB>', views.studentPage, name='studentPage'),
    path('professorPage/<professorOIB>', views.professorPage, name='professorPage'),
    path('api', views.apiList.as_view(), name='apiList'),
    path('api/<int:pk>', views.apiDetail.as_view(), name='apiDetail'),


]