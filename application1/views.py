from django.shortcuts import render,redirect
from application1.forms3 import addhodFORM
from application1.models import FEES
from application1.form4 import FEESFORMS
from application1.models import addhod
from application1.forms import studentsFORMS
from application1.forms1 import detailsFORMS
from application1.models import students,details
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

def home_page(request):
    bb=students.objects.all()
    cou=0
    for x in bb:
        cou+=1
   
    
    return render(request,'frontend/home.html',{'cou':cou})

def new_student(request):
    data101=students.objects.all()
    form=studentsFORMS()
    if request.method=='POST':
        form= studentsFORMS(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
    context={
        'data101':data101,
        'form':form,
    }
    return render(request,'frontend/students.html',context)



def edit(request,id):
    data2= students.objects.get(id=id)
    if request.method=='POST':
        form=studentsFORMS(request.POST,instance=data2)
        if form.is_valid():
            form.save()
            return redirect('new_student')
    else:
        form = studentsFORMS(instance=data2)
        context={
            'form':form
        }
    return render(request,'frontend/edit.html',context)



def delete(request,pk):
    data=students.objects.get(id=pk)
    data.delete()
    return redirect('new_student')

def std_full_details(request):
    data=request.GET.get('src',None)
    if data:
        pk= details.objects.filter(F_name__icontains=data)
    else:
        pk=details.objects.all()

    context={
        'pk':pk
    }
    return render(request,'frontend/std_full_details.html',context)


def student_details(request):
   form1=detailsFORMS()
   if request.method=='POST':
        form1= detailsFORMS(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('student_details')
   context={
       'form1':form1,
       
    }
   return render(request,'frontend/std_details.html',context)


def std_details_edit(request,id):
 
    data2= details.objects.get(id=id)
    if request.method =='POST':
        form2 = detailsFORMS(request.POST,instance=data2)
        if form2.is_valid():
            form2.save()
            return redirect('new_student')

    else:
        form2 = detailsFORMS(instance=data2)
    context={
            'form2':form2
        }
    return render(request,'frontend/std_edit.html',context)



def newhod(request):
    data10 = addhod.objects.all()
    form4 = addhodFORM()
    if request.method=='POST':
        form4 = addhodFORM(request.POST)
        if form4.is_valid():
            form4.save()
            
    context={
        'form4':form4,
        'data10':data10
    }
    return render(request,'frontend/newhod.html',context)

def hod_delete(request,HD):
    data_hod= addhod.objects.filter(id=HD)
    data_hod.delete()
    return redirect('newhod')



def hod_edit(request,id):
    data3= addhod.objects.get(id=id)
    if request.method =='POST':
        form3 = addhodFORM(request.POST,instance=data3)
        if form3.is_valid():
            form3.save()
            return redirect('newhod')

    else:
        form3 = addhodFORM(instance=data3)
        context={
            'form3':form3,
            
        }
    return render(request,'frontend/hod_edit.html',context)

def feesdetails(request):
    data10 = FEES.objects.all()
    form123 = FEESFORMS()
    if request.method=='POST':
        form123 = FEESFORMS(request.POST)
        if form123.is_valid():
            form123.save()
    context={
        'data10':data10,
        'form123':form123
    }
    return render(request,'frontend/feesdetails.html',context)

def feesedit(request,id):
    data120 = FEES.objects.get(id=id)

    if request.method=='POST':
        form120=FEESFORMS(request.POST,instance=data120)
        if form120.is_valid():
            form120.save()
    else:
        form120=FEESFORMS(instance=data120)
    context={'form120':form120}
    return render(request,'frontend/editfees.html',context)



def register(request):
    message = ''
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        conpassword = request.POST.get('con_password')

        if password == conpassword:
            try:
                # Create the user
                user = User.objects.create_user(username=name, email=email, password=password)
                # Optionally, you can save the mobile number to the user profile or extend User model
                user.profile.mobile = mobile  # Assuming a custom profile model with a mobile field
                user.profile.save()  # If you have a custom model for additional fields
                # Redirect to login after successful registration
                # return redirect('login')  # Ensure 'login' is the correct URL name for your login page
            except Exception as e:
                # Handle the case where the user already exists or other exceptions
                message = 'User Already Exists: ' + str(e)
                return redirect('login')
        else:
            message = 'Passwords do not match.'

    return render(request, 'frontend/register.html', {'message': message})




def login_view(request):
    message = ''
    if request.method == 'POST':
        usernamee = request.POST.get('username')
        passwordd = request.POST.get('password')
        
        # Use the authenticate function to check if the user exists and password matches
        user = authenticate(request, username=usernamee, password=passwordd)
        
        if user is not None:
            # Log the user in if authentication is successful
            login(request, user)
            return redirect('home')  # Redirect to the home page (or another page you want)
        else:
            message = 'Invalid username or password.'

    return render(request, 'frontend/login.html', {'message': message})
