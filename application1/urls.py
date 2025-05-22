
from django.urls import path
from application1.views import new_student,home_page,edit,delete
from application1.views import std_details_edit,student_details,newhod,hod_delete
from application1.views import hod_edit
from application1.views import std_full_details,feesdetails
from application1.views import feesedit
from application1.views import register,login_view

urlpatterns = [
    path('',register,name='register'),
    path('login',login_view,name='login'),
    path('homepage',home_page,name='home'),
    path('new_student',new_student,name='new_student'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:pk>/',delete, name='delete'),
    path('std_details',student_details,name='student_details'),
    path('std_details/<int:id>/',std_details_edit,name='std_dt_edit'),
   
    path('newhod',newhod,name='newhod'),
    path('hoddelete/<int:HD>/',hod_delete, name='hoddelete'),
    path('hod_edit/<int:id>/',hod_edit, name='hod_editer'),
    path('std_full',std_full_details,name='srcs'),
    path('feesdetails',feesdetails,name='fees_details'),
    path('feesedit/<int:id>/',feesedit,name='feesedit')
   
]