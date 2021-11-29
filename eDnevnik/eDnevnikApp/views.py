from django.shortcuts import redirect,render
import requests
from .models import Student
from .models import Studentsubjecttable
from .models import Professor
from .models import Subject
from .models import School
from eDnevnikApp.serializers import SchoolSerializer
from eDnevnikApp.serializers import StudentSerializer
from eDnevnikApp.serializers import SubjectSerializer
from eDnevnikApp.serializers import StudentsubjecttableSerializer
from eDnevnikApp.serializers import ProfessorSerializer

import urllib, json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



def index(request): 

    #url = "http://10.30.10.55:5000/schools"
    #"http://127.0.0.1:8000/apiStudent/12312312312?format=json"
    #response = urllib.request.urlopen(url)
    #data = json.loads(response.read())
    data = 1
    
    #data = requests.delete('http://127.0.0.1:8000/apiSchool/2')
    
    payload  = {'schoolname':'65','adress':'69','website':'69'}
    data = requests.post("http://127.0.0.1:8000/apiSchool", data=payload)


    context = {'data':data}
    return render(request, 'eDnevnikApp/index.html',context)

def studentLogin(request):
    
    if request.method == 'POST':
        if Student.objects.filter(studentoib = request.POST.get('OIB')).exists():
            return redirect('studentPage/'+ request.POST.get('OIB'))
        else:
            context = { 'alert' : 1}
            return render(request, 'eDnevnikApp/studentLogin.html',context) 
    return render(request, 'eDnevnikApp/studentLogin.html')

def professorLogin(request):
    
    if request.method == 'POST':
        if Professor.objects.filter(professoroib = request.POST.get('OIB')).exists():
            return redirect('professorPage/'+ request.POST.get('OIB'))
        else:
            context = { 'alert' : 1}
            return render(request, 'eDnevnikApp/professorLogin.html',context) 
    
    return render(request, 'eDnevnikApp/professorLogin.html')

def studentPage(request,studentOIB):  
    studentByOib = Student.objects.get(pk=studentOIB)
    studentsSubject = Studentsubjecttable.objects.filter(fkstudentoib=studentOIB)
    context = {'studentByOib': studentByOib, 'studentsSubject': studentsSubject}
    return render(request, 'eDnevnikApp/studentPage.html',context)

def professorPage(request,professorOIB):
    professorsByOib = Professor.objects.get(pk=professorOIB)
    teachersSubjects = Subject.objects.filter(taughtbyfkprofessoroib=professorOIB)
    context = {'teachersSubjects': teachersSubjects, 'professorsByOib': professorsByOib}
    return render(request, 'eDnevnikApp/professorPage.html',context)

def schoolsPage(request,pk):
    schoolById = School.objects.get(pk=pk)
    context = {'schoolById': schoolById}

    return render(request, 'eDnevnikApp/schoolsPage.html',context)


def professorSubjectView(request,professorOIB,subject):
    context = {'professorOIB':professorOIB,'subject':subject}
    return render(request, 'eDnevnikApp/professorSubjectView.html',context)



class apiSchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
class apiSchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class apiStudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class apiStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class apiStudentsubjecttableList(generics.ListCreateAPIView):
    queryset = Studentsubjecttable.objects.all()
    serializer_class = StudentsubjecttableSerializer
class apiStudentsubjecttableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Studentsubjecttable.objects.all()
    serializer_class = StudentsubjecttableSerializer

class apiProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
class apiProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class apiSubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
class apiSubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


#add https://www.django-rest-framework.org/tutorial/2-requests-and-responses/ 
# +++ https://www.geeksforgeeks.org/put-method-python-requests/

@api_view(['GET', 'POST'])
def schoolList(request):
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def schoolDetail(request, pk):
    try:
        school = School.objects.get(pk=pk)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)