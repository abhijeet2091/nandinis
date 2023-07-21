
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import User

def login_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username = username, password = password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            messages.success(req,('Invalid login!'))
            return redirect('/members/login/')
    else:
        return render(req,'authenticate/login.html', {})

def logout_user(req):
    logout(req)
    messages.success(req,('You are logged out!'))
    return redirect('/')

def register_user(req):
   if req.method == "POST":
       print('checking register post method')
       mobile = req.POST['mobile']
       email = req.POST['email']
       password1 = req.POST['password1']
       password2 = req.POST['password2']
       first_name = req.POST['first_name']
       last_name = req.POST['last_name']
       address1 = req.POST['address1']
       address2 = req.POST['address2']
       address3 = req.POST['address3']
       address4 = req.POST['address4']
       address5 = req.POST['address5']
       address6 = req.POST['address6']

       if User.objects.filter(email=email).exists():
           messages.info(req,'Email id already exists')
           return redirect(req,'autheticate/register.html',{})
       else:
           user = User.objects.create_user(mobile=mobile, email=email, password=password1, first_name=first_name,
                                       last_name=last_name, address1=address1, address2=address2, address3=address3,
                                       address4=address4, address5=address5, address6=address6)
           user.save()
           login(req,user)
           return redirect('/')
   
   return render(req,'authenticate/register.html',{})

   """ if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(req, username = username, password = password)
            login(req, user)
            messages.success(req,('Registration successful!'))
            return redirect('/')
        else:
            messages.success(req,('There is an error!'))
    else:
        form = UserCreationForm()

    return render(req,'authenticate/register.html',{'form': form})
    """