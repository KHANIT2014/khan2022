from django.shortcuts import render, HttpResponse


# Create your views here.

# def contact(request):

#     return render(request,'hi.js')


def contact(request):
    a = int(request.GET['text'])
    b = int(request.GET['text1'])
    c = a + 2 * b
    return render(request, 'Registration.html', {'result': c})


def signup(request):
    return render(request, 'signup.html')
