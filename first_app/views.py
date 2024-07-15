from django.shortcuts import render, redirect
from .forms import RegisterForm, CreateCompany
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from first_app.models import ListCompany


# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'Register.html', {'form': form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)           # check korcha user database a acha kina.
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)  
                return redirect('profile')
        
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)  
                return redirect('profile')
        
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login') 

def create_company(request):
    if request.method == 'POST':
        company_form = CreateCompany(request.POST)
        if company_form.is_valid():
            company_form.save()
            print(company_form.cleaned_data)
            return redirect('list_company')
    else:
        company_form = CreateCompany()
    return render(request, 'create_company.html', {'form': company_form})
        
def list_company(request):
    company = ListCompany.objects.all()
    return render(request, 'list_company.html', {'data': company})

def edit(request):
    return render(request, 'list_company.html')


def delete(request):
    return render(request, 'list_company.html')
    