# Import django module
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Import project module
from storage_5d_pr.forms import *
from storage_5d_pr.models import *


# Create your views here.

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'login.html')
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
    def get(self, request):
        logout(request)
        return redirect('login')


# class ToolsAdd(LoginRequiredMixin, CreateView):
#     login_url = '/login/'
#     model = Tools
#     fields =
#     success_url = reverse_lazy('login')

class WorkersAdd(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Workers
    fields = ['name', 'surname', 'phone', 'company']
    template_name = 'workers_add.html'
    success_url = reverse_lazy('workers_list')


class WrokersList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        workers = Workers.objects.all()
        context = {
            'workers': workers
        }
        return render(request, 'workers_list.html', context=context)
