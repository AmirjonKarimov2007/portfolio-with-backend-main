from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, '{%url 'login'%}l')
def forgotpassword(request):
    return render(request,'auth-boxed-forgot-password.html')