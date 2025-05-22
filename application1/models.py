from django.db import models

class students(models.Model):
    ROOL_NO=models.CharField(max_length=4)
    s_name=models.CharField(max_length=20)
    s_Department=models.CharField(max_length=20)

    def __str__(self):
        return self.ROOL_NO

class details(models.Model):
    select_Rool_number=models.OneToOneField(students,on_delete=models.CASCADE)
    F_name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    District=models.CharField(max_length=20)
    Mandal=models.CharField(max_length=20)
    Village=models.CharField(max_length=20)

    def __str__(self):
        return f'details{self.name1.ROOL_NO}'

class addhod(models.Model):
    name = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    joinig_date = models.DateField()
    hodmobile = models.CharField(max_length=10)

class FEES(models.Model):

    Select_Department=models.CharField(max_length=20)
    Department_Fees=models.IntegerField()





