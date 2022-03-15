# import username as username
from django.contrib.auth.models import User,auth
from django.shortcuts import render, HttpResponse, redirect
# from datetime import datetime
# from .models import contact
# from django.contrib import messages


# from .models import contact
# from django.contrib import messages

# Create your views here.

# def contact(request):

#     return render(request,'hi.js')


def contact(request):
    a = int(request.GET['text'])
    b = int(request.GET['text1'])
    c = a + 2 * b
    return render(request, 'Registration.html', {'result': c})


def signup(request):
    if request.method=="POST":
        name = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        datetime = request.POST['date_joined']
        myuser = User.objects.create_user(username=name, first_name=fname, last_name=lname, email=email,
                                          password=password, date_joined=datetime)
        myuser.save()
        print("user created successfully")

        return redirect('/')
    else:
        return render(request, 'signup.html')




