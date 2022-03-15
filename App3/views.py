from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def login(request):
    if 'POST' == request.method:
        user = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        myuser = auth.authenticate(username=user, password=password1)
        if myuser is not None:
            auth.login(request, myuser)
            return redirect("/")

        else:
            print("Hi User You have successfully login")

    return render(request, 'login.html')

