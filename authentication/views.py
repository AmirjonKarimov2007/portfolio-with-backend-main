from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    return render(request, 'auth-boxed-register.html')


def logout_view(request):
    try:
        logout(request)
    except Exception as e:
        print(f'Chiqish amalga oshmadi: {e}')

    return redirect('login')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print('Tizimga xatolik yuz berdi!')

    return render(request, 'auth-boxed-login.html')

def forgotpassword(request):
    return render(request,'auth-boxed-forgot-password.html')