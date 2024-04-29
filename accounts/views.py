from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
# Create your views here.


def login_accounts(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':

        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def signup_accounts(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/login.html')
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@login_required
def logout_accounts(request):

    logout(request)
    return redirect('/')


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'email is already exists')
            return redirect('register')
        else:
            user = User(email=email, password=password, first_name=firstname,
                        last_name=lastname, username=username)
            user.set_password(password)
            user.save()
            subject = 'About Registration'
            message = f'Hi ,You has been registered successfully on website.'
            email_from = 'sinturana250@gmail.com'
            rec_list = [email,]
            response = send_mail(
                subject,
                message,
                email_from,
                rec_list,
                fail_silently=False
            )
            print("UYFRUYYUBTYUTBYUTUYBGUN", response)

            messages.success(request, 'User has been sucessfully registered')
            return redirect('/')
    return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'accounts/login1.html')


def logout_user(request):
    logout(request)
    return redirect('/')
