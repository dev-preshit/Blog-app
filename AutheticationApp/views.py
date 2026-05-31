from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from blog_main.forms import registration_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


# Create your views here.
def register_page(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            print(form.errors)
    else:
        form = registration_form()
    print(form)
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'login.html',context)

def logout_page(request):
    auth.logout(request)
    return redirect('login_page')