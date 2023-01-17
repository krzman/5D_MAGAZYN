# Import django module
import http.client

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

# Import project module
from storage_5d_pr.forms import *
from storage_5d_pr.models import *


# Create your views here.

# Main page / login
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


# Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# Page add workers
class WorkersAdd(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Workers
    fields = ['name', 'surname', 'phone', 'company']
    template_name = 'workers-add.html'
    success_url = reverse_lazy('workers_list')


# Page list all workers
class WrokersList(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        workers = Workers.objects.all()
        context = {
            'workers': workers
        }
        return render(request, 'workers-list.html', context=context)


# Page add tool
class ToolAdd(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = FormWorkersAdd
    template_name = 'tools-add.html'
    success_url = reverse_lazy('tools_list')


# PAge list all tools
class ToolList(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        tools = Tools.objects.all()
        context = {
            'tools': tools
        }
        return render(request, 'tools-list.html', context=context)
