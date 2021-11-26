from rest_framework import serializers
from .models import School
from .models import Student
from .models import Studentsubjecttable
from .models import Subject
from .models import Professor

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'schoolname', 'adress', 'website']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentoib', 'name', 'lastname', 'email','homeadress','attendsfkid','birthdate']

class StudentsubjecttableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studentsubjecttable
        fields = ['id', 'fksubjectid', 'fkstudentoib', 'grade']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subjectid', 'name', 'description', 'taughtbyfkprofessoroib','taughtatfkid']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['professoroib', 'firstname', 'lastname', 'email','homeadress','phonenumber','worksatfkid','birthdate']
