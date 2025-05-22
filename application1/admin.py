from django.contrib import admin

from application1.models import students,details
from application1.models import FEES,addhod

class studentADMIN(admin.ModelAdmin):
    list_display=['ROOL_NO','s_name','s_Department']
admin.site.register(students,studentADMIN)

class detailsADMIN(admin.ModelAdmin):
    list_display=['select_Rool_number','F_name','mobile','email','District','Mandal','Village']
admin.site.register(details,detailsADMIN)

class FEESADMIN(admin.ModelAdmin):
    list_display=['Select_Department','Department_Fees']
admin.site.register(FEES,FEESADMIN)

class addhodADMIN(admin.ModelAdmin):
    list_display=['name','Department','joinig_date','hodmobile']
admin.site.register(addhod,addhodADMIN)


