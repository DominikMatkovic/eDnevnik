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

        return redirect('studentPage/'+ request.POST.get('OIB'))
    return render(request, 'eDnevnikApp/studentLogin.html')

def professorLogin(request):

    
    
    return render(request, 'eDnevnikApp/professorLogin.html')



def studentPage(request,studentOIB):
    #studenti  = Student.objects.all()
    context = {'studentOIB': studentOIB}
    return render(request, 'eDnevnikApp/studentPage.html',context)

def professorPage(request):
    return render(request, 'eDnevnikApp/professorPage.html')