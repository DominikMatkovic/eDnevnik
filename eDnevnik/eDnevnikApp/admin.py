from django.contrib import admin

from .models import Professor, School, Student, Studentsubjecttable, Subject 

admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Studentsubjecttable)