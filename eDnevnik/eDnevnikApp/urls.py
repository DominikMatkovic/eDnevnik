from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schoolsPage/<int:pk>', views.schoolsPage, name='schoolsPage'),
    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('professorLogin', views.professorLogin, name='professorLogin'),
    path('studentPage/<studentOIB>', views.studentPage, name='studentPage'),
    path('professorPage/<professorOIB>', views.professorPage, name='professorPage'),
    path('professorPage/<professorOIB>/<subject>', views.professorSubjectView, name='professorSubjectView'),
    


    path('apiStudent', views.apiStudentList.as_view(), name='apiStudentList'),
    path('apiStudent/<pk>', views.apiStudentDetail.as_view(), name='apiStudentDetail'),
    path('apiProfessor', views.apiProfessorList.as_view(), name='apiProfessorList'),
    path('apiProfessor/<pk>', views.apiProfessorDetail.as_view(), name='apiProfessorDetail'),  
    path('apiSchool', views.apiSchoolList.as_view(), name='apiSchoolList'),
    path('apiSchool/<int:pk>', views.apiSchoolDetail.as_view(), name='apiSchoolDetail'),
    path('apiSTT', views.apiStudentsubjecttableList.as_view(), name='apiStudentsubjecttableList'),
    path('apiSTT/<int:pk>', views.apiStudentsubjecttableDetail.as_view(), name='apiStudentsubjecttableDetail'),
    path('apiSubject', views.apiSubjectList.as_view(), name='apiSubjectList'),
    path('apiSubject/<int:pk>', views.apiSubjectDetail.as_view(), name='apiSubjectDetail'),

    path('schools', views.schoolList, name='schoolList'),
    path('schools/<int:pk>/', views.schoolDetail, name='schoolDetail'),



]