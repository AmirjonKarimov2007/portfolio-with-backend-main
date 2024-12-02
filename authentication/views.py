from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken. Please choose another.')
                return render(request, 'auth-boxed-register.html', {'form': form})

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Log the user in
            login(request, user)

            # Redirect to the profile page
            return redirect('/')  # Replace with your actual profile URL

    else:
        form = RegistrationForm()

    return render(request, 'auth-boxed-register.html', {'form': form})


def logout_view(request):
    try:
        logout(request)
    except Exception as e:
        print(f'Chiqish amalga oshmadi: {e}')

    return redirect('login')


from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        if username_or_email and password:
            try:
                # Username orqali tekshirish
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                # Email orqali tekshirish
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                # Autentifikatsiya qilish
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    print('Tizimga xatolik yuz berdi!')

    return render(request, 'auth-boxed-login.html')
def forgotpassword(request):
    return render(request,'auth-boxed-forgot-password.html')




def captchaview(request):
    return render(request,template_name="auth-bot-captcha.html")