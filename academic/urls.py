from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='academic-home'),
    path('about/', views.about, name='academic-about'),
    path('dual/', views.dual, name='dual'),
    path('restart/', views.restart, name='restart'),
    path('term/', views.terminate, name='terminate'),
    path('btechstudent/', views.btechstudent, name='academic-btechstudent'),
    path('btechstudent1/', views.btechstudent1, name='academic-btechstudent1'),
    path('student/', views.student, name='student'),
    path('planning/', views.planning, name='planning'),
    path('shivani/', views.shivani, name='shivani'),
    path('searching/', views.searching, name='searching'),
    path('cascade/', views.cascadingddl, name='cascade'),
    path('studentlist/', views.studentlist, name='studentlist'),    
]
