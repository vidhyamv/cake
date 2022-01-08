from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from . models import Cake


def login(request):
    if request.method == 'POST':
        print("hii")
        Username=request.POST['Username']
        Password=request.POST['Password']
        user=auth.authenticate(username=Username,password=Password)
        if user is None:
            messages.info(request,"username invalid")

        else:
            return redirect('order')
    # messages.info(request,"invalid credential")
        # messages.info(request, "Username in")

    # else:
    #     print("bye")
    #     # return redirect('order')
    return render(request,"login.html")

def allprodcat(request):
    cake = Cake.objects.all()
    return render(request, 'product.html', {'cake': cake})

def register(request):
    print("REGISTER")
    if request.method == 'POST':
        print("post==>")
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        Username=request.POST['Username']
        Password=request.POST['Password']
        CPassword=request.POST['Conform_Password']
        if Password==CPassword:
            print("pass ok")
            if User.objects.filter(username=Username).exists():
                messages.info(request,"Username taken")
                print("user exist")
                    # return redirect('register')
            else:
                user = User.objects.create_user(first_name=FirstName, last_name=LastName, username=Username, password=Password,)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            print("chek pass")
            # return redirect('register')

    return render(request,"registration.html")

def order(request):

    return render(request,"order.html")

def logout(request):
    auth.logout(request)
    return redirect('login')



