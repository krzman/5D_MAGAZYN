# Import django module
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Import project module
from storage_5d_pr.templates import *
from storage_5d_pr.forms import *


# Create your views here.

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {'mess': 'Zalogowany'}
            return render(request, 'login.html', context=context)
        else:
            form = FormLogin()
            context = {'form': form}
            return render(request, 'login.html', context=context)

    def post(self, request):
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
        context = {
            'mess': 'Wprowadzono złe dane',
            'form': form,
        }
        return render(request, 'login.html', context=context)

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')