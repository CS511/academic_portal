from django.shortcuts import render
from .models import Course
from .models import CsBtech
from .models import BtechC
from .models import DualC
from .models import BtechStudents
from .models import Termin
from .models import Restarting
from .models import Planning
from .models import Shivani
from .models import CatNames
from .models import DepNames
from .models import CourseOffered

import pandas as pd
import numpy as np
import json


def home(request):
    context = {
        'posts': Course.objects.all
    }  
    return render(request, 'academic/home.html', context)

def about(request):
    cscourses = BtechStudents.objects.all()
    return render(request, 'academic/about.html', {'cscourses':cscourses})  

   

######################################

def planning(request):
    btechcourses = BtechC.objects.all()
    return render(request, 'academic/planning.html', {'btechcourses':btechcourses})      

def dual(request):
    dualcourses = DualC.objects.all()
    return render(request, 'academic/dual.html', {'dualcourses':dualcourses}) 

def studentlist(request):
    sem1 = BtechStudents.objects.raw('SELECT * FROM btech_student GROUP BY semester')
    sem2list =  BtechStudents.objects.all()

    context = {
    'sem1': sem1,
    'sem2list': sem2list
    }
    return render(request, 'academic/studentlist.html', context)    


## in the view given below, the context has two parameters, one if for courses of semester 1 and one is for all courses given in the model
def btechstudent(request):
    sem1 = BtechStudents.objects.raw('SELECT * FROM btech_student GROUP BY semester')
    sem2 =  BtechStudents.objects.all()

    context = {
    'sem1': sem1,
    'sem2': sem2
    }
    return render(request, 'academic/btechstudent.html', context)  

def searching(request):
    courses = Course.objects.all()
    return render(request, 'academic/searching.html', {'courses':courses})  


def cascadingddl(request):
    depobj = DepNames.objects.all()
    catobj = CatNames.objects.all()
    courseobj = CourseOffered.objects.all()

    return render(request, 'academic/cascade.html', {'Depart':depobj, 'Category':catobj, 'Course':courseobj})


def btechstudent1(request):
    sem3 =  BtechStudents.objects.all().values()
    df = pd.DataFrame(sem3)
    df_1 = df.pivot(index='semester', columns='course_no', values='course_code').reset_index()
    df_2 = df.pivot_table(index='semester', columns='course_no', values='credits', aggfunc='first').reset_index()
    print(df_2)

    def grades_to_num(grades):
        grades_dict = {"A":10,"A-":9, "B":8,"B-":7, "C":6,"C-":5,"D":4,"E":2,"F":0}

    df['grades'] = df['grades'].apply(grades_to_num)


    df_3 = df.pivot_table(index='semester', columns='course_no', values='grades', aggfunc='first').reset_index()
    df_4 = df_1.append(df_2).reset_index(drop=True).append(df_3).reset_index(drop=True).sort_values(by=['semester']).reset_index(drop=True)
    df_4['sem_change'] = df_4.semester != df_4.semester.shift()
    sem_change_idx = df_4[df_4.sem_change == True].index.values

    for idx in sem_change_idx:
        df_4.semester.iloc[idx+1] = 'grades'
        df_4.semester.iloc[idx+2] = 'credits'
    df_4 = df_4.set_index('semester')
    df_4 = df_4.drop(['sem_change'],axis=1)

    df_4.loc[:,'Total'] = df_4.sum(axis=1)
    
    df['combined']=df['course_code'].astype(str)+'('+df['credits']+')'+'('+df['grades']+')'
    df3 = df.reset_index().pivot(index='semester', columns='course_no', values='combined')

    df3.loc[:,'Total Credits'] = df3.sum(axis=1)
    data4 = df3.to_html()


    
    json_records = df_4.reset_index().to_json(orient ='records') 
    data3 = [] 
    data3= json.loads(json_records)

    json_records1 = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records1) 

    context = {
    'data4': data4,
    'data5': data,
    'data6': data3
    } 
    
    return render(request, 'academic/btechstudent1.html', context) 


def student(request):

    grid = BtechStudents.objects.all().values()
    gdf = pd.DataFrame(grid)

    gdf.groupby(['semester','course_code'])['credits'].sum().reset_index()
    gdf['total_credits'] = gdf['credits']

    def grades_to_num(grades):
        grades_dict = {"A":10,"A-":9, "B":8,"B-":7, "C":6,"C-":5,"D":4,"E":2,"F":0}

    gdf['grades'] = gdf['grades'].apply(grades_to_num)

    gdf['combined']=gdf['course_code'].astype(str)+'\n'+'('+gdf['course_cat']+')'+'\n'+'('+gdf['credits']+')'+' '+'Credit'+'\n'+'('+gdf['grades']+')'+' '+'Grade'
    gdf['newsem']=gdf['semester'].astype(str)+'\n'+gdf['sem_title']
    df_3 = gdf.reset_index().pivot(index='newsem', columns='course_no', values='combined')

    df_4 = df_3.replace(np.nan, '', regex=True)
        
    json_records2 = df_4.reset_index().to_json(orient ='records') 
    datag = [] 
    datag= json.loads(json_records2)
   

    context = {
    'datag': datag
    }

    return render(request, 'academic/student.html', context)


##### Cases here 


def restart(request):

    rgrid = Restarting.objects.all().values()
    rgdf = pd.DataFrame(rgrid)

    def grades_to_num(grades):
        grades_dict = {"A":10,"A-":9, "B":8,"B-":7, "C":6,"C-":5,"D":4,"E":2,"F":0}

    rdf['grades'] = rdf['grades'].apply(grades_to_num)

    rgdf.groupby(['semester','course_code'])['credits'].sum().reset_index()
    rgdf['total_credits'] = rgdf['credits']
    rgdf['combined']=rgdf['course_code'].astype(str)+'\n'+'('+rgdf['course_cat']+')'+'\n'+'('+rgdf['credits']+')'+' '+'Credit'+'\n'+'('+rgdf['grades']+')'+' '+'Grade'
    rgdf['newsem']=rgdf['logical_sem'].astype(str)+ '(Chron.)'+ '\n'+rgdf['semester']+ '(Log.)'+'\n'+rgdf['sem_title']
    rdf_3 = rgdf.reset_index().pivot(index='newsem', columns='course_no', values='combined')

    rdf_4 = rdf_3.replace(np.nan, '', regex=True)
    
        
    json_records2 = rdf_4.reset_index().to_json(orient ='records') 
    datares = [] 
    datares= json.loads(json_records2)
   

    context = {
    'datares': datares
    }

    return render(request, 'academic/restart.html', context)

   


def terminate(request):

    tgrid = Termin.objects.all().values()
    tgdf = pd.DataFrame(tgrid)

    def grades_to_num(grades):
        grades_dict = {"A":10,"A-":9, "B":8,"B-":7, "C":6,"C-":5,"D":4,"E":2,"F":0}

    tdf['grades'] = tdf['grades'].apply(grades_to_num)

    tgdf.groupby(['semester','course_code'])['credits'].sum().reset_index()
    tgdf['total_credits'] = gdf['credits']
    tgdf['combined']=tgdf['course_code'].astype(str)+'\n'+'('+tgdf['course_cat']+')'+'\n'+'('+tgdf['credits']+')'+' '+'Credit'+'\n'+'('+tgdf['grades']+')'+' '+'Grade'
    tgdf['newsem']= tgdf['logical_sem'].astype(str)+ '(Chron.)'+ '\n'+tgdf['semester']+ '(Log.)'+'\n'+tgdf['sem_title']
    tdf_3 = tgdf.reset_index().pivot(index='newsem', columns='course_no', values='combined')

    tdf_4 = tdf_3.replace(np.nan, '', regex=True)

        
    json_records2 = tdf_4.reset_index().to_json(orient ='records') 
    dataterm = [] 
    dataterm= json.loads(json_records2)
   

    context = {
    'dataterm': dataterm
    }

    return render(request, 'academic/term.html', context)



def planning(request):

    depobj = DepNames.objects.all()
    catobj = CatNames.objects.all()
    courseobj = CourseOffered.objects.all()
    fixedc = BtechStudents.objects.all()


    fixedp = pd.DataFrame(fixedc)
    fixedp['combined']= fixedp['course_code'].astype(str)+'\n'+'('+ fixedp['course_cat']+')'+'\n'+'('+ fixedp['credits']+')'+' '+'Credit'+'\n'+'('+ fixedp['grades']+')'+' '+'Grade'
    fixedp['newsem']=fixedp'semester'].astype(str)+'\n'+fixedp['sem_title']
    df_3f = fixedp.reset_index().pivot(index='newsem', columns='course_no', values='combined')
    df_4f = df_3f.replace(np.nan, '', regex=True)

    json_records1 = df_4f.reset_index().to_json(orient ='records') 
    fixed = [] 
    fixed = json.loads(json_records1)

    gridp = Planning.objects.all().values()
    gdfp = pd.DataFrame(gridp)

    def grades_to_num(grades):
        grades_dict = {"A":10,"A-":9, "B":8,"B-":7, "C":6,"C-":5,"D":4,"E":2,"F":0}

    gridfp['grades'] = gridfp['grades'].apply(grades_to_num)

    gdfp.groupby(['semester','course_code'])['credits'].sum().reset_index()
    gdfp['total_credits'] = gdfp['credits']
    gdfp['combined']=gdfp['course_code'].astype(str)+'\n'+'('+gdfp['course_cat']+')'+'\n'+'('+gdfp['credits']+')'+' '+'Credit'+'\n'+'('+gdfp['grades']+')'+' '+'Grade'
    gdfp['newsem']=gdfp['semester'].astype(str)+'\n'+gdfp['sem_title']
   

    gdfp['combined'] = gdfp['combined'].apply(lambda x: x.replace('() Credit', ''))
    gdfp['combined'] = gdfp['combined'].apply(lambda x: x.replace('() Grade', ''))

    df_3p = gdfp.reset_index().pivot(index='newsem', columns='course_no', values='combined')
    df_4p = df_3p.replace(np.nan, '', regex=True)

        
    json_records2 = df_4p.reset_index().to_json(orient ='records') 
    planned = [] 
    planned= json.loads(json_records2)
   

    context = {
    'planned': planned,
    'Depart':depobj,
    'Category':catobj,
    'Course':courseobj
    'fixed':fixed
    }

    return render(request, 'academic/planning.html', context)



def shivani(request):

    grid = Shivani.objects.all().values()
    gdf = pd.DataFrame(grid)

    def grades_to_num(grades):
        grades_dict = {"A":10,"A-":9, "B":8,"B-":7, "C":6,"C-":5,"D":4,"E":2,"F":0}

    gdf['grades'] = gdf['grades'].apply(grades_to_num)

    gdf.groupby(['semester','course_code'])['credits'].sum().reset_index()
    gdf['total_credits'] = gdf['credits']
    gdf['combined']=gdf['course_code'].astype(str)+'\n'+'('+gdf['course_cat']+')'+'\n'+'('+gdf['credits']+')'+' '+'Credit'+'\n'+'('+gdf['grades']+')'+' '+'Grade'
    gdf['newsem']=gdf['semester'].astype(str)+'\n'+gdf['sem_title']
    df_3 = gdf.reset_index().pivot(index='newsem', columns='course_no', values='combined')

    df_4 = df_3.replace(np.nan, '', regex=True)
    
        
    json_records2 = df_4.reset_index().to_json(orient ='records') 
    datashiv = [] 
    datashiv= json.loads(json_records2)
   

    context = {
    'datashiv': datashiv,
    'grid': grid
    }

    return render(request, 'academic/shivani_sem.html', context)    

