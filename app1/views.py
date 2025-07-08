
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        
        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        print("DOB:", dob)
        print("Gender:", gender)
        my_user = User.objects.create_user(username=name, email=email, password=password)
        my_user.save()
        return redirect('loginpage')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(request,email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            return HttpResponse('Wrong username or password !!!')

    return render(request, 'login.html')