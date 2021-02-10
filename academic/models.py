from django.db import connections
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):

    course_slot = models.CharField(max_length = 10)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    course_credit = models.FloatField()
    course_ltp = models.CharField(max_length = 100)
    max_limit = models.IntegerField()
    coordinator =  models.CharField(max_length = 100)
    class Meta:
        db_table = "course1801"


class CsBtech(models.Model):

    semester = models.CharField(max_length = 100)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    course_slot = models.CharField(max_length = 100)
    graded_ng = models.IntegerField()
    one_of_three = models.IntegerField()
    course_credit = models.FloatField()
    class Meta: 
        db_table = "cs_btech"               

class CatNames(models.Model):
    
    cid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length = 100)
    class Meta: 
        db_table = "names_cats"


class DepNames(models.Model):
    
    did = models.IntegerField(primary_key=True)
    depart = models.CharField(max_length = 100)
    class Meta: 
        db_table = "names_deps"

class CourseOffered(models.Model):

    course_id = models.IntegerField(primary_key=True)
    depart = models.CharField(max_length = 100)
    did = models.IntegerField()
    category = models.CharField(max_length = 100)
    cid = models.IntegerField()
    course_code = models.CharField(max_length = 100)
    course_title = models.CharField(max_length = 100)
    slot = models.CharField(max_length = 100)
    credits = models.CharField(max_length = 100)
    course_ltp = models.CharField(max_length = 100)
    coordinator = models.CharField(max_length = 100)
    max_limit = models.CharField(max_length = 100)
  
    class Meta: 
        db_table = "courses_offered"

## Newer Models ## 


class BtechStudents(models.Model):

    semester = models.CharField(max_length = 100)
    sem_title = models.CharField(max_length = 20)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    course_cat = models.CharField(max_length = 20)
    course_slot = models.CharField(max_length = 100)
    graded_ng = models.IntegerField()
    one_of_three = models.IntegerField()
    credits = models.FloatField()
    grades = models.CharField(max_length = 10)
    course_no = models.CharField(max_length = 5)
    class Meta: 
        db_table = "btech_student"  


class Termin(models.Model):

    logical_sem = models.CharField(max_length = 100)
    semester = models.CharField(max_length = 100)
    sem_title = models.CharField(max_length = 20)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    course_cat = models.CharField(max_length = 20)
    credits = models.FloatField()
    grades = models.CharField(max_length = 10)

    class Meta: 
        db_table = "btech_term" 


class Restarting(models.Model):
    
    logical_sem = models.CharField(max_length = 100)
    semester = models.CharField(max_length = 100)
    sem_title = models.CharField(max_length = 20)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    course_cat = models.CharField(max_length = 20)
    credits = models.FloatField()
    grades = models.CharField(max_length = 10)

    class Meta: 
        db_table = "btech_restart"   



class Planning(models.Model):
    
    logical_sem = models.CharField(max_length = 100)
    semester = models.CharField(max_length = 100)
    sem_title = models.CharField(max_length = 20)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    slot = models.CharField(max_length = 5)
    course_cat = models.CharField(max_length = 20)
    credits = models.FloatField()
    grades = models.CharField(max_length = 10)

    class Meta: 
        db_table = "btech_plan"               





class Shivani(models.Model):

    semester = models.CharField(max_length = 100)
    sem_title = models.CharField(max_length = 20)
    course_code = models.CharField(max_length = 10)
    course_title = models.CharField(max_length = 100)
    course_cat = models.CharField(max_length = 20)
    credits = models.FloatField()
    grades = models.CharField(max_length = 10)
   
    class Meta: 
        db_table = "btech_shivani"   








