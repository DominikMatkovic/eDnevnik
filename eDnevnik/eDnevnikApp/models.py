from django.db import models

class Professor(models.Model):
    professoroib = models.CharField(db_column='professorOIB', primary_key=True, max_length=11)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    homeadress = models.CharField(db_column='homeAdress', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45)  # Field name made lowercase.
    worksatfkid = models.ForeignKey('School', models.DO_NOTHING, db_column='worksAtFKId', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='birthDate')  # Field name made lowercase.
    def __str__(self):
        return self.professoroib
    class Meta:
        db_table = 'professor'

class School(models.Model):
    schoolname = models.CharField(db_column='schoolName', unique=True, max_length=45)  # Field name made lowercase.
    adress = models.CharField(max_length=45)
    website = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.schoolname
    class Meta:
        db_table = 'school'

class Student(models.Model):
    studentoib = models.CharField(db_column='studentOIB', primary_key=True, max_length=11)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    homeadress = models.CharField(db_column='homeAdress', max_length=45)  # Field name made lowercase.
    attendsfkid = models.ForeignKey(School, models.DO_NOTHING, db_column='attendsFKId', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='birthDate')  # Field name made lowercase.
    def __str__(self):
        return self.studentoib
    class Meta:
        db_table = 'student'

class Studentsubjecttable(models.Model):
    fksubjectid = models.ForeignKey('Subject', models.DO_NOTHING, db_column='FKSubjectId')  # Field name made lowercase.
    fkstudentoib = models.ForeignKey(Student, models.DO_NOTHING, db_column='FKStudentOIB')  # Field name made lowercase.
    grade = models.FloatField(blank=True, null=True)
    class Meta:
        db_table = 'studentsubjecttable'

class Subject(models.Model):
    subjectid = models.AutoField(db_column='subjectId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=1000)
    taughtbyfkprofessoroib = models.ForeignKey(Professor, models.DO_NOTHING, db_column='taughtByFKProfessorOIB', blank=True, null=True)  # Field name made lowercase.
    taughtatfkid = models.ForeignKey(School, models.DO_NOTHING, db_column='taughtAtFKId', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'subject'
