from django.shortcuts import redirect,render

from .models import Student
from .models import Studentsubjecttable
from .models import Professor
from .models import Subject
from .models import School


def index(request): 
    return render(request, 'eDnevnikApp/index.html')

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
        if Professor.objects.filter(studentoib = request.POST.get('OIB')).exists():
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

def professorPage(request):
    return render(request, 'eDnevnikApp/professorPage.html')